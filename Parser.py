import ply.lex as lex
import ply.yacc as yacc
from Lexer import tokens

symboltable = {}#global symboltable stores global variables and global functions takes the form of symbol = [type,token scope,value]
globalfunctions = {} # function global function symboltables
class_symboltable = {} 
def p_assignment(p):
    #assignment of single terms of variables eg var x = 10;
    '''expression : VAR identifier  equals  Int colon
                  | VAR identifier equals str colon
                  | VAR identifier equals true colon
                  | VAR identifier equals false colon
                  | VAR identifier equals nil colon
		  | VAR identifier equals Float colon

                  '''
    p[0] = ('assignment',p[2],p[3],p[4])
    if p[4] == "nil":#checks if equals to nil
        symboltable[p[2]] = ["nil","identifier","global"]#populates the symboltable 
    
    elif p[4] == "true" or p[4] == "false":
        symboltable[p[2]] = ["bool","identifer","global"]
    
    else:
        check_type = type(eval(str(p[4])))#checks the type of p[4] and then attaches to symboltable
        symboltable[p[2]] = [check_type,"identifier","global"]


def p_assignmentvariables(p):
    '''expression  : VAR identifier equals identifier plus identifier colon
                   | VAR identifier equals identifier minus identifier colon
                   | VAR identifier equals identifier times identifier colon
                   | VAR identifier equals identifier greaterthan identifier colon
                   | VAR identifier equals identifier lessthan identifier colon
                   | VAR identifier equals identifier equalequal identifier colon
                   | VAR identifier equals identifier greaterthanequal identifier colon
                   | VAR identifier equals identifier lessthanequal identifier colon
                   '''
    #first check if variables are in the symbol table and are same type and restrict operations such as bool + bool is a parse error
    operation  = p[5]
    if operation  == "+":
		symboltable[p[2]] =  [type(1),type(1.0),"global"]
    elif operation  == "-":
		symboltable[p[2]] =  [type(1),type(1.0),"global"]
    elif operation  == "*":
		symboltable[p[2]] =  [type(1),type(1.0),"global"]
    else:
		symboltable[p[2]] = [type(True),"global"]
    p[0] = ("assignment",p[2],p[3],p[4],p[5],p[6])
		
				
def p_assignmentofexpression(p):
	# assignment of expressions  var x = 1 + 1;
	
    '''expression : VAR identifier equals Int plus Int colon
                | VAR identifier equals Int minus Int colon
                | VAR identifier equals Int times Int colon
                | VAR identifier equals Int lessthan Int colon
                | VAR identifier equals Int greaterthan Int colon
                | VAR identifier equals Int equalequal Int colon
                | VAR identifier equals Int lessthanequal Int colon
                | VAR identifier equals Int  greaterthanequal Int colon
				| VAR identifier equals Float minus Float colon
                | VAR identifier equals Float times Float colon
                | VAR identifier equals Float lessthan Float colon
                | VAR identifier equals Float greaterthan Float colon
                | VAR identifier equals Float equalequal Float colon
                | VAR identifier equals Float lessthanequal Float colon
                | VAR identifier equals Float  greaterthanequal Float colon
				| VAR identifier equals Float plus Float colon
                '''
               # some type checking if they are same type eg float + float = float also int + int = int
               #check types of terms if both the same then populate symbol table
    operation = p[5]
    check_type_p4 = type(eval(str(p[4])))
    check_type_p6 = type(eval(str(p[6])))
    if check_type_p4 == type(1) and check_type_p6 == type(1):
				   if operation == '+':
					   symboltable[p[2]] = [type(1),"identifier","global"]
				   if operation == '-':
					   symboltable[p[2]] = [type(1),"identifier","global"]
				   if operation == '*':
					   symboltable[p[2]] =  [type(1),"identifier","global"]
				   if operation == '<':
					   symboltable[p[2]] =  [type(True),"identifier","global"]
				   if operation == '>':
					   symboltable[p[2]] = [type(True),"identifier","global"]
				   if operation == '>=':
					   symboltable[p[2]] = [type(True),"identifier","global"]
				   if operation == '<=':
					   symboltable[p[2]] = [type(True),"identifier","global"]
				   if operation == '==':
					   symboltable[p[2]] = [type(True),"identifier","global"]
    elif check_type_p4 == type(1.0) and check_type_p6 == type(1.0):
				   if operation == '+':
					   symboltable[p[2]] = [type(1.0),"identifier","global"]
				   if operation == '-':
					   symboltable[p[2]] = [type(1.0),"identifier","global"]
				   if operation == '*':
					   symboltable[p[2]] =  [type(1.0),"identifier","global"]
				   if operation == '<':
					   symboltable[p[2]] =  [type(True),"identifier","global"]
				   if operation == '>':
					   symboltable[p[2]] = [type(True),"identifier","global"]
				   if operation == '>=':
					   symboltable[p[2]] = [type(True),"identifier","global"]
				   if operation == '<=':
					   symboltable[p[2]] = [type(True),"identifier","global"]
				   if operation == '==':
					   symboltable[p[2]] = [type(True),"identifier","global"]
						   
    p[0] = ("assignment",p[2],p[3],p[4],p[5],p[6])
               
		
    
				   
    

def p_assignmentofvariable(p):
    #rule for swapping variables x = y if y exists
    'expression : VAR identifier equals identifier colon'
    p[0] = ("assignment",p[2],p[3],p[4])
	#update symbol table
    symboltable[p[2]] = [type(1),type(1.0),type(true),"nil","global"]
    
        

    

def p_printstatement(p):
    # print statement of terms print name;
    '''printstatement : PRINT Int colon
		  | PRINT str colon
          | PRINT identifier colon
		  | PRINT true colon
		  | PRINT false colon
		  | PRINT Float colon
		  
		  '''
    p[0] = ("printstatement",p[2])
    check_type = type(eval(str(p[2])))
    if check_type == type(1):#symbol table allocation
	symboltable[p[2]] = [type(1),"printstatement","global"]
    elif check_type == type(1.0):#symbol table of float
	symboltable[p[2]] = [type(1.0),"printstatment","global"]
    elif check_type  == type("check"):
	symboltable[p[2]] = [type("check"),"printstatement","global"]
    elif check_type == type(true): 
	symboltable[p[2]] = [type(true),"printstatement","global"]
    else:
	symboltable[p[2]] = [type(1),type(1.0),type(true),type("check"),"printstatement","global"]	    
	
	
	
	


def p_printexpression(p):
	#print expresssion rule eg print 1+1;
    '''expression : PRINT Int plus Int colon
                       | PRINT Int minus Int colon
                       | PRINT Int times Int colon
                       | PRINT Int lessthan Int colon
                       | PRINT Int greaterthan Int colon
                       | PRINT Int equalequal Int colon
                       | PRINT Int greaterthanequal Int colon
                       | PRINT Int lessthanequal Int colon
                       | PRINT identifier plus identifier colon
                       | PRINT identifier minus identifier colon
					   | PRINT Float plus Float colon
                       | PRINT Float minus Float colon
                       | PRINT Float times Float colon
                       | PRINT Float lessthan Float colon
                       | PRINT Float greaterthan Float colon
                       | PRINT Float equalequal Float colon
                       | PRINT Float greaterthanequal Float colon
                       | PRINT Float lessthanequal Float colon
                       '''
    p[0] = ("printexpression",p[1],p[2],p[3])
    check_type_p2 = type(eval(str(p[2])))
    check_type_p4 = type(eval(str(p[4])))
    operation = p[3]#gets operations
    if check_type_p4 == type(1) and check_type_p4 == type(1) and operation == '+':
		    symboltable[p[2]] = ["printstatement",type(1),"global"]
    elif check_type_p4 == type(1) and check_type_p4 == type(1) and operation == '-':
		    symboltable[p[2]] = ["printstatement",type(1),"global"]
    elif check_type_p4 == type(1) and check_type_p4 == type(1) and operation == '*':
		    symboltable[p[2]] = ["printstatement",type(1),"global"]
    elif check_type_p4 == type(1) and check_type_p4 == type(1) and operation == '<':
		    symboltable[p[2]] = ["printstatement",type(True),"global"]
    elif check_type_p4 == type(1) and check_type_p4 == type(1) and operation == '>':
		    symboltable[p[2]] = ["printstatement",type(True),"global"]
    elif check_type_p4 == type(1) and check_type_p4 == type(1) and operation == '==':
		   symboltable[p[2]] = ["printstatement",type(True),"global"]
    elif check_type_p4 == type(1) and check_type_p4 == type(1) and operation == '>=':
		    symboltable[p[2]] =  ["printstatement",type(True),"global"]
    elif check_type_p4 == type(1) and check_type_p4 == type(1) and operation == '<=':
		    symboltable[p[2]] =  ["printstatement",type(True),"global"]
    elif check_type_p4 == type(1.0) and check_type_p4 == type(1.0) and operation == '+':
		    symboltable[p[2]] =  ["printstatement",type(1.0),"global"]
    elif check_type_p4 == type(1.0) and check_type_p4 == type(1.0) and operation == '-':
		    symboltable[p[2]] =  ["printstatement",type(1.0),"global"]			
    elif check_type_p4 == type(1.0) and check_type_p4 == type(1.0) and operation == '*':
		    symboltable[p[2]] =  ["printstatement",type(1.0),"global"]
    

				
    
		    
		    
		    

def p_functioncall(p):
    '''funccall : identifier leftfunction identifier rightfunction colon
				| identifier leftfunction identifier identifier rightfunction colon
				'''
    p[0] = ("function-call",p[2],p[4])

    
def p_functions(p):
    '''func : FUN identifier leftfunction identifier rightfunction rightclosure  RETURN identifier colon leftclosure
             | FUN identifier leftfunction identifier rightfunction rightclosure RETURN str colon leftclosure
             | FUN identifier leftfunction identifier rightfunction rightclosure RETURN Int colon leftclosure'''
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





def p_fun(p):
    'fun : FUN'
    p[0] = p[1]




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
    'Int : integer'
    p[0] = p[1]


def p_float(p):
    'Float : float'
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


