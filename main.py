# -*- coding:utf-8 -*-

from src.tokenize import Tokenizer
from src.clean import Clean_kor
from src.template import Template
import argparse
import os

if __name__ == "__main__":
    opt_availables = ['tokenize', 'clean_kor', 'template']
    token_availables = ['mecab']
    method_availables = ['morphs', 'nouns', 'pos']
    task_availables = ['next_sentence_prediction']

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", \
                        required=True, type=str, help="Input file dir")
    parser.add_argument("-o", "--output", \
                        type=str, default=None, help="Output file dir")
    parser.add_argument("-opt", "--option", \
                        required=True, type=str, default=None, \
                        choices=opt_availables, help="Which option to apply.")
    parser.add_argument("--mecab", action="store_true", help="Use mecab for tokenizing")
    parser.add_argument("--morphs", action="store_true", \
                        help="Apply \'morphs\' of the tokenizer to the text")
    parser.add_argument("--nouns", action="store_true", \
                        help="Apply \'nouns\' of the tokenizer to the text")
    parser.add_argument("--pos", action="store_true", \
                        help="Apply \'pos\' of the tokenizer to the text")
    parser.add_argument("--nsp", action="store_true", help="Which task to apply.")
    parser.add_argument("-ms", "--min_seq", type=int, default=0, \
                        help="Minimum length of sequence")
    parser.add_argument("-s", "--sep", \
                        type=str, default='. ', help="Separator for spliting sentences")
    parser.add_argument("-e", "--encoding", \
                        type=str, default='utf8', help="Encoding of input file")

    args = parser.parse_args()

    os.makedirs(os.path.dirname(os.path.normpath(args.output)) or './', exist_ok=True)

    if args.option == 'tokenize':
        opt = Tokenizer(args)
        opt.apply()
    elif args.option == 'clean_kor':
        opt = Clean_kor(args)
        opt.apply()
    elif args.option == 'template':
        opt = Template(args)
        opt.apply()