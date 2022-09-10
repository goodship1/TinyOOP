# SmallLox
A small Compiler written using python ply to lex and  Parse with the IR and code generation being handled by tinyllvm . An overview of the small Lox programming language . The small lox programming language is very small some what OOP programming language an Overview of some core features can be scene below 

# Overview of the Syntax 



# Types

```python
 var word  =  "hello"; //strings
 var age  =  20; // integers
 var weight =  20.0; // floats
 var TRUE =  true;
 var FALSE = False;
 var  none =  Nil;
 
 ```

# Expressions and assignment and Operations

```python

var  x  = 10;
var y  = 100;
var addtogether =  x+y;
var substract = x - y;
var times =  x * y;

var subtractfivefrom  = x-5;
var addfive = x + 5;
var isTrue = True;
var isFalse = False;
var none = nil;

x + y;
x - y;
x * y;

x < y;
x > y;
x<=y

var compareless  = x < y;
var greaterthan = x > y;
var lessthanequal = x<=y;
var greaterthanequal = x>=y;

```



# Control Flow If statements For loops and while loops

```python

number =  10;
start = 0;
while(start <=10){
   print "hello";
   start + 1;
   }
 
if  number  < 10 {
   print True;
 }
 else {
  print False;
  }

for(var z = 10; z <=20; z+1;){
   print z;
   }

```

# Functions

```python 

fun helloword() {
    return "Hello world";
 }
 
 fun sumto(a){
   var sum =  0;
   for(var x = 0; x <=a; x+1;{
     sum+x;
     }
     return sum;
     }
     
    
      
 
fun addtogether(a b) {
  return a + b;
 }
 
 ```
 
 # Classes
 
 ```python
 
 class house {
   init(numberofrooms,typeofhouse);
   var Numberofrooms =  numberrooms;
   var type = typeofhouse;
   
   
   fun getnumberofrooms(){
      return numberofrooms;
    }
    fun settypeofhouse(housetype){
      typeofhouse =  housetype;
      return typeofhouse;
      }
 }
        
    
 var  my_house =  house(10,"Cottage");
 ```
