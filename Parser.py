import ply.lex as lex
import ply.yacc as yacc
from Lexer import tokens

symboltable = {}#global symboltable stores global variables and global functions takes the form of symbol = [type,token scope,value]
globalfunctions = {} # function global function symboltables 
def p_assignment(p):
    #assignment of single terms of variables eg var x = 10;
    '''expression : VAR identifier  equals  term colon
                  | VAR identifier equals str colon
                  | VAR identifier equals true colon
                  | VAR identifier equals false colon
                  | VAR identifier equals nil colon

                  '''
    p[0] = ('assignment',p[2],p[3],p[4])
    if p[4] == "nil":#checks if equals to nil
        symboltable[p[2]] = ["nil","identifier","global"]#populates the symboltable 
    
    elif p[4] == "true" or p[4] == "false":
        symboltable[p[2]] = ["bool","identifer","global"]
    
    else:
        check_type = type(eval(str(p[4])))#checks the type of p[4] and then attaches to symboltable
        symboltable[p[2]] = [check_type,"identifier","global",eval(p[4])]


def p_assignmentvariables(p):
    '''expression  : VAR identifier equals identifier plus identifier colon
                   | VAR identifier equals identifier minus identifier colon
                   | VAR identifier equals identifier times identifier colon
                   | VAR identifier equals identifier greaterthan identifier colon
                   | VAR identifier equals identifier lessthan identifier colon
                   | VAR identifier equals identifier equalequal identifier colon
                   '''
    #first check if variables are in the symbol table and are same type and restrict operations such as bool + bool is a parse error
    if p[4] in symboltable and p[6] in symboltable and symboltable[p[4]][0] == symboltable[p[6]][0]  \
     and symboltable[p[4]][0] != "bool" and symboltable[p[6]][0] != "bool"\
     and symboltable[p[4]][0] != "nil" and symboltable[p[6]][0] != "nil" and symboltable[p[4]][0] != "<type 'str'>" \
     and symboltable[p[6]][0] != "<type 'str'>":
		 #p[0] = ("expression",p[2],p[3],symboltable[p[4]][3],p[5],symboltable[p[6]][3])
		 get_symbol_p4 = symboltable[p[4]][3]
		 get_symbol_p5 =symboltable[p[4]][3]
		 get_operation = p[5]
		 if type(1) == symboltable[p[4]][0] and type(1) == symboltable[p[6]][0]:#some basic type checking 
			 #checks for ints  what operation is being performed then preforms the operation then adds to symbol table 
			 if p[5] == '+':
				 preform_operation = get_symbol_p4 + get_symbol_p5
				 #updating symbol table with new value
				 symboltable[p[2]] = [type(preform_operation),"identitier","global",preform_operation]
			 if p[5] == '-':
				 preform_operation = get_symbol_p4 - get_symbol_p5
				 symboltable[p[2]] =[type(preform_operation),"identifer","global",preform_operation]
			 if p[5] == '*':
				 prefrom_operation = get_symbol_p4 * get_symbol_p5
				 symboltable[p[2]] = [type(preform_operation) ,"identifer", "global",preform_operation]
			 if p[5] == '<':
				 preform_operation = get_symbol_p4 < get_symbol_p5
				 symboltable[p[2]] = [type(preform_operation),"identifier","global",preform_operation]
			 
				 
				 	
				 
			 
			 
			 
			 
			 
			 
    



def p_expressionidentifier(p):
    '''expression : identifier plus identifier colon
                  | identifier minus identifier colon
                  | identifier times identifier colon
                  | identifier lessthan identifier colon
                  | identifier greaterthan identifier colon
                   '''
    p[0]  = ("expression",p[1],p[2],p[3])



def p_assignmentofexpression(p):
	# assignment of expressions  var x = 1 + 1;
	
    '''expression : VAR identifier equals term plus term colon
                | VAR identifier equals term minus term colon
                | VAR identifier equals term times term colon
                | VAR identifier equals term lessthan term colon
                | VAR identifier equals term greaterthan term colon
                | VAR identifier equals term equalequal term colon
                | VAR identifier equals term lessthanequal term colon
                | VAR identifier equals term  greaterthanequal term colon
                '''
    p[0] = ("assignment",p[2],p[3],p[4],p[5],p[6])
    if type(p[4]) == type(p[6]):
	symboltable[p[2]] = [type(p[3]),"global"]
    else:
 	 p_error("error")

def p_variablechange(p):
    #rule for swapping variables x = y if y exists
    'varchange : identifier equals identifier colon'
    if p[1] in symboltable and p[3] in symboltable:
		pass 
        

    

def p_printstatement(p):
    # print statement of terms print name;
    '''expression : PRINT term colon
		  | PRINT str colon
                  | PRINT identifier colon
		  '''
    p[0] = ("printstatement",p[2])  


def p_printexpression(p):
	#print expresssion rule eg print 1+1;
    '''expression : PRINT term plus term colon
                       | PRINT term minus term colon
                       | PRINT term times term colon
                       | PRINT term lessthan term colon
                       | PRINT term greaterthan term colon
                       | PRINT term equalequal term colon
                       | PRINT term greaterthanequal term colon
                       | PRINT term lessthanequal term colon
                       | PRINT identifier plus identifier colon
                       | PRINT identifier minus identifier colon

                       '''
    p[0] = ("printexpression",p[1],p[2],p[3])

def p_functioncall(p):
    '''funccall : identifier leftfunction identifier rightfunction colon
				| identifier leftfunction identifier identifier rightfunction colon
				'''
    p[0] = ("function-call",p[2],p[4])

    
def p_functions(p):
    '''func : FUN identifier leftfunction identifier rightfunction rightclosure  RETURN identifier colon leftclosure
             | FUN identifier leftfunction identifier rightfunction rightclosure RETURN str colon leftclosure
             | FUN identifier leftfunction identifier rightfunction rightclosure RETURN term colon leftclosure'''
    #example of the above grammar fun hello(id){ return type;}
    p[0] = ("function",p[2],p[4],p[7],p[8])
    symboltable[p[2]] = p[0]

def p_functionnoreturn(p):
    '''funcexp : FUN identifier leftfunction identifier rightfunction rightclosure expression  leftclosure
               | FUN identifier leftfunction identifier rightfunction rightclosure expression expression leftclosure
               | FUN identifier leftfunction identifier rightfunction rightclosure expression expression expression leftclosure
               '''
    p[0] = ("functionexp",p[2])
    symboltable[p[2]] = p[0]




def p_variablelessthanterm(p):
    #Parser rule for  x < 10;
    'varlessthenterm : identifier lessthan term colon'
    if p[1] in symboltable:	
    	p[0] = ("varlessthanterm",p[1],p[2],p[3])

def p_variablegreaterthanterm(p):
    'vargreaterthanterm : identifier greaterthan term colon'
    p[0] = ("vargreaterthanterm",p[1],p[2],p[3])

def p_variableequalequalterm(p):
    'varequalequalterm : identifier equalequal term colon'
    p[0] = ("varequaleqaulterm",p[1],p[2],p[3])

def p_functionargs(p):
    'args : identifier identifier '
    p[0] = ('args',p[1],p[2])


def p_variableaddterm(p):
    'varaddterm : identifier plus term colon'
    p[0] = ("varaddterm" , p[1] ,p[2],p[3])

def p_variableminusterm(p):
    'varminusterm : identifier minus term colon '
    p[0] = ("varminusterm",p[1],p[2],p[3])

def p_variabletimesterm(p):
    'vartimesterm : identifier times term colon'
    p[0] = ("vartimesterm",p[1],p[2],p[3])

def p_variableaddition(p):
    #rules to for adding to integers
    'varaddvar : identifier plus identifier colon'
    if p[1] in symboltable and p[3] in symboltable:
        p[1] = symboltable[p[1]]
        p[3] = symboltable[p[3]]
        p[0] = ("varaddvar",p[1],p[2],p[3])

def p_variablesubtraction(p):
    'varsubvar : identifier minus identifier colon'
    if p[1] in symboltable and p[3] in symboltable:
        p[1] = symboltable[p[1]]
        p[3] = symboltable[p[3]]
        p[0] = ("varsubvar",p[1],p[2],p[3])

def p_variabletimesvariable(p):
    'vartimesvar : identifier times identifier colon'
    if p[1] in symboltable and p[3] in symboltable:
        p[1] =  symbolable[p[1]]
        p[3] = symboltable[p[3]]
        p[0] = ("vartimesvar",p[1],p[2],p[3])

def p_variablelessthanvariable(p):
    'varlessthanvar : identifier lessthan identifier colon'
    if p[1] in symboltable and p[3] in symboltable:
        p[1] = symboltable[p[1]]
        p[3] = symboltable[p[3]]
        p[0] = ("varlessthanvar",p[1],p[2],p[3])

def p_variablegreaterthanvariable(p):
    'vargreaterthanvar : identifier greaterthan identifier colon'
    if p[1] in symboltable and p[3] in symboltable:
        p[1] = symboltable[p[1]]
        p[3] = symboltable[p[3]]
        p[0] = ("vargreaterthanvar",p[1],p[2],p[3])

def p_variableequalqual(p):
    'varequalequalvar : identifier equalequal identifier colon'
    if p[1] in symboltable and p[3] in symboltable:
        p[1] = symboltable[p[1]]
        p[3] = symboltable[p[3]]
        p[0] = ("varequalvar",p[1],p[2],p[3])

def p_variablegreaterthanequal(p):
    'vargreaterthanequal : identifier greaterthanequal identifier colon'
    if p[1] in symboltable and p[3] in symboltable:
        p[1] = symboltable[p[1]]
        p[3] = symboltable[p[3]]
        p[0] = ("vargreaterthanequal",p[1],p[2],p[3])

def p_variablelessthanequal(p):
    'varlessthanequalvar : identifier lessthanequal identifier colon'
    if p[1] in symboltable and p[3] in symboltable:
        p[1] = symboltable[p[1]]
        p[3] = symboltable[p[3]]
        p[0] = ("varlessthanequalvar",p[1],p[2],p[3])
        
def p_vargreaterthanequalterm(p):
    'expression : identifier greaterthanequal term colon'
    p[0] = ("vargreaterequalterm",p[1],p[2],p[3])

def  p_equalequalterm(p):
    'expression : term equalequal term colon'
    p[0] = ("equalequalterm",p[0],p[1],p[2])


def p_varlessthanequalterm(p):
    'expression : identifier lessthanequal term colon'
    p[0] = ("varlessthanequalterm", p[1],p[2],p[3])



def p_greaterthanequalterm(p):
    'greaterequalterm : term greaterthanequal term colon'
    p[0] = ("greaterthanterm",p[1],p[2],p[3])



def p_fun(p):
    'fun : FUN'
    p[0] = p[1]


def p_add(p):
    #non variable addition eg 1+1;
    'add : term plus term colon'
    p[0] = ('add',p[1],p[2],p[3])

def p_substract(p):
    'sub : term minus term colon'
    p[0] = ('sub',p[1],p[2],p[3])

def p_mutiply(p):
    'mutiply : term times term colon'
    p[0] = ('mutiply',p[1],p[2],p[3])

def p_less(p):
    'less : term lessthan term colon'
    p[0] = ('less',p[1],p[2],p[3])

def p_greater(p):
    'greater : term greaterthan term colon'
    p[0] = ("greater",p[1],p[2],p[3])

def p_equalequalto(p):
    'equalcompare : term equalequal term colon'
    p[0] =("equalcompare",p[1],p[2],p[3])


def p_lessequal(p):
    'lessequal : term lessthanequal term colon'
    p[0] = ("lessequal",p[1],p[2],p[3])

def p_greaterequal(p):
    'greaterequal : greaterthanequal'
    p[0] = p[1]



def p_lessthanequal(p):
    'expression : lessthanequal'
    p[0] = p[1]

def p_greaterthanequal(p):
    'expression : greaterthanequal'
    p[0] = p[1]

def p_return(p):
    'ret : RETURN'
    p[0] = p[1]


def p_lessthan(p):
    'expression : lessthan'
    p[0] = p[1]

def p_greaterthan(p):
    'expression : greaterthan'
    p[0] = p[1]

def p_equalequal(p):
    'expression : equalequal'
    p[0] = p[1]


def p_times(p):
    'expression : times'
    p[0] = p[1]

def p_print(p):
    'print : PRINT'
    p[0] = p[1]

def p_nil(p):
    'nil : NIL'
    p[0] = p[1]

def p_true(p):
    'true : TRUE'
    p[0] = p[1]

def p_false(p):
    'false : FALSE'
    p[0] = p[1]


def p_integer(p):
    'term : integer'
    p[0] = p[1]


def p_float(p):
    'term : float'
    p[0] = p[1]

def p_leftpara(p):
    'leftfunction : leftpara'
    p[0] = p[1]

def p_rightpara(p):
    'rightfunction : rightpara'
    p[0] = p[1]

def p_leftclosure(p):
    'leftclo : leftclosure'
    p[0] = p[1]

def p_rightclosure(p):
    'rightclo : rightclosure'
    p[0] = p[1]

def p_string(p):
    'str : string'
    p[0] = p[1]

def p_minus(p):
    'expression : minus'
    p[0] = p[1]

def p_error(p):
    print("syntax error")

def p_plus(p):
    'expression : plus'
    p[0] = p[1]

def p_block(p):
    'block : rightclosure '
    p[0] = p[1] 	
	

start = 'expression'
parser = yacc.yacc(start=start)
while True:
    try:
        s = raw_input('Lox > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
    print(symboltable)


