# -*- coding: utf-8 -*-

import math
import random

punc_list = [u'，', u'。', u'！', u'？']
all_words = open('word.txt').read()
word_list = all_words.decode('utf-8').split('\n')[:-1]


class LoremGenerator(object):
    def __init__(self, paragraph=random.randint(1, 5)):
        self.paragraph = paragraph

    def generate(self):
        p_list = []
        for p in range(self.paragraph):
            s_list = []
            sentence_per_paragraph = random.randint(1, 20)
            for s in range(sentence_per_paragraph):
                word_per_sentence = random.randint(1, 20)
                words = random.sample(word_list, word_per_sentence)
                words.append(random.choice(punc_list))
                s = ''.join(words)
                s_list.append(s)
            p_list.append(''.join(s_list))
        
        output = '\n\n'.join(p_list)
        return output


if __name__ == '__main__':
    a = LoremGenerator()
    print(a.generate())
