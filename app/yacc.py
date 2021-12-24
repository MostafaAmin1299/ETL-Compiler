import ply.yacc as yacc
from lex import tokens

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
    'select : SELECT distinct select_columns FROM DATASOURCE into where order limit SIMICOLON'
    from etl import ETL

    data = ETL.extract(p[5])
    data = ETL.transform(
        data, 
        {
            "COLUMNS":  p[3],
            "DISTINCT": p[2],
            "FILTER":   p[7],
            "ORDER":    p[8],
            "LIMIT":    p[9],
        }
    )
    ETL.load(data, p[6])

    p[0] = None
    

###########################
#==== INSERT STATEMENT ====
###########################

def p_insert(p):
    'insert : INSERT INTO DATASOURCE icolumn VALUES values SIMICOLON'
    from etl import ETL

    ETL.insert_into(p[3], p[4], p[6])
    p[0] = None



###########################
#==== Update STATEMENT ====
###########################
def p_update(p):
    'update : UPDATE DATASOURCE SET assigns where SIMICOLON'
    from etl import ETL
    
    ETL.update(p[2], p[4], p[5])
    p[0] = None


###########################
#==== YET DELETE STATEMENT​​ ====
###########################

def p_delete(p):
    'delete : DELETE FROM DATASOURCE where'
    from etl import ETL

    ETL.delete(p[3], p[4])
    p[0] = None



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
           | COLNAME''' 
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
#======== COLUMNS =========
###########################
def p_column(p):
    '''column : COLNUMBER
               | COLNAME'''
    p[0] = p[1]

def p_columns(p):
    '''columns : columns COMMA columns'''
    p[0] = []
    p[0].extend(p[1])
    p[0].extend(p[3])

def p_columns_base(p):
    '''columns : column'''
    p[0] = [p[1]]


###########################
#===== SELECT COLUMNS​​ =====
###########################

def p_select_columns_all(p):
    'select_columns : TIMES'
    p[0] = '__all__'

def p_select_columns(p):
    'select_columns : columns'
    p[0] = p[1]



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
#======= Order by =========
###########################

def p_order_by(p):
    '''order : ORDER BY column way'''
    p[0] = (p[3], p[4])

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
        p[0] = p[2]

def p_limit_empty(p):
    'limit : empty'
    p[0] = None


###########################
#===== INSERT VALUES​ ======
###########################

def p_value(p):
    '''value : STRING
             | NUMBER'''
    p[0] = p[1]

def p_single_values(p):
    'single_values : LPAREN value COMMA values RPAREN'
    p[0] = []
    p[0] = p[0].append(p[1])
    p[0] = p[0].extend(p[3])

def p_values(p):
    'values : single_values COMMA values'
    p[0] = [p[1]].extend(p[3])

def p_values_end(p):
    'values : single_values'
    p[0] = [p[1]]


###########################
#===== Insert Columns​​ =====
###########################

def p_icolumn(p):
    'icolumn : LPAREN columns RPAREN'
    p[0] = p[2]


def p_icolumn_empty(p):
    'icolumn : empty'
    p[0] = None



###########################
#==== ASSIGNS STATEMENT​​ ===
###########################

def p_assign(p):
    'assign : column EQUAL value'
    p[0] = (p[1], p[3])

def p_assigns(p):
    'assigns : assign COMMA assigns'
    p[0] = [p[1]].extend(p[3])

def p_assigns_end(p):
    'assigns : assign'
    p[0] = [p[1]]




# Build the parser
parser = yacc.yacc()

if __name__=='__main__':
    while True:
        s = input('query> ')
        if not s: break
        s = s.lower()
        result = parser.parse(s)

    