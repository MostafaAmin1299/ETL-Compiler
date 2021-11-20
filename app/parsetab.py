
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BETWEEN BIGGER_THAN BIGGER_THAN_OR_EQUAL_TO BY COLNAME COMMA DATASOURCE DIVIDE EQUAL EXISTS FROM GROUP IN INSERT INTO LIKE LPAREN MINUS NOT NUMBER OR PATTERN PLUS RPAREN SELECT SIMICOLON SMALLER_THAN SMALLER_THAN_OR_EQUAL_TO STRING TIMES WHEREexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : factorfactor : NUMBERterm : term DIVIDE factorfactor : LPAREN expression RPARENselect : SELECT cols FROM DATASOURCEcols : cols COMMA COLNAMEcols : COLNAME'
    
_lr_action_items = {'NUMBER':([0,5,6,7,8,9,],[4,4,4,4,4,4,]),'LPAREN':([0,5,6,7,8,9,],[5,5,5,5,5,5,]),'$end':([1,2,3,4,11,12,13,14,15,],[0,-3,-5,-6,-1,-2,-4,-7,-8,]),'PLUS':([1,2,3,4,10,11,12,13,14,15,],[6,-3,-5,-6,6,-1,-2,-4,-7,-8,]),'MINUS':([1,2,3,4,10,11,12,13,14,15,],[7,-3,-5,-6,7,-1,-2,-4,-7,-8,]),'RPAREN':([2,3,4,10,11,12,13,14,15,],[-3,-5,-6,15,-1,-2,-4,-7,-8,]),'TIMES':([2,3,4,11,12,13,14,15,],[8,-5,-6,8,8,-4,-7,-8,]),'DIVIDE':([2,3,4,11,12,13,14,15,],[9,-5,-6,9,9,-4,-7,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,5,],[1,10,]),'term':([0,5,6,7,],[2,2,11,12,]),'factor':([0,5,6,7,8,9,],[3,3,3,3,13,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','yacc.py',7),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','yacc.py',11),
  ('expression -> term','expression',1,'p_expression_term','yacc.py',15),
  ('term -> term TIMES factor','term',3,'p_term_times','yacc.py',19),
  ('term -> factor','term',1,'p_term_factor','yacc.py',23),
  ('factor -> NUMBER','factor',1,'p_factor_num','yacc.py',27),
  ('term -> term DIVIDE factor','term',3,'p_term_div','yacc.py',31),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','yacc.py',35),
  ('select -> SELECT cols FROM DATASOURCE','select',4,'p_select_into','yacc.py',39),
  ('cols -> cols COMMA COLNAME','cols',3,'p_cols','yacc.py',45),
  ('cols -> COLNAME','cols',1,'p_cols_end','yacc.py',54),
]
