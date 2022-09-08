import pytest
import sys
sys.path.insert(0,'..')
from Scanner import Lexer as Lex

class LexerTests(object):

    def __str__(self):
        return "test class for lexer"

	def __init__(self):
		self.lexer = Scanner.Lex()
		self.lexer.build()
                self.variable = '''LexToken(VAR,'var',1,0)'''

	
    def integerassignmenttest(self):
        #interger assignment test
        assignmentinteger = '''var x  = 10''';
        variable = '''LexToken(VAR,'var',1,0)'''
        integer = '''LexToken(integer,'10',1,9)'''
        assignmentarray = [self.lexer.test_function(assignmentinteger)]
        if integer and variable in assignmentarray:
            return True
        else:
            return False


    
    def floatassignmenttest(self):
        #float assignment test
        assignmentfloat = "var y = 100.0;"
        Float = '''LexToken(float,'100.0',1,9)'''
        assignmentarray  = [self.lexer.test_function(assignmentfloat)]
        if self.variable in assignmentarray and Float in assignmentarray:
            return True
        else:
            False


    def stringassignmenttest(self):
        #string assignment test
        assignmentstring = '''var x = "hello";'''
        string = '''LexToken(string,'hello;',1,9)'''
        assignmentarray = [self.lexer.test_function(assignmentstring)]
        if string in assignmentarray and self.variable in assignmentarray:
            return True
        else:
            return False


    def nilassignmenttest(self):
        #assignment of nill test
        assignmentnil = '''var x  = nil;'''
        nil  = '''LexToken(nil,'NIL',1,9)'''
        assignmentarray = [self.lexer.test_function(assignmentnil)]
        if nil in assignmentarray and self.variable in assignmentarray:
            return True
        else:
            return False
        


    def addingtwovariablestest(self):
        #adding two variables together tests
        addingtwovariables = ''' var x =  10;
                             var y = 200;
                             x + y;'''
        plus = '''LexToken(plus,'+',1,27)'''
        assignmentarray = [self.lexer.test_function(addingtwovariables)]
        if plus in assignmentarray and self.variable in assignmentarray:
            return True
        else:
            return False

    def substractingtwovariablestest(self):
        #substracting two varables
        substractingtwovariables = ''' var x = 10; var y = 10; x-y;'''
        subtraction = '''LexToken(minus,'-',1,26)'''
        assignmentarray = [self.lexer.test_function(substractiontwovariables)]
        if subtraction in assignmentarray and self.variable in assignmentarray:
            return True
        else:
            return False

    
    def mutiplyingtwovariablestest(self):
        # mutiply two variables together
        mutiplytwovariables = '''var x = 20; var y = 20; x * y;'''
        times = '''LexToken(times,'*',1,26)'''
        assignmentarray = [self.lexer.test_function(mutiplytwovariables)]
        if times in assignmentarray and self.variable in assignmentarray:
            return True
        else:
            return False


    def lessthanintegertest(self):
        #less than integer value
        lessthaninteger = ''' var x =  100; x<200;'''
        lessthan = '''LexToken(lessthan,'<',1,14)'''
        assignmentarray = [self.lexer.test_function(lessthaninteger)]
        if lessthan in assignmentarray and self.variable in assignmentarray:
            return True
        else:
            return False

    def lessthanequalintegertest(self):
        #less than equal integer
        lessthanequalinteger = ''' var x = 200; x<=200;'''
        lessthanequal = '''LexToken(lessthanequal,'<=',1,14)'''
        assignmentarray = [self.lexer.test_function(lessthanequalinteger)]
        if self.variable in assignmentarray and lessthanequal in assignmentarray:
            return True
        else:
            return False




    def lessthanfloattest(self):
        #less than float test
        lessthanfloat =  '''var x = 100.0; x<200.0;'''
        lessthanequal = '''LexToken(lessthanequal,'<=',1,14)'''
        assignmentarray = [self.lexer.test_function(lessthanequal)]
        if self.variable in assignmentarray  and lessthanequal in assignmentarray:
            return True
        else:
            return False



    def lessthanequalfloattest(self):
        #lessthan floating point lexer rules
        lessthanequalfloat = '''var x = 100.0 x<=200.0'''
        lessthanequal = '''LexToken(lessthanequal,'<=',1,14)'''
        assignmentarray = [self.lexer.test_function(lessthanequal)]
        if self.variable in assignmentarray and lessthanequal in assignmentarray:
            return True
        else:
            return False


    def greaterthanintegertest(self):
        #greaterthaninteger test
        greaterthaninteger = '''var x = 200; x>100;'''
        greaterthan = '''LexToken(greaterthan,'>',1.14)'''
        assignmentarray = [self.lexer.test_function(greaterthaninteger)]
        if self.variable in assignmentarray and greaterthan in assignmentarray:
            return True
        else:
            return False
    
    def greaterthanfloattest(self):
        #greaterthanfloat test
        greaterthanfloat = '''var x = 100.0; x>200.0;'''
        greaterthan = '''LexToken(greaterthan,'>',1.14)'''
        assignmentarray = [self.lexer.test_function(greaterthanfloat)]
        if self.variable in assignmentarray and greaterthan in assignmentarray:
            return True
        else:
            return False



    def greaterthanequalintegertest(self):
        #greater than equal integer
        greatherthanequalinteger = '''var x  = 200; x>=200;'''
        greaterthan = '''LexToken(greaterthan,'>',1.14)'''
        assignmentarray = [self.lexer.test_function(greaterthaninteger)]
        if self.variable in assignmentarray and greaterthan in assignmentarray:
            return True
        else:
            return False


    def greaterthanequalfloattest(self):
        #greater than equal float test
        greatherthaneqaulfloat = '''var x = 200.0; x>=200.0;'''
        greaterthan = '''LexToken(greaterthanequal,'>=',1.14)'''
        assignmentarray = [self.lexer.test_function(greaterthanequalfloat)]
        if self.variable in assignmentarray and greaterthan in assignmentarray:
			return True
		else:
			return False
			
        
        

    def booltestoftrue(self):
        #true key word test
        trueassignment = '''var x  = true;'''
        truestring = '''LexToken(TRUE,'true',1,9)'''
        assignmentarray = [self.lexer.test_function(trueassignment)]
        if self.variable in assignmentarray and truestring in assignmentarray:
			return True
		else:
			return False
        



    def booltestfalse(self):
        #false key word test
        falseassignment = '''var x  = false;'''
        falsestring = '''LexToken(FALSE,'false',1,9)'''
        assignmentarray = [self.lexer.test_function(falseassignment)]
		if self.variable in assignmentarray and falsestring in assignmentarray:
			return True
		else:
			return False
    
tests =  LexerTests()
tests.integerassignmenttest()        







    
