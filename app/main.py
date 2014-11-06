__author__ = 'mrx'

import utils as ut
import read_configs as cfg
from lexers.utils import frequencies_kw_input as lex


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
         ut.neuron_compute(n, ut.dict_to_list(inputs.get(ut.neuron_name(n)), features_order))
        )
        for n in neurons]
    return dict(raw_dict)


def main(filename):
    kws = cfg.read_kws('../lexers/utils/c_keywords.txt',
                       '../lexers/utils/java_keywords.txt',
                       '../lexers/utils/python_keywords.txt')
    inputs = lex.countKeywords(kws, filename)
    model_coeffs = cfg.read_config()
    responses_dict = compute_neurons(inputs, model_coeffs, kws)
    min_response = ("", 2)
    for k, v in responses_dict:
        if v < min_response[1]:
            min_response = (k, v)

