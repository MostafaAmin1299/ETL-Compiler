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
    'is':       'IS',
    'null':     'NULL',
    'distinct': 'DISTINCT',
    'count':    'COUNT',
    'max':      'MAX',
    'min':      'MIN',
    'sum':      'SUM',
    'avg':      'AVG',
    'having':   'HAVING',
    'order':    'ORDER',
    'asc':      'ASC',
    'desc':     'DESC',
    'limit':    'LIMIT',
    'values':   'VALUES',
    'update':   'UPDATE',
    'set':      'SET',
    'delete':   'DELETE'
}

# List of token names.   This is always required
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'PERCENT',
    'LPAREN',
    'RPAREN',
    'COLNAME',
    'DATASOURCE',
    'EQUAL',
    'NOTEQUAL',
    'BIGGER_EQUAL',
    'BIGGER',
    'SMALLER_EQUAL',
    'SMALLER',
    'SIMICOLON',
    'COMMA',
    'STRING',
    'PATTERN',
    'COLNUMBER',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_PERCENT   = r'%'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_EQUAL         = r'=='
t_NOTEQUAL      = r'<>'
t_BIGGER_EQUAL  = r'>='
t_BIGGER        = r'>'
t_SMALLER_EQUAL = r'<='
t_SMALLER       = r'<'
t_SIMICOLON = r';'
t_COMMA     = r','
t_STRING          = r'"([^"\n])*"'
t_COLNUMBER      = r'\[\d+\]'

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

@TOKEN(r'\[[^,\]\[]+\]')
def t_DATASOURCE(t):
    t.value = str(t.value[1:-1])
    return t

@TOKEN(r'\n+')
def t_newline(t):
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal entity {t.value}")
    t.lexer.skip(1)



lexer = lex.lex()

if __name__=='__main__':
    while(True):
        s = input("lex> ")
        if not s:
            break
        s = s.lower() 
        lexer.input(s)
        print('=======Tokens=======')
        while True:
            tok = lexer.token()
            if not tok:
                break
            print("\t", tok.value, "\t:\t", tok.type, sep="")
        print('====================')
