#!/usr/bin/env python
__author__ = 'mrx'

import sys

import utils.read_configs as cfg
import lexers.utils.common as lex
from gitignore_gen import gen as git_gen
from utils.pyutils import relative_path, snd, fst
from model import compute_neurons


KEYWORDS_PATHS = ['lexers/utils/c_keywords.txt',
                  'lexers/utils/java_keywords.txt',
                  'lexers/utils/python_keywords.txt']


KEYWORDS_DIR = 'lexers/utils'


MODEL_CONFIG = 'neurons.csv'


def inputs_dict(filename, kws, langs):
    with open(filename, "r") as in_file:
        contents = in_file.read()
        inp_list_raw = lex.keywordsAndSymbolsFrequencies(kws, contents)
        inp_list = {}
        for k, v in inp_list_raw.iteritems():
            inp_list[str(k)] = v
        inp_list.update({'intercept' : 1})
    inp_dict = {}
    for l in langs:
        inp_dict.update({l: inp_list})
    return inp_dict, map(lambda x: str(x), inp_list.keys())


def detect(filename):
    langs, kws = cfg.read_kws(relative_path(KEYWORDS_DIR, __file__))
    inputs, _ = inputs_dict(filename, kws, langs)
    model_coeffs = cfg.read_config(relative_path(MODEL_CONFIG, __file__))
    responses_dict = compute_neurons(inputs, model_coeffs)
    print(responses_dict)
    min_response = max(responses_dict.iteritems(), key=snd)
    return fst(min_response).capitalize()


# if __name__ == '__main__':
#     langs = map(detect, sys.argv[1:])
#     print('\n'.join(langs))
#     git_gen.dump(langs)

langs = [detect('ignoreme.py')]
print('\n'.join(langs))
git_gen.dump(langs)