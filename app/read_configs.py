__author__ = 'mrx'

import csv
from os import path
from lexers.utils.common import readList


def relative_path(path_part, relative=__file__):
    return path.join(path.join(path.dirname(relative), path_part))


# def read_config():
#     """
#     Reads neurons.csv that contains logistic regression models coefficients. neurons.csv example:
#     "","final","ArrayList"
#     "java",10.22,12.00
#     "c",0.11,0
#
#     :return: dictionary of dictionaries. Enclosing dict maps language model name (for example "java") to
#     predictors dict. Predictors dict maps predictor names to coefficients. Output example:
#     {"java" : {"final" : 10.22, "ArrayList" : 12.00 }, "c" : {"final" : 0.11, "ArrayList" : 0 }}
#     """
#     with open(relative_path('neurons.csv'), 'rb') as cfg_file:
#         csv_reader = csv.reader(cfg_file)
#         rows = [row for row in csv_reader]
#         if len(rows) < 2:
#             raise Exception("neurons.csv file contains less than 2 lines")
#         head = map(lambda x: x if x != 'doublequote' else '\"', rows[0])
#         tail = rows[1:]
#         raw_dicts = [zip(head, entry) for entry in tail]
#         return dict(map(lambda x: (x[0][1], dict(x[1:])), raw_dicts))


def read_config():
    """
    Reads neurons.csv that contains logistic regression models coefficients. neurons.csv example:
    "","final","ArrayList"
    "java",10.22,12.00
    "c",0.11,0

    :return: dictionary of dictionaries. Enclosing dict maps language model name (for example "java") to
    predictors dict. Predictors dict maps predictor names to coefficients. Output example:
    {"java" : {"final" : 10.22, "ArrayList" : 12.00 }, "c" : {"final" : 0.11, "ArrayList" : 0 }}
    """
    with open('neurons.csv', 'rb') as cfg_file:
        csv_reader = csv.reader(cfg_file)
        rows = [row for row in csv_reader]
        if len(rows) < 2:
            raise Exception("neurons.csv file contains less than 2 lines")
        head = rows[0]
        tail = rows[1:]
        raw_dicts = [zip(head, entry) for entry in tail]
        return dict(map(lambda x: (x[0][1], dict(x[1:])), raw_dicts))


def read_kws(files):
    kws_lists = map(lambda x: readList(x), files)
    return reduce(lambda x, y: x + y, kws_lists)
