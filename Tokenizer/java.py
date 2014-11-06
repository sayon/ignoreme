__author__ = 'admin'

import ply.lex as lex


JAVA_KEYWORDS = [
    'abstract'
    , 'assert'
    , 'boolean'
    , 'break'
    , 'byte'
    , 'case'
    , 'catch'
    , 'char'
    , 'class'
    , 'const'
    , 'continue'
    , 'default'
    , 'do'
    , 'double'
    , 'else'
    , 'enum'
    , 'extends'
    , 'final'
    , 'finally'
    , 'float'
    , 'for'
    , 'goto'
    , 'if'
    , 'implements'
    , 'import'
    , 'instanceof'
    , 'int'
    , 'interface'
    , 'long'
    , 'native'
    , 'new'
    , 'package'
    , 'private'
    , 'protected'
    , 'public'
    , 'return'
    , 'short'
    , 'static'
    , 'strictfp'
    , 'super'
    , 'switch'
    , 'synchronized'
    , 'this'
    , 'throw'
    , 'throws'
    , 'transient'
    , 'try'
    , 'void'
    , 'volatile'
    , 'while'
]


class JavaTokenizer:

    RESERVED = {kw: kw for kw in JAVA_KEYWORDS}

    tokens = RESERVED.values() + [
        'ID'
        , 'STRING_LITERAL'
        , 'NUMBER'
        , 'COMMENT'
        , 'LINE_COMMENT'
        , 'MULTI_COMMENT_LEFT'
        , 'MULTI_COMMENT_RIGHT'
    ]

    def check_comment(fn):
        def wrapped(self, t):
            if self.nested_comment:
                t.type = 'COMMENT'
                return t
            else:
                return fn(self, t)
        wrapped.__doc__ = fn.__doc__
        return wrapped

    @check_comment
    def t_ID(self, t):
        t.type = JavaTokenizer.RESERVED.get(t.value, 'ID')
        return t

    # @check_comment
    def t_STRING_LITERAL(self, t):
        return t

    @check_comment
    def t_NUMBER(self, t):
        return t

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

    t_ignore = ' \t'

    def t_error(self, t):
        # self.skipped.append(t.value)
        t.lexer.skip(1)

    def __init__(self, **kwargs):
        self.t_ID.__func__.__doc__ = r'[@a-zA-z_][a-zA-Z0-9]*'
        self.t_STRING_LITERAL.__func__.__doc__ = r'\'.*\''
        self.t_NUMBER.__func__.__doc__ = r'\d+'
        self.t_LINE_COMMENT.__func__.__doc__ = r'//.*'
        self.t_MULTI_COMMENT_LEFT.__func__.__doc__ = r'/\*.*'
        self.t_MULTI_COMMENT_RIGHT.__func__.__doc__ = r'.*\*/'

        self.skipped = []
        self.nested_comment = 0
        self.lexer = lex.lex(module=self, **kwargs)

    def refresh(self):
        self.skipped = []
        self.nested_comment = 0

    def tokenize(self, data):
        self.lexer.input(data)
        out_token_dict = {}
        while True:
            tok = self.lexer.token()
            if not tok: break
            out_token_dict[tok.type] = out_token_dict.get(tok.type, [])
            out_token_dict[tok.type].append(tok)
        return out_token_dict