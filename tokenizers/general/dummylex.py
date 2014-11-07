__author__ = 'novokonst'

import ply.lex as lex


def check_comment(fn):
    def wrapped(self, t):
        if self.nested_comment:
            t.type = 'COMMENT'
            return t
        else:
            return fn(self, t)
    wrapped.__doc__ = fn.__doc__
    return wrapped


class DummyLexer:
    """
    Need to set MY_KEYWORDS and implement comment policy
    """
    MY_KEYWORDS = []

    t_ignore = ' \t'

    def __init__(self):
        self.__class__.RESERVED = {kw: kw for kw in self.__class__.MY_KEYWORDS}
        self.__class__.tokens = ['COMMENT'] + self.__class__.RESERVED.values() + ['ID']

        self.refresh()

    def t_error(self, t):
        t.lexer.skip(1)

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    @check_comment
    def t_ID(self, t):
        t.type = self.__class__.RESERVED.get(t.value, 'ID')
        return t

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def refresh(self):
        self.skipped = []
        self.nested_comment = 0
        self.out_token_dict = {}

    def tokenize(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok: break
            self.out_token_dict[tok.type] = self.out_token_dict.get(tok.type, [])
            self.out_token_dict[tok.type].append(tok)
        return self.out_token_dict

    def keywords_ex_stats(self, extra_type_list=[]):
        keys = self.__class__.MY_KEYWORDS + extra_type_list
        return {k: self.out_token_dict.get(k, []) for k in keys}