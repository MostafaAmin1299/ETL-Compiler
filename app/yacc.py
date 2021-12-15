import ply.yacc as yacc
from lex import tokens
from etl import ETL


start = 'start'
def p_start(p):
    '''start : select 
             | insert 
             | update 
             | delete'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Syntax error!")



###########################
#==== Yet SELECT STATEMENT​​ 
###########################

def p_select(p):
    'select : SELECT distinct select_columns FROM DATASOURCE into where group order limit SIMICOLON'

    # etl = ETL()
    # etl.extract(p[5])
    # etl.transform({
    #     "COLUMNS":  p[3],
    #     "DISTINCT": p[2],
    #     "FILTER":   p[7],
    #     "LIMIT":    p[10]
    # })
    # etl.load(p[6])

    p[0] = f'''<SELECT STATEMENT>
    EXTRACT DATASOURCE: {p[5]}
    TRANFORMATION: 
        COLUMNS = {p[3]}
        DISTINCT? {p[2]}
        FILTER:   {p[7]}
        LIMIT:    {p[10]}
    LOAD DATASOURCE: {p[6]}

    '''
    


###########################
#==== Yet INSERT STATEMENT 
###########################

def p_insert(p):
    '''insert : INSERT INTO DATASOURCE icolumn VALUES LPAREN values RPAREN SIMICOLON
              | INSERT INTO DATASOURCE LPAREN select RPAREN SIMICOLON'''
    p[0] = f'''<INSERT STATEMENT>
    VALUES: {p[5]}
    LOAD DATASOURCE: {p[3]}

    '''



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
#====== COMPARISON =======
##########################

def p_logical(p):
    '''logical :  EQUAL 
                | NOTEQUAL 
                | BIGGER_EQUAL 
                | BIGGER 
                | SMALLER_EQUAL 
                | SMALLER'''
    p[0] = p[1]



##########################
#====== WHERE CLAUSE =====
##########################

def p_where(p):
    'where : WHERE conditions'         
    p[0] = p[2]

def p_where_empty(p):
    'where : empty'
    p[0] = None

def p_cond_parens(p):
    'conditions : LPAREN conditions RPAREN'
    p[0] = p[2]

def p_cond_3(p):
    '''conditions : conditions AND conditions 
                  | conditions OR conditions
                  | exp LIKE STRING
                  | exp logical exp'''
    p[0] = {'type': p[2], 'left': p[1], 'right': p[3]}

def p_conditions_not(p):
    'conditions : NOT conditions'
    p[0] = {p[1]: p[2]}



##########################
#========== EXP ==========
##########################

def p_exp(p):
    '''exp : STRING
           | COLNAME
           | expression''' 
    p[0] = p[1]



###########################
#======== Distinct ========
###########################

def p_distinct(p):
    '''distinct : DISTINCT'''
    p[0] = True

def p_distinct_empty(p):
    '''distinct : empty'''
    p[0] = False



###########################
#===== SELECT COLUMNS​​ =====
###########################

def p_select_columns_all(p):
    'select_columns : TIMES'
    p[0] = ['__all__']

def p_column_number(p):
    'select_columns : COLNUMBER'
    p[0] = [int(p[1][1:-1])]

def p_column_name(p):
    'select_columns : COLNAME'
    p[0] = [str(p[1])]

def p_columns(p):
    'select_columns : select_columns COMMA select_columns'
    p[0] = []
    p[0].extend(p[1])
    p[0].extend(p[3])



###########################
#========= Into ===========
###########################

def p_into(p):
    'into : INTO DATASOURCE'
    p[0] = p[2]

def p_into_empty(p):
    'into : empty'
    p[0] = None



###########################
#=======  Group by ========
###########################

def p_group(p):
    'group : GROUP BY db_column'
    p[0] = p[3]

def p_group_empty(p):
    'group : empty'
    p[0] = None

def p_db_column(p):
    '''db_column : COLNAME 
                    | COLNUMBER'''
    p[0] = p[1]



###########################
#======= Order by =========
###########################

def p_order_by(p):
    '''orders : ORDER BY orders'''
    p[0] = p[3]

def p_order(p):
    'orders : db_column way'
    p[0] = [(p[1], p[2])]

def p_orders(p):
    'orders : orders COMMA orders'
    p[0] = []
    p[0] = p[0].extend(p[1])
    p[0] = p[0].extend(p[3])

def p_order_empty(p):
    'order : empty'
    p[0] = None

def p_way_asc(p):
    '''way : ASC 
           | empty'''
    p[0] = 'ASC'

def p_way_desc(p):
    'way : DESC'
    p[0] = 'DESC'



###########################
#========= Limit ==========
###########################

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
#====== YET INSERT VALUES​ =====
###########################

def p_value(p):
    '''values : STRING
             | NUMBER'''
    p[0] = [p[1]]

def p_values(p):
    'values : values COMMA values'
    p[0] = []
    p[0] = p[0].extend(p[1])
    p[0] = p[0].extend(p[3])

def p_icolumn(p):
    '''icolumn : empty'''
    pass



###########################
#==== YET UPDATE STATEMENT​​ ====
###########################

def p_update(p):
    'update : UPDATE DATASOURCE SET assigns where SIMICOLON'
    pass

def p_assigns(p):
    '''assigns : COLNAME EQUAL
               | empty'''
    pass



###########################
#==== YET DELETE STATEMENT​​ ====
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
        s = s.lower()
        result = parser.parse(s)
        print(result)
    