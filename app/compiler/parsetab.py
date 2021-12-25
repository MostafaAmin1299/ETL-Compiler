
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'startAND ASC AVG BETWEEN BIGGER BIGGER_EQUAL BY COLNAME COLNUMBER COMMA COUNT DATASOURCE DELETE DESC DISTINCT DIVIDE EQUAL EXISTS FROM GROUP HAVING IN INSERT INTO IS LIKE LIMIT LPAREN MAX MIN MINUS NOT NOTEQUAL NULL NUMBER OR ORDER PATTERN PERCENT PLUS RPAREN SELECT SET SIMICOLON SMALLER SMALLER_EQUAL STRING SUM TIMES UPDATE VALUES WHEREstart : select \n             | insert \n             | update \n             | deleteempty :select : SELECT distinct select_columns FROM DATASOURCE into where order limit SIMICOLONinsert : INSERT INTO DATASOURCE icolumn VALUES insert_values SIMICOLONupdate : UPDATE DATASOURCE SET assigns where SIMICOLONdelete : DELETE FROM DATASOURCE wherelogical :  EQUAL \n                | NOTEQUAL \n                | BIGGER_EQUAL \n                | BIGGER \n                | SMALLER_EQUAL \n                | SMALLERwhere : WHERE conditionswhere : emptyconditions : LPAREN conditions RPARENconditions : conditions AND conditions \n                  | conditions OR conditions\n                  | exp LIKE STRING\n                  | exp logical expconditions : NOT conditionsexp : STRING\n           | COLNAMEdistinct : DISTINCTdistinct : emptycolumn : COLNUMBER\n               | COLNAMEcolumns : columns COMMA columnscolumns : columnselect_columns : TIMESselect_columns : columnsinto : INTO DATASOURCEinto : emptyorder : ORDER BY column wayorder : emptyway : ASC \n           | emptyway : DESClimit : LIMIT NUMBERlimit : emptyvalue : STRING\n             | NUMBERvalues : value COMMA valuesvalues : valuesingle_values : LPAREN values RPARENinsert_values : single_values COMMA insert_valuesinsert_values : single_valuesicolumn : LPAREN columns RPARENicolumn : emptyassign : column EQUAL valueassigns : assign COMMA assignsassigns : assign'
    
_lr_action_items = {'SELECT':([0,],[6,]),'INSERT':([0,],[7,]),'UPDATE':([0,],[8,]),'DELETE':([0,],[9,]),'$end':([1,2,3,4,5,24,33,35,43,46,48,56,72,75,79,80,81,82,83,95,],[0,-1,-2,-3,-4,-5,-9,-17,-16,-24,-25,-8,-23,-7,-19,-20,-18,-21,-22,-6,]),'DISTINCT':([6,],[11,]),'TIMES':([6,10,11,12,],[-5,17,-26,-27,]),'COLNUMBER':([6,10,11,12,23,26,28,41,93,],[-5,20,-26,-27,20,20,20,20,20,]),'COLNAME':([6,10,11,12,23,26,28,34,41,44,47,61,62,65,66,67,68,69,70,71,93,],[-5,21,-26,-27,21,21,21,48,21,48,48,48,48,48,-10,-11,-12,-13,-14,-15,21,]),'INTO':([7,36,],[13,50,]),'DATASOURCE':([8,13,15,25,50,],[14,22,24,36,74,]),'FROM':([9,16,17,18,19,20,21,37,],[15,25,-32,-33,-31,-28,-29,-30,]),'SET':([14,],[23,]),'COMMA':([18,19,20,21,31,37,39,53,58,59,60,78,88,],[26,-31,-28,-29,41,26,26,76,-52,-43,-44,89,-47,]),'RPAREN':([19,20,21,37,39,46,48,59,60,63,72,77,78,79,80,81,82,83,94,],[-31,-28,-29,-30,55,-24,-25,-43,-44,81,-23,88,-46,-19,-20,-18,-21,-22,-45,]),'EQUAL':([20,21,32,45,46,48,],[-28,-29,42,66,-24,-25,]),'ASC':([20,21,97,],[-28,-29,99,]),'DESC':([20,21,97,],[-28,-29,101,]),'LIMIT':([20,21,35,36,43,46,48,49,51,72,73,74,79,80,81,82,83,84,86,97,98,99,100,101,],[-28,-29,-17,-5,-16,-24,-25,-5,-35,-23,-5,-34,-19,-20,-18,-21,-22,91,-37,-5,-36,-38,-39,-40,]),'SIMICOLON':([20,21,30,31,35,36,40,43,46,48,49,51,52,53,57,58,59,60,72,73,74,79,80,81,82,83,84,86,87,88,90,92,96,97,98,99,100,101,],[-28,-29,-5,-54,-17,-5,56,-16,-24,-25,-5,-35,75,-49,-53,-52,-43,-44,-23,-5,-34,-19,-20,-18,-21,-22,-5,-37,-48,-47,95,-42,-41,-5,-36,-38,-39,-40,]),'LPAREN':([22,34,38,44,47,61,62,76,],[28,44,54,44,44,44,44,54,]),'VALUES':([22,27,29,55,],[-5,38,-51,-50,]),'WHERE':([24,30,31,36,49,51,57,58,59,60,74,],[34,34,-54,-5,34,-35,-53,-52,-43,-44,-34,]),'NOT':([34,44,47,61,62,],[47,47,47,47,47,]),'STRING':([34,42,44,47,54,61,62,64,65,66,67,68,69,70,71,89,],[46,59,46,46,59,46,46,82,46,-10,-11,-12,-13,-14,-15,59,]),'ORDER':([35,36,43,46,48,49,51,72,73,74,79,80,81,82,83,],[-17,-5,-16,-24,-25,-5,-35,-23,85,-34,-19,-20,-18,-21,-22,]),'NUMBER':([42,54,89,91,],[60,60,60,96,]),'AND':([43,46,48,63,72,79,80,81,82,83,],[61,-24,-25,61,61,61,61,-18,-21,-22,]),'OR':([43,46,48,63,72,79,80,81,82,83,],[62,-24,-25,62,62,62,62,-18,-21,-22,]),'LIKE':([45,46,48,],[64,-24,-25,]),'NOTEQUAL':([45,46,48,],[67,-24,-25,]),'BIGGER_EQUAL':([45,46,48,],[68,-24,-25,]),'BIGGER':([45,46,48,],[69,-24,-25,]),'SMALLER_EQUAL':([45,46,48,],[70,-24,-25,]),'SMALLER':([45,46,48,],[71,-24,-25,]),'BY':([85,],[93,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'select':([0,],[2,]),'insert':([0,],[3,]),'update':([0,],[4,]),'delete':([0,],[5,]),'distinct':([6,],[10,]),'empty':([6,22,24,30,36,49,73,84,97,],[12,29,35,35,51,35,86,92,100,]),'select_columns':([10,],[16,]),'columns':([10,26,28,],[18,37,39,]),'column':([10,23,26,28,41,93,],[19,32,19,19,32,97,]),'icolumn':([22,],[27,]),'assigns':([23,41,],[30,57,]),'assign':([23,41,],[31,31,]),'where':([24,30,49,],[33,40,73,]),'conditions':([34,44,47,61,62,],[43,63,72,79,80,]),'exp':([34,44,47,61,62,65,],[45,45,45,45,45,83,]),'into':([36,],[49,]),'insert_values':([38,76,],[52,87,]),'single_values':([38,76,],[53,53,]),'value':([42,54,89,],[58,78,78,]),'logical':([45,],[65,]),'values':([54,89,],[77,94,]),'order':([73,],[84,]),'limit':([84,],[90,]),'way':([97,],[98,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> select','start',1,'p_start','yacc.py',4),
  ('start -> insert','start',1,'p_start','yacc.py',5),
  ('start -> update','start',1,'p_start','yacc.py',6),
  ('start -> delete','start',1,'p_start','yacc.py',7),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',11),
  ('select -> SELECT distinct select_columns FROM DATASOURCE into where order limit SIMICOLON','select',10,'p_select','yacc.py',24),
  ('insert -> INSERT INTO DATASOURCE icolumn VALUES insert_values SIMICOLON','insert',7,'p_insert','yacc.py',48),
  ('update -> UPDATE DATASOURCE SET assigns where SIMICOLON','update',6,'p_update','yacc.py',60),
  ('delete -> DELETE FROM DATASOURCE where','delete',4,'p_delete','yacc.py',72),
  ('logical -> EQUAL','logical',1,'p_logical','yacc.py',85),
  ('logical -> NOTEQUAL','logical',1,'p_logical','yacc.py',86),
  ('logical -> BIGGER_EQUAL','logical',1,'p_logical','yacc.py',87),
  ('logical -> BIGGER','logical',1,'p_logical','yacc.py',88),
  ('logical -> SMALLER_EQUAL','logical',1,'p_logical','yacc.py',89),
  ('logical -> SMALLER','logical',1,'p_logical','yacc.py',90),
  ('where -> WHERE conditions','where',2,'p_where','yacc.py',100),
  ('where -> empty','where',1,'p_where_empty','yacc.py',104),
  ('conditions -> LPAREN conditions RPAREN','conditions',3,'p_cond_parens','yacc.py',108),
  ('conditions -> conditions AND conditions','conditions',3,'p_cond_3','yacc.py',112),
  ('conditions -> conditions OR conditions','conditions',3,'p_cond_3','yacc.py',113),
  ('conditions -> exp LIKE STRING','conditions',3,'p_cond_3','yacc.py',114),
  ('conditions -> exp logical exp','conditions',3,'p_cond_3','yacc.py',115),
  ('conditions -> NOT conditions','conditions',2,'p_conditions_not','yacc.py',119),
  ('exp -> STRING','exp',1,'p_exp','yacc.py',129),
  ('exp -> COLNAME','exp',1,'p_exp','yacc.py',130),
  ('distinct -> DISTINCT','distinct',1,'p_distinct','yacc.py',140),
  ('distinct -> empty','distinct',1,'p_distinct_empty','yacc.py',144),
  ('column -> COLNUMBER','column',1,'p_column','yacc.py',152),
  ('column -> COLNAME','column',1,'p_column','yacc.py',153),
  ('columns -> columns COMMA columns','columns',3,'p_columns','yacc.py',157),
  ('columns -> column','columns',1,'p_columns_base','yacc.py',163),
  ('select_columns -> TIMES','select_columns',1,'p_select_columns_all','yacc.py',172),
  ('select_columns -> columns','select_columns',1,'p_select_columns','yacc.py',176),
  ('into -> INTO DATASOURCE','into',2,'p_into','yacc.py',186),
  ('into -> empty','into',1,'p_into_empty','yacc.py',190),
  ('order -> ORDER BY column way','order',4,'p_order_by','yacc.py',200),
  ('order -> empty','order',1,'p_order_empty','yacc.py',204),
  ('way -> ASC','way',1,'p_way_asc','yacc.py',208),
  ('way -> empty','way',1,'p_way_asc','yacc.py',209),
  ('way -> DESC','way',1,'p_way_desc','yacc.py',213),
  ('limit -> LIMIT NUMBER','limit',2,'p_limit','yacc.py',223),
  ('limit -> empty','limit',1,'p_limit_empty','yacc.py',230),
  ('value -> STRING','value',1,'p_value','yacc.py',239),
  ('value -> NUMBER','value',1,'p_value','yacc.py',240),
  ('values -> value COMMA values','values',3,'p_values','yacc.py',244),
  ('values -> value','values',1,'p_values_end','yacc.py',248),
  ('single_values -> LPAREN values RPAREN','single_values',3,'p_single_values','yacc.py',252),
  ('insert_values -> single_values COMMA insert_values','insert_values',3,'p_insert_values','yacc.py',258),
  ('insert_values -> single_values','insert_values',1,'p_insert_values_end','yacc.py',262),
  ('icolumn -> LPAREN columns RPAREN','icolumn',3,'p_icolumn','yacc.py',271),
  ('icolumn -> empty','icolumn',1,'p_icolumn_empty','yacc.py',276),
  ('assign -> column EQUAL value','assign',3,'p_assign','yacc.py',286),
  ('assigns -> assign COMMA assigns','assigns',3,'p_assigns','yacc.py',290),
  ('assigns -> assign','assigns',1,'p_assigns_end','yacc.py',294),
]
