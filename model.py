__author__ = 'mrx'

import utils.pyutils as ut
import operator


#neuron interface


def neuron_create(name, model_coeffs, features_order):
    return name, map(lambda x: float(x), ut.dict_to_list(model_coeffs, features_order))


def neuron_name(neuron):
    return neuron[0]


def neuron_coeffs(neuron):
    return neuron[1]


def neuron_compute(neuron, input):
    n_coeffs = neuron_coeffs(neuron)
    if len(n_coeffs) != len(input):
        raise Exception("file features number not equals to neuron's coefficients number")
    return reduce(operator.add, map(operator.mul, n_coeffs, input))


#compute


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
    neurons = [neuron_create(k, v, features_order) for k, v in models_coefficients.iteritems()]
    raw_dict = [
        (neuron_name(n),
         neuron_compute(n, ut.dict_to_list(inputs.get(neuron_name(n)), features_order)))
        for n in neurons]
    return dict(raw_dict)
