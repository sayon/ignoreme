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


MODEL_CONFIG = 'neurons.csv'


def inputs_dict(filename, kws):
    with open(filename, "r") as in_file:
        contents = in_file.read()
        return lex.keywordsAndSymbolsFrequencies(kws, contents)


def detect(filename):
    paths = map(lambda path_part: relative_path(path_part, __file__), KEYWORDS_PATHS)
    inputs = inputs_dict(filename, cfg.read_kws(paths))
    inputs.update({'intercept' : 1})
    features_order = inputs.keys()
    model_coeffs = cfg.read_config(relative_path(MODEL_CONFIG, __file__))
    responses_dict = compute_neurons(inputs, model_coeffs, features_order)
    min_response = min(responses_dict.iteritems(), key=snd)
    return fst(min_response).capitalize()


# if __name__ == '__main__':
#     langs = map(detect, sys.argv[1:])
#     print('\n'.join(langs))
#     git_gen.dump(langs)

langs = [detect('main.py')]
print('\n'.join(langs))
git_gen.dump(langs)