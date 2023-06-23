//1912958
grammar MT22;

@lexer::header {
from lexererr import *
}

// @lexer::members { def emit(self): tk = self.type if tk == self.UNCLOSE_STRING: result =
// super().emit(); raise UncloseString(result.text) elif tk == self.ILLEGAL_ESCAPE: result =
// super().emit(); raise IllegalEscape(result.text); elif tk == self.ERROR_CHAR: result =
// super().emit(); raise ErrorToken(result.text); else: return super().emit(); }

options {
	language = Python3;
}

program: decllist EOF;
decllist: decl decllist | decl;

//5

decl: var_decl | func_decl;
//5.1 Variable declarations

/* ---------- VARIABLE DECLARE ---------- */

//5.1.1 Variables
var_decl: (vardecl_normal | vardecl_symmetric) SEMI;
vardecl_normal: idlist COLON var_type;

vardecl_symmetric:
	ID vardecl_symmetric exp
	| COMMA ID vardecl_symmetric exp COMMA
	| COLON var_type BANG;
// var_decl: idlist COLON (primitive_type | AUTO) (BANG list_exp)? SEMI;
idlist: ID COMMA idlist | ID;
list_exp: exp COMMA list_exp | exp;

//5.2 Function declarations
func_decl:
	ID COLON FUNCTION func_type LB param_lists? RB (INHERIT ID)? statement_block;
param_lists: param_list COMMA param_lists | param_list;
//5.1.2 Parameters
param_list: INHERIT? OUT? idlist COLON var_type;

func_type: var_type | VOID;
var_type: primitive_type | AUTO | array_type;
// idlist: id_or_arr (CM id_or_arr)*; id_or_arr: ID | ID LSB INTLIT RSB;

/*3.4 Keyword */
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

/*3.5 Operator */
//
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
PHANTRAM: '%';
//
THAN: '!';
VAVA: '&&';
THANGTHANG: '||';
//
BANGBANG: '==';
// BANG: '=';
THANBANG: '!=';
NHOHON: '<';
NHOHONBANG: '<=';
LONHON: '>';
LONHONBANG: '>=';
//
HAICHAMHAICHAM: '::';

/*3.6 Seperators: */
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
DOT: '.';
COMMA: ',';
SEMI: ';';
COLON: ':';
LCB: '{';
RCB: '}';
BANG: '=';

/*3.7 Literals */
//integer
INTEGER_LIT: DEC {self.text = self.text.replace("_", "")};
fragment DEC: '0' | [1-9] [0-9]* ('_' [0-9]+)*;

//float
// fragment FRAC: DOT [0-9]+; fragment EXP: [eE] [+-]? [0-9]+;
fragment FRAC: DOT [0-9]+ ('_' [0-9]+)*;
fragment EXP: [eE] [+-]? [0-9]+ ('_' [0-9]+)*;

// FLOAT_LIT: DEC (DOT ([0-9]+ ('_' [0-9]+)*) ([eE] [+-]? [0-9]+ ('_' [0-9]+)*)? | ([eE] [+-]?
// [0-9]+ ('_' [0-9]+)*)) {self.text = self.text.replace("_", "") };

FLOAT_LIT:
	DEC (FRAC EXP? | EXP) {self.text = self.text.replace("_", "")};

//boolean
booleanlit: TRUE | FALSE;

//string
fragment DoubleQ: '"';
STRING_LIT:
	DoubleQ STR_CHAR* DoubleQ {
		xoaDB = str(self.text)
		self.text = xoaDB[1:-1]
	};

//5. Array

indexed_array: LCB list_exp RCB;

/*************************************************/
//4.1 Primitive types
primitive_type: INTEGER | FLOAT | BOOLEAN | STRING;

//4.2 Array type Array[<element_type>, <size>]
array_type: ARRAY LSB list_exp RSB OF primitive_type;

//4.3 Void type

//4.4 Auto type

/***************************************************************/
//5. Declaration

/***************************************************************/
//6. Expressions

//6.1
// toán hạng: hằng số, biến, biểu thức khác, dữ liệu trả về bởi hàm operands: INTEGER_LIT |
// FLOAT_LIT | BOOLEAN_LIT | STRING_LIT | ID | ID LB (list_exp |) RB // | indexed_array ;

// 6.5 Index operators
index_operators: ID LSB list_exp RSB;

//6.6 Function call
func_call: ID LB (list_exp |) RB;

//6.7
exp: exp1 HAICHAMHAICHAM exp1 | exp1;
exp1:
	exp2 (
		BANGBANG
		| THANBANG
		| NHOHON
		| NHOHONBANG
		| LONHON
		| LONHONBANG
	) exp2
	| exp2;
exp2: exp2 (VAVA | THANGTHANG) exp3 | exp3;
exp3: exp3 (ADD | SUB) exp4 | exp4;
exp4: exp4 (MUL | DIV | PHANTRAM) exp5 | exp5;
exp5: THAN exp5 | exp6;
exp6: SUB exp6 | exp7;
exp7: exp7 LSB exp RSB | exp8;
exp8: LB exp RB | operands;
operands:
	INTEGER_LIT
	| FLOAT_LIT
	| booleanlit
	| STRING_LIT
	| indexed_array
	| ID
	| index_operators
	| func_call;

// exp7: exp7 LSB exp RSB | exp8; exp8: instance_access | exp9; exp9: static_access | exp10; exp10:
// creation_object | exp11; exp11: LB exp RB | operands;

/***************    7. STATENMENT     ****************/

//1 bien vo huong, index expression statement_assignment: operands BANG exp
// SEMI;//........?...........(identifier | index_exp)

statement_assignment: lhs BANG exp SEMI;

lhs: ID | index_operators;
// assign_body: assign_lhs BANG assign_tail;

// assign_lhs: operands;

// assign_tail: assign_lhs BANG assign_tail | exp;

// index_exp: operands postfix_array_exp ; postfix_array_exp: LSB exp RSB postfix_array_exp | LSB
// exp RSB ;

//2
// statement_if: IF LB exp RB statement_block (ELSEIF LB exp RB statement_block)* (ELSE
// statement_block)?;
statement_if: if0 if1;
if0: IF LB exp RB true_false_statement;
if1: ELSE true_false_statement |;
//3
statement_for:
	FOR LB ID BANG exp COMMA exp COMMA exp RB true_false_statement;

//4
statement_while: WHILE LB exp RB true_false_statement;
true_false_statement: statement_block | instruction_line;

//5
statement_do_while: DO statement_block WHILE LB exp RB SEMI;

//6
statement_break: BREAK SEMI;

//7
statement_continue: CONTINUE SEMI;

//8
statement_return: RETURN exp? SEMI;

//9
statement_call: ID LB (list_exp |) RB SEMI;

//10
statement_block: LCB bodymethods? RCB;
bodymethods: bodymethod bodymethods | bodymethod;
bodymethod: stmt | var_decl;
stmt: instructions stmt | instructions;

instructions: instruction_line | instruction_block;

instruction_line:
	statement_if
	| statement_for
	| statement_while
	| statement_assignment
	| statement_break
	| statement_continue
	| statement_return
	| statement_call;

instruction_block:
	statement_if
	| statement_for
	| statement_while
	| statement_do_while
	| statement_block;

/***************************************************************/
/*3.3 Identifiers */
ID: [A-Za-z_] [A-Za-z_0-9]*;

/*3.1 whilespace */
WS: [ \t\b\f\r\n]+ -> skip;

fragment STR_CHAR: ~[\b\f\r\n\t'"\\] | ESCAPE_SEQUENCE | '\\"';

fragment ESCAPE_SEQUENCE: '\\' [bfrnt'\\];

/*3.2 COMMENT */
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

ERROR_CHAR: .{raise ErrorToken(self.text)};

UNCLOSE_STRING:
	DoubleQ STR_CHAR* ([\b\t\n\f\r'\\] | EOF) {
		error = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '\'', '\\']
		if error[-1] in possible:
			raise UncloseString(error[1:-1])
		else:
			raise UncloseString(error[1:])
	};

fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\';

ILLEGAL_ESCAPE:
	DoubleQ STR_CHAR* ESC_ILLEGAL {
        illegal_str = str(self.text)
        raise IllegalEscape(illegal_str[1:])
    };
