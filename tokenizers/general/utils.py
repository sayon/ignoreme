__author__ = 'novokonst'

import os
import csv


def save_results(token_dict, out_dir):
    for ttype, tlist in token_dict.items():
        filename = out_dir + '\\' + ttype + '.txt'
        out_file = open(filename, 'w')
        out_file.write(str(len(tlist)) + '\n')
        out_file.write('\n'.join([tok.value for tok in tlist]))


def make_csv(file_name, dict_data):
    with open(file_name + '.csv', 'wb') as csvfile:
        csv_writer = csv.DictWriter(csvfile, dict_data.keys())
        csv_writer.writeheader()
        csv_writer.writerow(dict_data)


def list_files_in_dir(in_dir):
    return [file_path for file_path in os.listdir(in_dir) if os.path.isfile(os.path.join(in_dir, file_path))]


def nested_list_dir(in_dir):
    list_files = []
    for root, dirs, files in os.walk(in_dir):
        for ffile in files:
            list_files.append(os.path.join(root, ffile))
    return list_files


def clean_folder(folder):
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)