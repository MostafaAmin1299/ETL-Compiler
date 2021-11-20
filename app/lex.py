import ply.lex as lex
from ply.lex import TOKEN

# To handle reserved words
reserved = {
    'select':   'SELECT',
    'from':     'FROM',
    'into':     'INTO',
    'where':    'WHERE',
    'like':     'LIKE',
    'group':    'GROUP',
    'by':       'BY',
    'insert':   'INSERT',
    'between':  'BETWEEN',
    'and':      'AND',
    'or':       'OR',
    'in':       'IN',
    'exists':   'EXISTS',
    'not':      'NOT', 
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
    'COLNAME',
    'DATASOURCE',
    'EQUAL',
    'BIGGER_THAN_OR_EQUAL_TO',
    'BIGGER_THAN',
    'SMALLER_THAN_OR_EQUAL_TO',
    'SMALLER_THAN',
    'SIMICOLON',
    'COMMA',
    'STRING',
    'PATTERN',
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
t_SIMICOLON = r';'
t_COMMA     = r','
t_DATASOURCE      = r'\[[^,\]\[]+\]'
t_STRING          = r'"([^"\n])*"' # Not working

# ignored characters 
t_ignore  = ' \t'  # Spaces and tabs
t_ignore_COMMENT = r'/\*.*\*/' # Comment

# To define tokens as a series of more complex regular expression rules.
digit            = r'([0-9])'
nondigit         = r'([_A-Za-z])'
identifier       = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'
identifier       = identifier + r'|' + r'\[' + digit + r'+\]' 

@TOKEN(identifier)
def t_COLNAME(t):
    t.type = reserved.get(t.value,'COLNAME')    # Check for reserved words
    return t

@TOKEN(r'\d+')
def t_NUMBER(t):
    t.value = int(t.value)
    return t

@TOKEN(r'\n+')
def t_newline(t):
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal entity {t.value}")
    t.lexer.skip(1)


def tokenize(data, lexer):
    lexer.input(data)
    print('=======Tokens=======')
    while True:
        tok = lexer.token()
        if not tok:
            break
        print("\t", tok.value, "\t:\t", tok.type, sep="")
    print('====================')


# Build the lexer and try it out
lexer = lex.lex()

if __name__=='__main__':
    while(True):
        q = input("Enter Query (q to exit): ")
        q = q.lower() 
        if q == 'q':
            break
        tokenize(q, lexer)
