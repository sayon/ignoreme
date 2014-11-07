__author__ = 'novokonst'

from general.dummylex import *
from general.keywords import JAVA_KEYWORDS


class JavaKeyLexer(DummyLexer):
    MY_KEYWORDS = JAVA_KEYWORDS

    def __init__(self):
        self.t_LINE_COMMENT.__func__.__doc__ = r'//.*'
        self.t_MULTI_COMMENT_LEFT.__func__.__doc__ = r'/\*.*'
        self.t_MULTI_COMMENT_RIGHT.__func__.__doc__ = r'.*\*/'
        self.t_ID.__func__.__doc__ = r'[a-zA-Z]+'
        self.t_STRING.__func__.__doc__ = r'\'.*\'|".*"'
        DummyLexer.__init__(self)

    def t_LINE_COMMENT(self, t):
        t.type = 'COMMENT'
        return t

    def t_MULTI_COMMENT_LEFT(self, t):
        self.nested_comment += 1
        t.type = 'COMMENT'
        return t

    def t_MULTI_COMMENT_RIGHT(self, t):
        self.nested_comment -= 1
        t.type = 'COMMENT'
        return t

    @check_comment
    def t_STRING(self, t):
        t.type = 'COMMENT'
        return t


if __name__ == '__main__':
    import os
    import tests.utils as test_utils

    CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
    TEST_DIR_NAME = 'tests'
    TEST_DIR_PATH = os.path.join(CURRENT_DIR_PATH, TEST_DIR_NAME)
    TEST_FILE_NAME = '1.java'

    lexer = JavaKeyLexer()
    test_utils.test_lexer(lexer, TEST_DIR_PATH, TEST_FILE_NAME)