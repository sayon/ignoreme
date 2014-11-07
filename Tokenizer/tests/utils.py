__author__ = 'novokonst'

import os
import csv


def test_lexer(lexer, test_dir_path, test_file_name):
    test_file_path = os.path.join(test_dir_path, test_file_name)
    data = open(test_file_path, 'r').read()

    lexer.build()
    token_dict = lexer.tokenize(data)
    token_dict = lexer.keywords_ex_stats()

    token_frequencies = {tok_type: len(values) for tok_type, values in token_dict.items()}

    csvfile = open(test_file_path + '.csv', 'wb')
    csvfile.write('\n'.join([k + ' ' + str(v) for k, v in token_frequencies.items()]))
    # csv_writer = csv.DictWriter(csvfile, lexer.__class__.MY_KEYWORDS)
    # csv_writer.writerow(token_frequencies)