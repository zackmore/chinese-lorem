# -*- coding: utf-8 -*-

import math
import random
import argparse

punc_list = [u'，', u'。', u'！', u'？']
all_words = open('word.txt').read()
word_list = all_words.decode('utf-8').split('\n')[:-1]


class LoremGenerator(object):
    def __init__(self, paragraph):
        self.paragraph = paragraph

    def generate(self):
        p_list = []
        for p in range(self.paragraph):
            s_list = []
            sentence_per_paragraph = random.randint(1, 20)
            for s in range(sentence_per_paragraph):
                word_per_sentence = random.randint(1, 20)
                words = random.sample(word_list, word_per_sentence)
                words.append(random.choice(punc_list[1:]))
                s = ''.join(words)
                s_list.append(s)
            p_list.append(''.join(s_list))
        
        output = '\n\n'.join(p_list)
        return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A python script for generating Chinese lorem ipsum')
    parser.add_argument('-p', dest='para', default=5, type=int, help='Number of paragraphs')
    args = parser.parse_args()

    a = LoremGenerator(args.para)
    print(a.generate())
