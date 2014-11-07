#!/usr/bin/env python
__author__ = 'mrx'

import sys

import app.utils as ut
import app.read_configs as cfg
import lexers.utils.common as lex
from gitignore_gen import gen as gitgen
from utils.pyutils import relative_path, snd, fst


def compute_neurons(inputs, models_coefficients, features_order):
    """
    Multiply inputs and model coefficients in specified order

    :param inputs: dict<string, dict<string, float>> - lexers results.
    Format:
    {lexer_name1 : {feature1 : val1, feature2 : val2, ...}, ...}.
    Example:
    {'java' : {'final' : 10, 'public' : 2}, 'c' {'final' : 0, 'public' : 1}}
    :param models_coefficients: dict<string, dict<string, float>> - format is identical to previous
    one
    :param features_order: list<string> - order in witch features will be read from
    previous two dictionaries
    :return: dict<string, float> - format:
    {model_name1 : response1, model_name2 : response2, ...}
    """
    neurons = [ut.neuron_create(k, v, features_order) for k, v in models_coefficients.iteritems()]
    raw_dict = [
        (ut.neuron_name(n),
         ut.neuron_compute(n, ut.dict_to_list(inputs.get(ut.neuron_name(n)), features_order)))
        for n in neurons]
    return dict(raw_dict)


KEYWORDS_PATHS = ['lexers/utils/c_keywords.txt',
                  'lexers/utils/java_keywords.txt',
                  'lexers/utils/python_keywords.txt']


def inputs_dict(filename, kws):
    with open(filename, "r") as in_file:
        contents = in_file.read()
        return lex.keywordsAndSymbolsFrequencies(kws, contents)


def detect(filename):
    paths = map(lambda path_part: relative_path(path_part, __file__), KEYWORDS_PATHS)
    inputs = inputs_dict(filename, cfg.read_kws(paths))
    inputs.update({'intercept' : 1})
    features_order = inputs.keys()
    model_coeffs = cfg.read_config()
    responses_dict = compute_neurons(inputs, model_coeffs, features_order)
    min_response = min(responses_dict.iteritems(), key=snd)
    return fst(min_response).capitalize()


if __name__ == '__main__':
    langs = map(detect, sys.argv[1:])
    print('\n'.join(langs))
    gitgen.dump(langs)