# -*- coding:utf-8 -*-

from .mecab import mecab
from .clean import clean_kor
from .nlp import NLP
import argparse
import os

inp_path = os.path.normpath(inp)

class Refine():
    def __init__(self):
        pass

    def readline(self, inp_path, enc='utf8'):
        with open(inp_path, "r", encoding=enc) as f:
            line = f.readline()
            while line:
                yield line
                line = f.readline()


if __name__ == "__main__":
    opt_availables = ['Mecab', 'clean_kor', 'NLP']
    nlp_availables = ['next_sentence_prediction']

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", required=True, type=str, help="input file dir")
    parser.add_argument("-p", "--option", required=True, type=str, \
                        choice=opt_availables, help="which refine option to apply")
    parser.add_argument("-n", "--nlp_task", required=args.option=='NLP', default=None\
                        choice=nlp_availables, help="which nlp task to apply")
    parser.add_argument("-o", "--output", type=str, default=None, help="output file dir")
    parser.add_argument("-e", "--encoding", type=str, default='utf8', \
                        help="encoding of input file")

    args = parser.parse_args()

    if args.option == 'Mecab':
        pass
    

    
    


                                


