#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
import argparse

PUNC_LIST = (u'\uff0c', u'\u3002') # 逗号和句号
WORDS_PER_SENTENCE = (5, 15)       # 每句词语数
SENTENCE_PER_PARAGRAPH = (3, 10)   # 每段落句数


class BaseLorem(object):
    def __init__(self):
        self.character_list = []

    def gen_character(self):
        pass

    def gen_word(self):
        pass

    def gen_sentence(self):
        number = random.choice(range(WORDS_PER_SENTENCE[0],
                                     WORDS_PER_SENTENCE[1]))
        sentence = ''
        for i in range(number):
            sentence += self.gen_word()
        return sentence
    
    def gen_paragraph(self):
        number = random.choice(range(SENTENCE_PER_PARAGRAPH[0],
                                     SENTENCE_PER_PARAGRAPH[1]))
        paragraph = ''
        for i in range(number):
            paragraph += self.gen_sentence() + PUNC_LIST[0]
        paragraph = paragraph[:-1] + PUNC_LIST[1]
        return paragraph

        
class MeaningLorem(BaseLorem):
    def __init__(self):
        BaseLorem.__init__(self)
        with open('word.txt') as words:
            all_words = words.read().decode('utf-8')
            self.character_list = list(set(list(all_words.replace('\n', ''))))
            self.word_list = all_words.split('\n')[:-1]
            
    def gen_character(self):
        return random.choice(self.character_list)
            
    def gen_word(self):
        return random.choice(self.word_list)


class GabbleLorem(BaseLorem):
    def __init__(self):
        BaseLorem.__init__(self)
        self.character_list = xrange(0x4e00, 0x9fa5)

    def gen_character(self):
        return unichr(random.choice(self.character_list))

    def gen_word(self):
        number = random.choice([2, 3, 4])
        word = ''
        for i in range(number):
            word += self.gen_character()
        return word


if __name__ == '__main__':
    def print_out(func, number):
        result = []
        for i in range(number):
            result.append(func())
        return '\n'.join(result)
        
    def main():
        parser = argparse.ArgumentParser(description='A chinese lorem ipsum generator.')
        parser.add_argument('-z', dest='meaning', type=int,
                            help='Meaning(1) or Gabble(0)? The default value is 1.')
        parser.add_argument('-t', dest='gentype',
                            help='Generate what? c:character w:word s:sentence p:paragraph.')
        parser.add_argument('-n', dest='number', type=int,
                            help='How many to generate?')
        parser.set_defaults(meaning=1, gentype='p', number=1)
        args = parser.parse_args()

        if args.meaning:
            lorem = MeaningLorem()
        else:
            lorem = GabbleLorem()

        print_dict = {
            'c': print_out(lorem.gen_character, args.number),
            'w': print_out(lorem.gen_word, args.number),
            's': print_out(lorem.gen_sentence, args.number),
            'p': print_out(lorem.gen_paragraph, args.number)
        }

        if args.gentype in print_dict:
            print print_dict[args.gentype]
        else:
            print parser.print_help()
            sys.exit(1)

    main()

        
