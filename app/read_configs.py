__author__ = 'mrx'

import csv


def read_config():
    """
    Reads config.csv that contains logistic regression models coefficients. config2.csv example:
    "","final","ArrayList"
    "java",10.22,12.00
    "c",0.11,0

    :return: dictionary of dictionaries. Enclosing dict maps language model name (for example "java") to
    predictors dict. Predictors dict maps predictor names to coefficients. Output example:
    {"java" : {"final" : 10.22, "ArrayList" : 12.00 }, "c" : {"final" : 0.11, "ArrayList" : 0 }}
    """
    with open('config.csv', 'rb') as cfg_file:
        csv_reader = csv.reader(cfg_file)
        rows = [row for row in csv_reader]
        if len(rows) < 2:
            raise Exception("config.csv file contains less than 2 lines")
        head = rows[0]
        tail = rows[1:]
        raw_dicts = [zip(head, entry) for entry in tail]
        return dict(map(lambda x: (x[0][1], dict(x[1:])), raw_dicts))


def read_kws(*files):
    res = []
    for file in files:
        with open(file) as kws_file:
            kws = kws_file.readlines()
            res += map(lambda x: x.strip('\n'), kws)
    return res
