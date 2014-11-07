__author__ = 'novokonst'

from general.dummylex import DummyLexer
from javalex.javakeylex import JavaKeyLexer
from general.keywords import C_KEYWORDS


class CKeyLexer(JavaKeyLexer):
    MY_KEYWORDS = C_KEYWORDS

    def __init__(self):
        JavaKeyLexer.__init__(self)


if __name__ == '__main__':
    import os
    import tests.utils as test_utils

    CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
    TEST_DIR_NAME = 'tests'
    TEST_DIR_PATH = os.path.join(CURRENT_DIR_PATH, TEST_DIR_NAME)
    TEST_FILE_NAME = '1.c'

    lexer = CKeyLexer()
    test_utils.test_lexer(lexer, TEST_DIR_PATH, TEST_FILE_NAME)