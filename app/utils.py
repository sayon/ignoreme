__author__ = 'mrx'


# def enum(*sequential, **named):
#     enums = dict(zip(sequential, range(len(sequential))), **named)
#     return type('Enum', (), enums)

import operator


def dict_to_list(d, order):
    if order:
        return [d.get(k) for k in order]
    else:
        return list(d.itervalues())

# neuron

def neuron_create(name, model_coeffs, features_order):
    return name, map(lambda x: float(x), utils.dict_to_list(model_coeffs, features_order))

def neuron_name(neuron): return neuron[0]
def neuron_coeffs(neuron): return neuron[1]

def neuron_compute(neuron, input):
    n_coeffs = neuron_coeffs(neuron)
    if len(n_coeffs) != len(input):
        raise Exception("file features number not equals to neuron's coefficients number")
    return reduce(operator.add, map(operator.mul, n_coeffs, input))
