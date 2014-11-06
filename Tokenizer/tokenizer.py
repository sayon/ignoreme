__author__ = 'novokonst'

import sys
import getopt
from utils import *
from java import JavaTokenizer

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(CURRENT_DIR, 'results')

SOURCES_DIR = 'sources\\java'
JAVA_FILE_NAME = 'AbstractBiMap.java'
COMMENT_FILE_NAME = 'Comment.java'


def make_result_dir():
    global RESULTS_DIR
    n = 1
    while os.path.exists(RESULTS_DIR + '_' + str(n)):
        n += 1
    RESULTS_DIR += '_' + str(n)
    os.makedirs(RESULTS_DIR)


def tokenize(in_dir):
    make_result_dir()
    tokenizers = {
        'java': JavaTokenizer()
        # , 'c': CTokenizer()
    }
    list_files = list_files_in_dir(in_dir)
    for ttype, tokenizer in tokenizers.items():
        current_results_dir = os.path.join(RESULTS_DIR, ttype)
        os.makedirs(current_results_dir)
        for file_name in list_files:
            tokenizer.refresh()
            data = open(os.path.join(in_dir, file_name), 'r').read()
            token_dict = tokenizer.tokenize(data)
            token_frequencies = {tok_type: len(values) for tok_type, values in token_dict.items()}
            make_csv(os.path.join(current_results_dir, file_name), token_frequencies)


def run(argv):
    try:
        opts, args = getopt.getopt(argv, 'hd:f:', ['dir=', 'files='])
    except getopt.GetoptError:
        print('tokenizer.py -d dir')
    for opt, arg in opts:
        if opt in ('-d', '--dir'):
            tokenize(os.path.join(CURRENT_DIR, arg))


if __name__ == '__main__':
    # run(['-d', 'sources\\test_dir'])
    run(sys.argv[1:])