__author__ = 'novokonst'

from general.keywords import PYTHON_KEYWORDS
from general.dummylex import *


class PythonKeyLexer(DummyLexer):
    MY_KEYWORDS = PYTHON_KEYWORDS

    def __init__(self):
        self.t_LINE_COMMENT.__func__.__doc__ = r'\#.*'
        self.t_STRING.__func__.__doc__ = r'\'.*\'|".*"'
        self.t_ID.__func__.__doc__ = r'[a-zA-Z]+'
        DummyLexer.__init__(self)

    def t_LINE_COMMENT(self, t):
        t.type = 'COMMENT'
        return t

    @check_comment
    def t_STRING(self, t):
        t.type = 'COMMENT'
        return t

    @check_comment
    def t_ID(self, t):
        t.type = self.__class__.RESERVED.get(t.value, 'ID')
        return t

if __name__ == '__main__':
    import os
    import tests.utils as test_utils

    CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
    TEST_DIR_NAME = 'tests'
    TEST_DIR_PATH = os.path.join(CURRENT_DIR_PATH, TEST_DIR_NAME)
    TEST_FILE_NAME = '1.py'

    lexer = PythonKeyLexer()
    test_utils.test_lexer(lexer, TEST_DIR_PATH, TEST_FILE_NAME)