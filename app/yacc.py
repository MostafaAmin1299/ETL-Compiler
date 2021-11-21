import ply.yacc as yacc
from lex import tokens
from etl import ETL


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


#=====BASIC VARIABLES=====

def p_where(p):
    '''where : WHERE cond
             | empty'''
             
    p[0] = ''

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

#=====BASIC VARIABLES (CONT.)​=====

def p_exp(p):
    '''exp : STRING
           | NUMBER
           | COLNAME
           | exp aop exp''' 
    pass

def p_exps(p):
    '''exps : exp 
            | exp COMMA exps'''
    pass

def p_op(p):
    '''op : EQUAL
          | BIGGER_THAN
          | SMALLER_THAN
          | NOTEQUAL
          | BIGGER_THAN_OR_EQUAL_TO
          | SMALLER_THAN_OR_EQUAL_TO'''
    pass

def p_aop(p):
    '''aop : PLUS
           | MINUS
           | TIMES
           | DIVIDE
           | PERCENT'''
    pass

def p_tuple (p):
    '''tuple : select
             | exps
             | empty'''
    pass

def p_is(p):
    '''is : IS NULL
          | IS NOT NULL'''
    pass

def p_empty(p):
    'empty :'
    p[0] = ''

#=====SELECT STATEMENT​​=====

def p_select(p):
    'select : SELECT distinct column into FROM DATASOURCE where group order limit SIMICOLON'

    p[0] = f'{p[1]} {",".join(p[3])}{" ".join(p[4:6])} {p[6][1:-1].split(";")[1]} {" ".join(p[7:])}'

    ETL.make_query(p[6][1:-1].split(";")[0], p[0])



def p_distinct(p):
    '''distinct : DISTINCT 
                | empty'''
    p[0] = ''

def p_column(p):
    '''column : TIMES
              | COLNAME
              | aggregatefun'''
    p[0] = [p[1]]

def p_columns(p):
    '''column : column COMMA COLNAME'''
    p[0] = []
    if type(p[1]) == list:
        p[0].extend(p[1])
    else:
        p[0].append(p[1])
    p[0].append(p[3])


def p_aggregatefun(p):
    'aggregatefun : aggregatename LPAREN distinct column RPAREN'
    p[0] = ''

def p_aggregatename(p):
    '''aggregatename : COUNT
                     | MAX
                     | MIN
                     | SUM
                     | AVG'''
    pass

def p_into(p):
    '''into : INTO DATASOURCE external
    | empty'''
    p[0] = ''

def p_external(p):
    '''external : IN column
                | empty'''
    pass

def p_group(p):
    '''group : GROUP BY column having
             | empty'''
    p[0] = ''

def p_having(p):
    '''having : HAVING cond
              | empty'''
    pass

def p_order(p):
    '''order : ORDER BY orders
             | empty'''
    p[0] = ''

def p_orders(p):
    '''orders : column way
              | orders COMMA orders'''
    pass

def p_way(p):
    '''way : ASC
           | DESC
           | empty'''
    pass

def p_limit(p):
    '''limit : LIMIT NUMBER
             | empty'''
    p[0] = ''

#=====INSERT STATEMENT​​=====

def p_insert(p):
    '''insert : INSERT INTO DATASOURCE icolumn VALUES LPAREN value RPAREN SIMICOLON
              | INSERT INTO DATASOURCE icolumn select SIMICOLON'''
    pass

def p_value(p):
    '''value : STRING
             | NUMBER
             | value COMMA value'''
    pass

def p_icolumn(p):
    '''icolumn : LPAREN COLNAME RPAREN
               | empty'''
    pass

#=====UPDATE STATEMENT​​=====

def p_update(p):
    'update : UPDATE DATASOURCE SET assigns where SIMICOLON'
    pass

def p_assigns(p):
    '''assigns : column EQUAL value
               | assigns COMMA assigns'''
    pass

#=====DELETE STATEMENT​​=====


def p_delete(p):
    'delete : DELETE FROM DATASOURCE where'
    pass


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!", p)




# Build the parser
parser = yacc.yacc()

while True:
    s = input('yacc> ')
    if not s: break
    result = parser.parse(s)
    print(result)
    