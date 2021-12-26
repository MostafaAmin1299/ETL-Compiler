
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'startAND ASC AVG BETWEEN BIGGER BIGGER_EQUAL BY COLNAME COLNUMBER COMMA COUNT DATASOURCE DELETE DESC DISTINCT DIVIDE EQUAL EXISTS FROM GROUP HAVING IN INSERT INTO IS LIKE LIMIT LPAREN MAX MIN MINUS NOT NOTEQUAL NULL NUMBER OR ORDER PATTERN PERCENT PLUS RPAREN SELECT SET SIMICOLON SMALLER SMALLER_EQUAL STRING SUM TIMES UPDATE VALUES WHEREstart : select \n             | insert \n             | update \n             | deleteempty :select : SELECT distinct select_columns FROM DATASOURCE into where order limit SIMICOLONinsert : INSERT INTO DATASOURCE icolumn VALUES insert_values SIMICOLONupdate : UPDATE DATASOURCE SET assigns where SIMICOLONdelete : DELETE FROM DATASOURCE wherelogical :  EQUAL \n                | NOTEQUAL \n                | BIGGER_EQUAL \n                | BIGGER \n                | SMALLER_EQUAL \n                | SMALLERwhere : WHERE conditionswhere : emptyconditions : LPAREN conditions RPARENconditions : conditions AND conditions \n                  | conditions OR conditions\n                  | exp LIKE STRING\n                  | exp logical expconditions : NOT conditionsexp : STRING\n           | COLNAME\n           | NUMBERdistinct : DISTINCTdistinct : emptycolumn : COLNUMBER\n               | COLNAMEcolumns : columns COMMA columnscolumns : columnselect_columns : TIMESselect_columns : columnsinto : INTO DATASOURCEinto : emptyorder : ORDER BY column wayorder : emptyway : ASC \n           | emptyway : DESClimit : LIMIT NUMBERlimit : emptyvalue : STRING\n             | NUMBERvalues : values COMMA valuesvalues : valuesingle_values : LPAREN values RPARENinsert_values : insert_values COMMA insert_valuesinsert_values : single_valuesicolumn : LPAREN columns RPARENicolumn : emptyassign : column EQUAL valueassigns : assign COMMA assignsassigns : assign'
    
_lr_action_items = {'SELECT':([0,],[6,]),'INSERT':([0,],[7,]),'UPDATE':([0,],[8,]),'DELETE':([0,],[9,]),'$end':([1,2,3,4,5,24,33,35,43,46,48,49,57,73,76,80,81,82,83,84,96,],[0,-1,-2,-3,-4,-5,-9,-17,-16,-24,-25,-26,-8,-23,-7,-19,-20,-18,-21,-22,-6,]),'DISTINCT':([6,],[11,]),'TIMES':([6,10,11,12,],[-5,17,-27,-28,]),'COLNUMBER':([6,10,11,12,23,26,28,41,94,],[-5,20,-27,-28,20,20,20,20,20,]),'COLNAME':([6,10,11,12,23,26,28,34,41,44,47,62,63,66,67,68,69,70,71,72,94,],[-5,21,-27,-28,21,21,21,48,21,48,48,48,48,48,-10,-11,-12,-13,-14,-15,21,]),'INTO':([7,36,],[13,51,]),'DATASOURCE':([8,13,15,25,51,],[14,22,24,36,75,]),'FROM':([9,16,17,18,19,20,21,37,],[15,25,-33,-34,-32,-29,-30,-31,]),'SET':([14,],[23,]),'COMMA':([18,19,20,21,31,37,39,53,54,59,60,61,78,79,88,89,95,],[26,-32,-29,-30,41,26,26,77,-50,-53,-44,-45,90,-47,77,-48,90,]),'RPAREN':([19,20,21,37,39,46,48,49,60,61,64,73,78,79,80,81,82,83,84,95,],[-32,-29,-30,-31,56,-24,-25,-26,-44,-45,82,-23,89,-47,-19,-20,-18,-21,-22,-46,]),'EQUAL':([20,21,32,45,46,48,49,],[-29,-30,42,67,-24,-25,-26,]),'ASC':([20,21,98,],[-29,-30,100,]),'DESC':([20,21,98,],[-29,-30,102,]),'LIMIT':([20,21,35,36,43,46,48,49,50,52,73,74,75,80,81,82,83,84,85,87,98,99,100,101,102,],[-29,-30,-17,-5,-16,-24,-25,-26,-5,-36,-23,-5,-35,-19,-20,-18,-21,-22,92,-38,-5,-37,-39,-40,-41,]),'SIMICOLON':([20,21,30,31,35,36,40,43,46,48,49,50,52,53,54,58,59,60,61,73,74,75,80,81,82,83,84,85,87,88,89,91,93,97,98,99,100,101,102,],[-29,-30,-5,-55,-17,-5,57,-16,-24,-25,-26,-5,-36,76,-50,-54,-53,-44,-45,-23,-5,-35,-19,-20,-18,-21,-22,-5,-38,-49,-48,96,-43,-42,-5,-37,-39,-40,-41,]),'LPAREN':([22,34,38,44,47,62,63,77,],[28,44,55,44,44,44,44,55,]),'VALUES':([22,27,29,56,],[-5,38,-52,-51,]),'WHERE':([24,30,31,36,50,52,58,59,60,61,75,],[34,34,-55,-5,34,-36,-54,-53,-44,-45,-35,]),'NOT':([34,44,47,62,63,],[47,47,47,47,47,]),'STRING':([34,42,44,47,55,62,63,65,66,67,68,69,70,71,72,90,],[46,60,46,46,60,46,46,83,46,-10,-11,-12,-13,-14,-15,60,]),'NUMBER':([34,42,44,47,55,62,63,66,67,68,69,70,71,72,90,92,],[49,61,49,49,61,49,49,49,-10,-11,-12,-13,-14,-15,61,97,]),'ORDER':([35,36,43,46,48,49,50,52,73,74,75,80,81,82,83,84,],[-17,-5,-16,-24,-25,-26,-5,-36,-23,86,-35,-19,-20,-18,-21,-22,]),'AND':([43,46,48,49,64,73,80,81,82,83,84,],[62,-24,-25,-26,62,62,62,62,-18,-21,-22,]),'OR':([43,46,48,49,64,73,80,81,82,83,84,],[63,-24,-25,-26,63,63,63,63,-18,-21,-22,]),'LIKE':([45,46,48,49,],[65,-24,-25,-26,]),'NOTEQUAL':([45,46,48,49,],[68,-24,-25,-26,]),'BIGGER_EQUAL':([45,46,48,49,],[69,-24,-25,-26,]),'BIGGER':([45,46,48,49,],[70,-24,-25,-26,]),'SMALLER_EQUAL':([45,46,48,49,],[71,-24,-25,-26,]),'SMALLER':([45,46,48,49,],[72,-24,-25,-26,]),'BY':([86,],[94,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'select':([0,],[2,]),'insert':([0,],[3,]),'update':([0,],[4,]),'delete':([0,],[5,]),'distinct':([6,],[10,]),'empty':([6,22,24,30,36,50,74,85,98,],[12,29,35,35,52,35,87,93,101,]),'select_columns':([10,],[16,]),'columns':([10,26,28,],[18,37,39,]),'column':([10,23,26,28,41,94,],[19,32,19,19,32,98,]),'icolumn':([22,],[27,]),'assigns':([23,41,],[30,58,]),'assign':([23,41,],[31,31,]),'where':([24,30,50,],[33,40,74,]),'conditions':([34,44,47,62,63,],[43,64,73,80,81,]),'exp':([34,44,47,62,63,66,],[45,45,45,45,45,84,]),'into':([36,],[50,]),'insert_values':([38,77,],[53,88,]),'single_values':([38,77,],[54,54,]),'value':([42,55,90,],[59,79,79,]),'logical':([45,],[66,]),'values':([55,90,],[78,95,]),'order':([74,],[85,]),'limit':([85,],[91,]),'way':([98,],[99,]),}

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
  ('insert -> INSERT INTO DATASOURCE icolumn VALUES insert_values SIMICOLON','insert',7,'p_insert','yacc.py',69),
  ('update -> UPDATE DATASOURCE SET assigns where SIMICOLON','update',6,'p_update','yacc.py',88),
  ('delete -> DELETE FROM DATASOURCE where','delete',4,'p_delete','yacc.py',100),
  ('logical -> EQUAL','logical',1,'p_logical','yacc.py',113),
  ('logical -> NOTEQUAL','logical',1,'p_logical','yacc.py',114),
  ('logical -> BIGGER_EQUAL','logical',1,'p_logical','yacc.py',115),
  ('logical -> BIGGER','logical',1,'p_logical','yacc.py',116),
  ('logical -> SMALLER_EQUAL','logical',1,'p_logical','yacc.py',117),
  ('logical -> SMALLER','logical',1,'p_logical','yacc.py',118),
  ('where -> WHERE conditions','where',2,'p_where','yacc.py',128),
  ('where -> empty','where',1,'p_where_empty','yacc.py',132),
  ('conditions -> LPAREN conditions RPAREN','conditions',3,'p_cond_parens','yacc.py',136),
  ('conditions -> conditions AND conditions','conditions',3,'p_cond_3','yacc.py',140),
  ('conditions -> conditions OR conditions','conditions',3,'p_cond_3','yacc.py',141),
  ('conditions -> exp LIKE STRING','conditions',3,'p_cond_3','yacc.py',142),
  ('conditions -> exp logical exp','conditions',3,'p_cond_3','yacc.py',143),
  ('conditions -> NOT conditions','conditions',2,'p_conditions_not','yacc.py',147),
  ('exp -> STRING','exp',1,'p_exp','yacc.py',157),
  ('exp -> COLNAME','exp',1,'p_exp','yacc.py',158),
  ('exp -> NUMBER','exp',1,'p_exp','yacc.py',159),
  ('distinct -> DISTINCT','distinct',1,'p_distinct','yacc.py',169),
  ('distinct -> empty','distinct',1,'p_distinct_empty','yacc.py',173),
  ('column -> COLNUMBER','column',1,'p_column','yacc.py',181),
  ('column -> COLNAME','column',1,'p_column','yacc.py',182),
  ('columns -> columns COMMA columns','columns',3,'p_columns','yacc.py',186),
  ('columns -> column','columns',1,'p_columns_base','yacc.py',192),
  ('select_columns -> TIMES','select_columns',1,'p_select_columns_all','yacc.py',201),
  ('select_columns -> columns','select_columns',1,'p_select_columns','yacc.py',205),
  ('into -> INTO DATASOURCE','into',2,'p_into','yacc.py',215),
  ('into -> empty','into',1,'p_into_empty','yacc.py',219),
  ('order -> ORDER BY column way','order',4,'p_order_by','yacc.py',229),
  ('order -> empty','order',1,'p_order_empty','yacc.py',233),
  ('way -> ASC','way',1,'p_way_asc','yacc.py',237),
  ('way -> empty','way',1,'p_way_asc','yacc.py',238),
  ('way -> DESC','way',1,'p_way_desc','yacc.py',242),
  ('limit -> LIMIT NUMBER','limit',2,'p_limit','yacc.py',252),
  ('limit -> empty','limit',1,'p_limit_empty','yacc.py',259),
  ('value -> STRING','value',1,'p_value','yacc.py',268),
  ('value -> NUMBER','value',1,'p_value','yacc.py',269),
  ('values -> values COMMA values','values',3,'p_values','yacc.py',274),
  ('values -> value','values',1,'p_values_end','yacc.py',279),
  ('single_values -> LPAREN values RPAREN','single_values',3,'p_single_values','yacc.py',284),
  ('insert_values -> insert_values COMMA insert_values','insert_values',3,'p_insert_values','yacc.py',289),
  ('insert_values -> single_values','insert_values',1,'p_insert_values_end','yacc.py',294),
  ('icolumn -> LPAREN columns RPAREN','icolumn',3,'p_icolumn','yacc.py',304),
  ('icolumn -> empty','icolumn',1,'p_icolumn_empty','yacc.py',309),
  ('assign -> column EQUAL value','assign',3,'p_assign','yacc.py',319),
  ('assigns -> assign COMMA assigns','assigns',3,'p_assigns','yacc.py',323),
  ('assigns -> assign','assigns',1,'p_assigns_end','yacc.py',327),
]
