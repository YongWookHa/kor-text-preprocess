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
                        required=True, type=str, help="input file dir")
    parser.add_argument("-o", "--output", \
                        type=str, default=None, help="output file dir")
    parser.add_argument("-opt", "--option", \
                        required=True, type=str, default=None, \
                        choices=opt_availables, help="which option to apply. \
                            Select in {}".format(opt_availables))
    parser.add_argument("-c", "--tokenize_class", \
                        type=str, default=None, choices=token_availables, \
                        help="which tokenize method to apply. \
                            Select in {}".format(token_availables))
    parser.add_argument("-met", "--method", \
                        choices=method_availables, type=str, default=None, \
                        help="which class method to apply. \
                            Select in {}".format(method_availables))
    parser.add_argument("-t", "--task", \
                        type=str, default=None, choices=task_availables, \
                        help="which task to apply. \
                            Select in {}".format(task_availables))
    parser.add_argument("-ms", "--min_seq", \
                        type=int, default=0, help="Minimum length of sequence")
    parser.add_argument("-s", "--sep", \
                        type=str, default='?.', help="Separator for spliting sentences")
    parser.add_argument("-e", "--encoding", \
                        type=str, default='utf8', help="encoding of input file")

    args = parser.parse_args()

    os.makedirs(os.path.dirname(os.path.normpath(args.output)), exist_ok=True)

    if args.option == 'tokenize':
        opt = Tokenizer(args.tokenize_class, args.method)
        opt.apply(os.path.normpath(args.input), os.path.normpath(args.output), \
                encoding=args.encoding)
    elif args.option == 'clean_kor':
        opt = Clean_kor()
        opt.apply(os.path.normpath(args.input), os.path.normpath(args.output), \
                encoding=args.encoding)
    elif args.option == 'template':
        opt = Template(args.task)
        opt.apply(os.path.normpath(args.input), os.path.normpath(args.output), \
                min_seq=args.min_seq, sep=args.sep, encoding=args.encoding)
