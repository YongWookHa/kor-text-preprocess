# kor-text-preprocess
Korean text data preprocess toolkit for NLP

## Overview
This repository contains codes for korean text preprocessing. There are several options you can use for now. Other functions will be added sooner or later.

### Options
* `clean_kor` is for cleaning korean text data like 'sejong corpus'. It will trim the unnecessary character and symbols.

* `mecab` is for morphological analysis. It provides `morphs`, `nouns`, `pos` functions for your korean text data and of course, each are selectable by additional option.
Check [KoNLPy](http://konlpy.org/en/latest/) out in detail.

* `NLP` for text data templating for certain task. For now, `next_sentence_prediction` template is only available. It arranges two sentences in a line with seperator [SEP]. Please read the description in `src/tasks.py`. Other task templates will be added in the list. 

## Environmnet
Ubuntu 16.04 _(`Mecab()` class of konlpy is only provided on linux)_

## Requirement
> $ pip install -r 'requirements.txt' <br>
> $ sudo apt-get install curl <br>
> $ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)

## Usage
```
> python main.py -i "input_file" -o "output_file" -e 'utf8' \
                |-opt   |"tokenize" |-tm    |"mecab"                    |-mec|"morphs"
                |       |           |       |                           |    |"nouns"
                |       |           |       |                           |    |"pos"
                |       |"clean_kor"|       |                           |    |
                |       |"template" |-t     |"next_sentence_prediction" |-ms |0
                |       |           |       |                           |-s  |"다."
```                                                            

