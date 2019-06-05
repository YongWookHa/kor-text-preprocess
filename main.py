# -*- coding:utf-8 -*-

from src.mecab import mecab
from src.clean import clean_kor
from src.nlp import NLP
import argparse
import os

if __name__ == "__main__":
    opt_availables = ['mecab', 'clean_kor', 'nlp']
    mecab_availables = ['morphs', 'nouns', 'pos']
    nlp_availables = ['next_sentence_prediction']

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", \
                        required=True, type=str, help="input file dir")
    parser.add_argument("-o", "--output", \
                        type=str, default=None, help="output file dir")
    parser.add_argument("-opt", "--option", \
                        required=True, type=str, default=None, \
                        choices=opt_availables, help="which refine option to apply")
    parser.add_argument("-m", "--mecab_method", \
                        choices=mecab_availables, type=str, default=None, \
                        help="which mecab method to apply")
    parser.add_argument("-n", "--nlp_task", \
                        type=str, default=None, choices=nlp_availables, \
                        help="which nlp task to apply")
    parser.add_argument("-ms", "--min_seq", \
                        type=int, default=0, help="Minimum length of sequence")
    parser.add_argument("-s", "--sep", \
                        type=str, default='다.', help="which nlp task to apply")
    parser.add_argument("-e", "--encoding", \
                        type=str, default='utf8', help="encoding of input file")

    args = parser.parse_args()

    if args.option == 'mecab':
        m = mecab(args.mecab_method, mecab_availables)
        m.apply(os.path.normpath(args.input), os.path.normpath(args.output), \
                 encoding=args.encoding)
    elif args.option == 'clean_kor':
        c = clean_kor()
        c.apply(os.path.normpath(args.input), os.path.normpath(args.output), \
                encoding=args.encoding)
    elif args.option == 'nlp':
        n = NLP(args.nlp_task, nlp_availables)
        n.apply(os.path.normpath(args.input), os.path.normpath(args.output), \
                min_seq=args.min_seq, sep=args.sep, encoding=args.encoding)

