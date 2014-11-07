__author__ = 'novokonst'

import sys
import getopt
from utils import *
from java import *
from c import *
from python import *

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


def normalize_dict(dict):
    count = 0
    for k, value in dict.items():
        count += value
    if count == 0:
        return dict
    return {k: value * 1.0 / count for k, value in dict.items()}


def tokenize(in_dir):
    make_result_dir()
    tokenizers = {
        'java': JavaTokenizer()
         , 'c': CTokenizer()
    }
    list_files = list_files_in_dir(in_dir)
    for ttype, tokenizer in tokenizers.items():
        current_results_dir = os.path.join(RESULTS_DIR, ttype)
        os.makedirs(current_results_dir)

        csvfile = open(os.path.join(current_results_dir, ttype) + '.csv', 'wb')
        csv_writer = csv.DictWriter(csvfile, tokenizer.__class__.MY_KEYWORDS)
        csv_writer.writeheader()
        for file_name in list_files:
            tokenizer.refresh()
            data = open(os.path.join(in_dir, file_name), 'r').read()
            token_dict = tokenizer.tokenize(data)
            token_dict = tokenizer.keywords_ex_stats()
            token_frequencies = {tok_type: len(values) for tok_type, values in token_dict.items()}
            token_frequencies_normalize = normalize_dict(token_frequencies)
            csv_writer.writerow(token_frequencies_normalize)
            print(os.path.join(current_results_dir, file_name))


def gen_tokenizers():
    return {
        'java': JavaTokenizer()
        , 'c': CTokenizer()
        , 'python': PythonTokenizer()
    }


def tokenize_file(in_file, need_normalize=True, languages=['java', 'c', 'python']):
    out_dict = {}
    tokenizers = gen_tokenizers()
    data = open(in_file, 'r').read()
    for lang in languages:
        tokenizer = tokenizers[lang]
        tokenizer.tokenize(data)
        keywords_dict = tokenizer.keywords_ex_stats()
        keywords_frequencies = {key: len(tlist) for key, tlist in keywords_dict.items()}
        if need_normalize:
            keywords_frequencies = normalize_dict(keywords_frequencies)
        out_dict[lang] = keywords_frequencies
    return out_dict


def serialize(lang_dict):
    make_result_dir()
    for lang, keyw_dict in lang_dict.items():
        ffile = open(os.path.join(RESULTS_DIR, lang), 'w')
        for keyword, count in keyw_dict.items():
            ffile.write(keyword + ' ' + str(count) + '\n')


def run(argv):
    try:
        opts, args = getopt.getopt(argv, 'hd:f:', ['dir=', 'files='])
    except getopt.GetoptError:
        print('tokenizer.py -d dir')
    for opt, arg in opts:
        if opt in ('-d', '--dir'):
            tokenize(os.path.join(CURRENT_DIR, arg))


if __name__ == '__main__':
    serialize(tokenize_file('sources\\test_dir\\comment.py'))
    # run(['-d', 'sources\\c'])
    # run(['-d', 'sources\\java'])
    # run(sys.argv[1:])