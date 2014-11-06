__author__ = 'nikita_kartashov'

from os import path
from collections import Counter

from utils.pyutils import fst, snd
from Tokenizer.python.python import clean_tokens

KEYWORD_PATH = 'python_keywords.txt'


def relative_path(path_part):
    return path.join(path.dirname(__file__), path_part)


def python_keywords():
    with open(KEYWORD_PATH) as keyfile:
        return set((line.strip() for line in keyfile.readlines()))


def token_frequencies(token_tuples):
    return list(Counter(map(snd, token_tuples)).most_common())


def normalize_by_number_of_occurrences(frequencies):
    total_frequencies = sum(map(snd, frequencies))
    return dict((key, frequency * 1.0 / total_frequencies) for key, frequency in frequencies)


def clean_tokens_frequencies(readline, normalize=normalize_by_number_of_occurrences):
    keywords = python_keywords()
    tokens = clean_tokens(readline)
    frequencies = filter(lambda x: fst(x) in keywords, token_frequencies(tokens))
    return normalize(frequencies)


if __name__ == '__main__':
    with open(__file__) as f:
        frequencies = clean_tokens_frequencies(f.readline)
        print(frequencies)