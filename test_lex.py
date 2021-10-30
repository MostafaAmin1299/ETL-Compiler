import ply.lex as lex
from ply.lex import TOKEN

class MyLexer(object):
    # To handle reserved words
    reserved = {
    'select':   'SELECT',
    'from':     'FROM',
    'into':     'INTO',
    'where':    'WHERE',
    }

    # List of token names.   This is always required
    tokens = [
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
        'NAME',
        'EQUAL',
        'BIGGER_THAN_OR_EQUAL_TO',
        'BIGGER_THAN',
        'SMALLER_THAN_OR_EQUAL_TO',
        'SMALLER_THAN',
        'SIMICOLON',
    ] + list(reserved.values())

    # Regular expression rules for simple tokens
    t_PLUS      = r'\+'
    t_MINUS     = r'-'
    t_TIMES     = r'\*'
    t_DIVIDE    = r'/'
    t_LPAREN    = r'\('
    t_RPAREN    = r'\)'
    t_EQUAL                     = r'='
    t_BIGGER_THAN_OR_EQUAL_TO   = r'>='
    t_BIGGER_THAN               = r'>'
    t_SMALLER_THAN_OR_EQUAL_TO  = r'<='
    t_SMALLER_THAN              = r'<'
    t_SELECT    = r'select'
    t_FROM      = r'from'
    t_INTO      = r'into'
    t_WHERE     = r'where'
    t_SIMICOLON = r';'

    # ignored characters 
    t_ignore  = ' \t'  # Spaces and tabs
    t_ignore_COMMENT = r'/\*.*\*/' # Comment

    # To define tokens as a series of more complex regular expression rules.
    digit            = r'([0-9])'
    nondigit         = r'([_A-Za-z])'
    identifier       = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'


    @TOKEN(identifier)
    def t_NAME(self,t):
        t.type = self.reserved.get(t.value,'NAME')    # Check for reserved words
        return t

    @TOKEN(r'\d+')
    def t_NUMBER(self,t):
        t.value = int(t.value)
        return t

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Error handling rule
    def t_error(self,t):
        print(f"Illegal entity {t.value}")
        t.lexer.skip(1)

    def __init__(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def tokenize(self,data):
        self.lexer.input(data)
        print('=======Tokens=======')
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print("\t", tok.value, "\t:\t", tok.type, sep="")
        print('====================')


# Build the lexer and try it out
m = MyLexer()

while(True):
    q = input("Enter Query (q to exit): ")
    if q == 'q':
        break
    m.tokenize(q)
