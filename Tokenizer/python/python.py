__author__ = 'nikita_kartashov'

from tokenize import generate_tokens
from token import *
from itertools import ifilterfalse

from utils.pyutils import fst, snd


QUOTES = ['"', "'", '"""']


def clean_tokens(readline):
    def matcher(token_tuple):
        token_type = fst(token_tuple)
        token_value = snd(token_tuple)
        should_be_discarded = not token_value or \
                              token_type == NUMBER or \
                              token_type == STRING or \
                              token_type == N_TOKENS or \
                              any(token_value.startswith(quot) and token_value.endswith(quot) for quot in QUOTES)
        return should_be_discarded

    return map(lambda t: (fst(t), snd(t)), ifilterfalse(matcher, generate_tokens(readline)))


if __name__ == '__main__':
    with open('python.py') as f:
        for line in clean_tokens(f.readline):
            print(line)
