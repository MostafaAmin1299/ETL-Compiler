# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex
from ply.lex import TOKEN

class MyLexer(object):

    # To handle reserved words
    reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'print' : 'PRINT',
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
    ] + list(reserved.values())

    # Regular expression rules for simple tokens
    t_PLUS    = r'\+'
    t_MINUS   = r'-'
    t_TIMES   = r'\*'
    t_DIVIDE  = r'/'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_IF = r'if'
    t_THEN = r'then'
    t_ELSE = r'else'
    t_WHILE = r'while'
    t_FOR   = r'for'
    t_PRINT = r'print'


    # A string containing ignored characters 
    t_ignore  = ' \t'  # Spaces and tabs
    t_ignore_COMMENT = r'\#.*' # Comment



    # To define tokens as a series of more complex regular expression rules.
    digit            = r'([0-9])'
    nondigit         = r'([_A-Za-z])'
    identifier       = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'



    # Check for reserved words
    @TOKEN(identifier)
    def t_NAME(self,t):
        t.type = self.reserved.get(t.value,'NAME')    # Check for reserved words
        return t



    # A regular expression rule with some action code
    def t_NUMBER(self,t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)



    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)


    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok:
                 break
             print(tok.type, tok.value, tok.lineno, tok.lexpos)




# Build the lexer and try it out
m = MyLexer()
m.build()           # Build the lexer
m.test(
    '''
    x = 2 + 4 * 7
    # hello
    print(aa)
    ''')     # Test it