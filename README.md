# kor-text-preprocess
Korean text data preprocess toolkit for NLP

## Overview
This repository contains codes for Korean text preprocessing. There are several options you can use for now. Other functions will be added sooner or later.

### Options

* **`tokenize`** is about tokenizing sentences usually for morphological analysis. Classes of `mecab` and `bpe` are provided for now. 
> * `mecab` from [KoNLPy](http://konlpy.org/en/latest/) includes `morphs`, `nouns` and `pos` which are functions for your Korean text data. 
> * `bpe` is imported from [SentencePiece of Google](https://github.com/google/sentencepiece). You need to train the BPE model first, and then tokenize your data using the model. 
Each methods are selectable by options.

* **`clean_kor`** is for cleaning Korean text data like 'sejong corpus'. It will trim the unnecessary character and symbols. Of course you can customize the regular expression in `src/clean.py`

* **`template`** for text data templating for certain task. For now, `next_sentence_prediction` template is only available. It arranges two sentences in a line with seperator [SEP]. Please read the description in `src/template.py`. Other task templates will be added in the list. 

## Environmnet
Ubuntu 16.04 _(`Mecab()` class of konlpy is only provided on linux)_

## Requirement
> $ pip install -r 'requirements.txt' <br>
> $ sudo apt-get install curl <br>
> $ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)

## Usage
```
> python main.py -h
> <help messages>

ex)
> python main.py -i "input_file" -o "output_file" -e 'utf8' \
                |-opt   |"tokenize" |--mecab|--morphs   |       |
                |       |           |       |--nouns    |       |
                |       |           |       |--pos      |       |
                |       |           |--bpe  |--train    |       | 
                |       |           |       |--model    |"model"|
                |       |           |       |--vocab    |30000  |
                |       |"clean_kor"|       |           |       |
                |       |"template" |--nsp  |-ms        |0      |
                |       |           |       |-s         |". "   |
```                                                            

