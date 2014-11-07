#!/usr/bin/env python
__author__ = 'mrx'

import sys

import app.utils as ut
import app.read_configs as cfg
from lexers.utils import frequencies_kw_input as lex
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


def inputs_dict(filename, kws, model_coeffs):
    inp = lex.countKeywords(kws, filename)
    # inp = lex.countKeywordsAndSymbols(kws, filename)
    # all_features = model_coeffs.values()[0]
    # for k, v in all_features.iteritems():
    # if k not in inp:
    # inp[k] = 0
    return dict([(name, inp) for name, _ in model_coeffs.iteritems()])


KEYWORDS_PATHS = ['lexers/utils/c_keywords.txt',
                  'lexers/utils/java_keywords.txt',
                  'lexers/utils/python_keywords.txt']


def detect(filename):
    kws = cfg.read_kws(*list(map(lambda path_part: relative_path(path_part, __file__), KEYWORDS_PATHS)))
    model_coeffs = cfg.read_config()
    model_c = {}
    for k, v in model_coeffs.iteritems():
        model_c[k] = dict(filter(lambda x: x[0] in kws, v.iteritems()))
    inputs = inputs_dict(filename, kws, model_c)
    responses_dict = compute_neurons(inputs, model_coeffs, kws)
    min_response = min(responses_dict.iteritems(), key=snd)
    print(fst(min_response))
    # Capitalize language so downloader will download it correctly
    return fst(min_response).capitalize()


if __name__ == '__main__':
    gitgen.dump(list(map(detect, sys.argv[1:])))