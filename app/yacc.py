import ply.yacc as yacc
from lex import tokens

start = 'select'

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_select_into(p):
    'select : SELECT cols FROM DATASOURCE'
    print(f'opening {p[4]}')
    print(f'colums = {p[2]}')

def p_where(p):
    '''where : WHERE cond
            | empty'''
    pass

def p_cond(p):
    '''cond : exp op exp
            | exp BETWEEN exp AND exp
            | exp IN tuple
            | exp is
            | exp LIKE STRING
            | EXISTS LPAREN select RPAREN
            | cond AND cond
            | cond OR cond
            | NOT cond
            | LPAREN cond RPAREN'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_where_empty(p):
    'where : '
    pass 

def p_cols(p):
    'cols : cols COMMA COLNAME'
    p[0] = []
    if type(p[1]) == list:
        p[0].extend(p[1])
    else:
        p[0].append(p[1])
    p[0].append(p[3])

def p_cols_end(p):
    'cols : COLNAME'
    p[0] = [p[1]]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!", p)

parser = yacc.yacc()

while True:
    s = input('yacc> ')
    if not s: break
    result = parser.parse(s)
    print(result)
    