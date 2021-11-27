import ply.yacc as yacc
from lex import tokens
from etl import ETL


start = 'start'
def p_start(p):
    'start : select | insert | update | delete'
    pass

def p_error(p):
    print("Syntax error in input!", p)



##########################
#========= Maths =========
##########################

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


##########################
#==== BASIC VARIABLES ====
##########################

def p_empty(p):
    'empty :'
    p[0] = ''


def p_logical(p):
    '''logical :  EQUAL 
                | NOTEQUAL 
                | BIGGER_EQUAL 
                | BIGGER 
                | SMALLER_EQUAL 
                | SMALLER'''
    pass


def p_where(p):
    'where : WHERE cond'         
    p[0] = p[2]

def p_where_empty(p):
    'where : empty'
    p[0] = True


def p_cond_parens(p):
    'cond : LPAREN cond RPAREN'
    p[0] = p[2]

def p_cond_logical(p):
    'cond : exp logical exp'
    pass

def p_cond_between(p):
    'cond : exp BETWEEN exp AND exp'
    pass

def p_cond_in(p):
    'cond : exp IN tuple'
    pass

def p_cond_is(p):
    'cond: exp is'
    pass

def p_cond_like(p):
    'cond : exp LIKE STRING'
    pass

def p_cond_exists(p):
    'cond : EXISTS LPAREN select RPAREN'
    pass

def p_cond_and(p):
    'cond : cond AND cond'
    p[0] = p[1] and p[3]

def p_cond_or(p):
    'cond : cond OR cond'
    p[0] = p[1] or p[3]

def p_cond_not(p):
    'cond : NOT cond'
    p[0] = not p[2]

def p_exp(p):
    '''exp : STRING
           | NUMBER
           | COLNAME
           | expression''' 
    pass

def p_exps(p):
    '''exps : exp 
            | exp COMMA exps'''
    pass


def p_tuple(p):
    '''tuple : select
             | exps
             | empty'''
    pass

def p_is(p):
    '''is : IS NULL
          | IS NOT NULL'''
    pass



###########################
#==== SELECT STATEMENT​​ ====
###########################

def p_select(p):
    'select : SELECT distinct column into FROM DATASOURCE where group order limit SIMICOLON'
    from app.etl import ETL
    data_source = str(p[6][1:-1])

    etl = ETL()
    etl.extract(data_source)

    criteria = {}
    criteria['distinct'] = p[2]
    criteria['limit'] = p[10]
    etl.transform() # according to: where, distinct, group, order, limit, column


    if p[4] == None:
        print(etl.data)
    else:
        etl.load(p[4])
    




def p_distinct(p):
    '''distinct : DISTINCT'''
    p[0] = True

def p_distinct_empty(p):
    '''distinct : empty'''
    p[0] = False

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
    '''limit : LIMIT NUMBER'''
    if p[2] < 0:
        p[0] = None
    else:
        p[0] = int(p[2])

def p_limit_empty(p):
    'limit : empty'
    p[0] = None



###########################
#==== INSERT STATEMENT​​ ====
###########################

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



###########################
#==== UPDATE STATEMENT​​ ====
###########################

def p_update(p):
    'update : UPDATE DATASOURCE SET assigns where SIMICOLON'
    pass

def p_assigns(p):
    '''assigns : column EQUAL value
               | assigns COMMA assigns'''
    pass



###########################
#==== DELETE STATEMENT​​ ====
###########################

def p_delete(p):
    'delete : DELETE FROM DATASOURCE where'
    pass



# Build the parser
parser = yacc.yacc()

if __name__=='__main__':
    while True:
        s = input('yacc> ')
        if not s: break
        result = parser.parse(s)
        print(result)
    