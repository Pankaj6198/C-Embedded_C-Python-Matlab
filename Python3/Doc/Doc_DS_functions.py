    
#################################################################################################################################################          

  KEY POINTS 

 1)  a,b=[eval(x) for x in input("enter no :").split()]  # a,b= input("enter no :").split()
   print(a,b)
   print(type(a))
   
************    NOTE  ***** 
    Tuple --> Hashable
    List --> UnHashable
    set--> add element based on hashcode
    In dict keys are added based on hashcode
    
    Only hashable objects can be added into set and dict(only keys)
    for ex ==> s={(10,20,30),[10,20,30]} ==> type error only hashable objects can be added .. list is not hashable
               d={("pankaj":108),"Name":['a','b','c']}  --> Valid , values can be anything(list,tuple,set,dict) but keys cant be list    
               d1={("pankaj":108),['name','rollno']:108} ---> Invaild typeerror dict keys cant be list as list is unhashable
  
 2) VV.IMP ===> *n means all values in n , where n can be list,tuple,set,dictionary anything
    l=[10,20,30]
    *n --> variable length argument in function concept ,**n variable length keyword argument
    print(*l)===> *l means all values in l
    
    MERGING CONCEPT FOR COLLECTIONS(list,tuple,set,dict)
    
    $$$ using *args,**kwargs for merging 
    for example:
    l1=[10,20]
    l2=[30,40]
    l3=[*l1,*l2] ==> *l1 means all values of l1
    print(l3)===> [10,20,30,40]
    
    same for tuple and set is valid....
    
    for dict use **d  ---> for all key,value merging 
    d1={10:"a",20:"b"}
    d2={30:"c",40:'d'}
    d3={**d1,**d2}  
    print(d3) --> {10:"a",20:"b",30:"c",40:'d'} 
 
 2) the sentence 'The quick brown fox jumps over the lazy frog'  --> A meaningful sentence which have all 26 alphabets within it .......

 3)Anagram (these are those strings which are equal in length and have same characters) for ex. --> SILENT LISTEN  

 4) a=[]    # list method extend is used to extend list, but we give string as a input then each character of that string will be added in the list   
    a.extend('hii')  #---> a=['h','i','i']
    Extend is same as update in set

 5)tuple with 1 element is created as t=(10,) , as if comma is not provide it will just consider parenthesis that is used in maths ... (10)+200+3 

   * Tuple packing and unpacking (also aplicable for all other data types except dictionary (key value pair)) 
  
        packing --> to pack variables into a tuple/other data type
  
        unpacking --> to unpack tuple element into different variables
  
        for example:
   packing:  a=10
             b=20
             c=30
             t=a,b,c  #---> packing a,b,c,d into tuple   t=(10,20,30)          
  
  NOTE: IF THERE IS NO PARENTHESIS IT WILL CONSIDER AS TUPLE EX: T=a,b,c,data , if t=[a,b,c,d] then it will be list
 
   unpacking:
             t=(10,20,30)
             a,b,c=t   #--> a=10 b=20 c=30
             
  
 6) in case of set : values given to a,b,c will be unpredictable as order is not preservved in set
                    a=10;b=20
                    s={a,b}
                    a=20, b=10 ---> values can be anything (10 or 20) 

**********NOTE:  
    Tuple comprehension not supported in python( As tuples r immutable) --> 
 NOTE: It will not give error , but it will give "genrator object" (a type of sequence)
   t=(x for x in range(10))

  
  7) Dictonary (Only tuple elements can be used as items in dictionary)
  d={100:"hii",200:"heyy"}
  To create dictionary with dict keyword 
   ---> dict() takes only one argument  
  
     And that must be  list of tuples , tuples of tuples or set of tuples   
    d=dict(20:"hi")--> INVALID  , it accepts only one argument like list of tuples
    like  --> d=dict([(100,'hii'),(200,'hey')])   ---> list of tuples
              d= dict(((100,'hii'),(200,'hey')))  ---> tuples of tuples
              d= dict({(100,'hii'),(200,'hey')})  ---> set of tuples
   
    d.items()  --> returns list of tuples 
 NOTE  : 
    d.pop(key)  --> returns value associated with the key and will remove that item from dictionary
    d.pop() ---> will through keyerror
    d.popitem()----> will remove random item from dict
    del d[key]  --> will remove the item with specific key
    del d  ---> delete the object d (object eligible for gc(garbage collection) )
     d.clear()---> clear all items from dict
      d1=d  ---> will create refference(alasing) object d1 both having same id
       d1=d.copy() ---> cloning (only content will be same but object will be different , id will be different)

    d.get(key,default_value) ---> retuns value associated with key 
    d.get(key)  if key is not found ,  returns None (by default)
      
 VVI:  d={100:'hi',200:'hey'} 
  Adding items to dictionary: 
       d[key]=value ---> in this approch if key already present , it will overwrite the value . id key not present add new item to dictionary 
       d.setdefault(k,v)  --->in this approch if key already present, it will not overwrite(ccontent of dict will remains the same),
                              old value remains the same and returns old value, 
                              And if key is not present then item with particular k,v will be added in dictionary
   For Ex:   
                d={100:'hi',200:'hey'}  
                d[100]='ok'
                >>> d
                {100: 'ok', 200: 'hey'}
                >>> d.setdefault(100,'ohh')
                'ok'
                >>> d
                {100: 'ok', 200: 'hey'}  
                
  d.update(d1) #only one argument  ---> to extend dictionary  , same as in set update method(can have more than one argument (sequence))  
                                        and in list extend method  (only one argument)       
   


################################################################################################################################################

########### STRING BASED PROBLEMS ##########################


a="hello world world hello"
b=[]
c={}
b=a.split()
print(b)

for word in b:
	count=0
	for i in b:
		if i==word:
			count+=1
	c[word]=count
print(c)

for char in a:
	b.append(char)

for i in b:
	c[i]=0;
	count=0
	for j in b:
		if j==i:
			count+=1
	c[i]=count

print(c)

##################################################

a={}

str="hhi i am pankajjj"

for i in str:
   count=0
   for j in str:
       if(i==j):
           count+=1
   a[i]=count
print(a)
            
##########################################

str="hi pankaj hi hi it me pankaj"
a={}
l=str.split()
for word in l:
   count=0
   for ele in l:
       if word==ele:
           count+=1
   a[word]=count
print(a)   

###############################################

s="a2c3b1"
output=''
for ch in s:
 if ch.isalpha():
   c=ch
 else:
   output=output+ int(ch)*c
print(''.join(sorted(output)))      

######################################################
 

s="aaabbccc"
i=0
count=0
pre=s[0]
output=''
count=0
while i<len(s):
   if s[i]==pre:
      count+=1
   else:
      output=output+str(count)+pre
      pre=s[i]
      count=1  
   if i==len(s)-1 :
      output=output+str(count)+pre    
   i+=1 
print(output)

###########################################################


s='a4k3b2'  #predicted output ==> aeknbd  -->prev char + digit will get that char
prev=s[0]
val=0
output=''
i=0
while i<len(s):
  if s[i].isalpha():
    val=ord(s[i])
    prev=s[i]
  else:
    output=output+prev+chr(ord(prev)+int(s[i]))
  i+=1
print(output)
  
 
###########################################################

remove duplicate char from string

s='paapppppannnnkkkajj'
i=0
output=[]
while i<len(s)-1:
   if s[i] not in output:
      output.append(s[i]) 
   i+=1
print(''.join(output))  
   
############################################################

No. of occurance of each character in a string

s='abbabbaacdcd' 
l=[]
i=0
while i<len(s):
    if s[i] not in l:
       l.append(s[i])
    i+=1   
i=0
while i<len(l):
    print(l[i],"occurred",s.count(l[i]),"times")
    i+=1    
    

Same using dict
 
s='aaabbddqwwsszzs'
d={}
for ch in s:
  d[ch]=d.get(ch,0)+1 # d.get(key) will return value associate with that key 
print(d)               # and if that key is not available it will return None
                      # 2nd argument in d.get() is the default value that it will return if key is not found
print(sorted(d)) # to show sorted keys..... sorted always return o/p in list                  
                 sorting based on keys

###################################################################

s="aabbcddeaa"  #predicted o/p -> 4a2b1c2d1e
d={}
output=''
for ch in s:
   d[ch]=d.get(ch,0)+1
for k,v in d.items():
   output=output+str(v)+k
print(output)

###################################################################

find no. of vowels present in a string

s='pankaj iioa'
d={}
l=['a','e','i','o','u','A','E','I','O','U']
for ch in s:
    if ch in l:
       d[ch]=d.get(ch,0)+1
print(d)
# Or u can print individually
for k,v in d.items():
  print('{} occured {} times'.format(k,v))
 
#######################################################################

find the occurance of a given substring
s='abcdpankaj123pankajsdfghs'
subs='Pankaj'
count=0
pos=-1
i=0
count=0
while 1:
  pos=s.find(subs,pos+1,len(s))
  if pos==-1:
    break
  print("Substring",subs,"found at index",pos)
  count+=1
print(subs,"Occured:",count)

#############################################################################

s='B4A1D3'   #Predicted o/p => ABD124
s_alp=''
s_dig=''
for ch in s:
  if ch.isalpha():
    s_alp=s_alp+ch
  else:
    s_dig=s_dig+ch
s_alp=sorted(s_alp) #sorted function returns a list
s_dig=sorted(s_dig)
print(''.join(s_alp + s_dig))


##################################################################################################################################################

************    FUNCTIONS :

1) def cal(a,b):  ---> parameters
    return a+b,a-b

    x=cal(20,10)  --> arguments  (positional argruments)
    print(x)   ------> type(x)-> tuple
 
2) ########  4 Types of arguments
 
    1) Postional Arguments(Applicable : In calling(Actual parameters)) ---> Normal one  --> order matters
        eg: def cal(a,b):
          print(a,b)
          cal(20,10) -----> postional arguments
 
    2) Keyword Arguments(Applicable : In calling(Actual parameters))  ---> Order does not matter
    --> Commonly used as we dont have to remember the order of paramters to make a call
        passing parameter names in the arguments to make a call
    eg: def cal(a,b):
          print(a,b)
       cal(a=20,b=10) -----> keyword arguments
        cal(b=10,a=20) -----> keyword arguments

    **## !!! NOTE : U can use both but, first must be positional ..
    #         ex :
         def cal(a,b):
          print(a,b)
       cal(20,b=10) ----->  Valid
        cal(b=10,20) -----> ## INVALID , first must be postional 
 
    3)  Default Arguments (Applicable: In function defination(formal parameters)) : When default values to the parameters is to be given,.. calling a function(which is having a argument in defination)
    without parameters will throw an error
        
    For Ex:   def wish(name,msg):
                print('HELLO',name,msg)
              wish()   ----->  Error as wish has to take argument can't call it as empty
              wish('Pankaj','Good Morning')---> Vaild
              
    SO, to encounter this, we have default argument, throoung which we can even make a empty call ,by passing it some default value
 
    Default Argument example:
      
        def wish(name='GUEST',msg='Good Morning'): # Here the value  guest and good morning is default value  
            print('HELLO',name,msg)                # , So even if we make a empty call it will not throw an error , it will give default value
        wish()---> will print default value 


   ********** NOTE : After DEFAULT argument we can not take NON-DEFAULT Argument..
    FOR ex:  def wish(name='Guest',msg): ------> INVALID
                print('HELLO',name,msg)
    
    EITHER All must be default or it should at the last..
             def wish(name,msg='Good Morning'): ------>  VALID
                print('HELLO',name,msg)

    
    4)  Variable Length Argument(*args)(Applicable: In function defination(formal parameters)):
                        Can pass any number of argument to the function...even 0(empty call)
    **** USED WHEN U CAN PASS ANY NUMBER OF ARGUMENT, SHOULD WORK ON ANY NO. OF ARGUMENT 
    tuple(n) will be created with the value u r providing in call.......
    for ex:  NOTE---> *n ----> variable length argument --> n will be tuple having values which we giving in call  
        def sum(*n): ----> n will be tuple of values which we are passing 0,3,2 ETC
            total=0
            for x in n:
                total=total+x
            print("Sum =",total)  
        sum()
        sum(10,20,30)
        sum(10,20)
        sum((1,2,3),(2,3,45)) # then n will be tuples of tuple

    !!!!!!!!! NOTE: MORE THAN ONE VARIABLE LENGTH ARGUMENT IS NOT ALLOWED.....
    FOR EX:
    def f(*x,*y):  -----> Syntax ERROR(INVALID) only one variable length argument is valid....
      pass
    f()
    
    
     VVI: DIFFERENCE BETWEEN *argv and **kwargv
         ----------------------------------------------------------------------------------------------------------------------------------------------
        |                 *args                         |                           **kwargs                                                              |
        ------------------------------------------------------------------------------------------------------------------------------------------------
        |                                               |                                                                                              |
        |  1) Variable length argument                  |  1) Variable length key-word argument                                                        |   
        |     (we can call with any no. of arguments)   |     (We can pass any no. of keyword argument and that will be internally                     |                                                                     |
        |     (And that will be tuple internally)       |        stored as key-value pair dictionary)                                                  |
        |  2) def f1(*n): n --> tuple (internally)      |  2)  def f1(**n): n--> dict (internally)                                                     |
        |                                               |                                                                                              |
        |  3) ex: def f1(*n):                           |  3)  ex: def f1():                                                                           |
        |          print(n)  -->tuple                   |            print(n)                                                                          |
        |          f1()   ==> ()                        |          f1() ===> {}--> empty dict                                                          |
        |          f1(10) ==> (10)                      |          f1(name='Pankaj',rollno=108)==> {'name':'Pankaj','rollno':108} --> keyword arguments|  
        |          f1(10,20)==> (10,20)                 |          f1(A=10,B=20,C=30) ==> {'A':10,'B':20,'C':30}  --> key value pair                   |
        |                                               |                                                                                              |
        |                                               |                                                                                              |
        |                                               |                                                                                              |
        ------------------------------------------------------------------------------------------------------------------------------------------------
        
  ~~~~~~~~  NOTE: After positional argument , u can give keyword argument but after keyword argument u can not give positional argument
            Ex:
                 def f1(a,b):
                    print(a,b)
                f1(10,b=20)   ------> valid
                f1(a=10,20)  ---> ERROR : positional argruments must be before keyword arguments
  
             NOTE : BOTH *args and **kwargs can be used simultanously but *args must be first and then **kwargs
                  
              Ex1:    def f1(*n,**x):   -----> Vaild
                       print(n,x)
                     f1(10,20,A=30,B=40)
              Ex 2:  
                    def f1(**x,*n):   ----->    INVALID (ERROR)
                       print(n,x)
                     f1(A=30,B=40,10,20)  ----> As postional arguments has to be given before keyword argument
  

 5) global keyword  : 1) Use to declare a global varible inside a function(To make available global variable to local(function) having same name)
                      2) To use global variable inside a local body having same variable.
                      3) global keyword is only used for declaring not initialing, to make global variable available inside a fucnction
                      4) global a =10 # Invalid syntax
                         global a # valid
                    for ex:
                    a=10     # global variable
                    def f1():
                        global a   # global declaration
                        a=20       # a is used after global declaration 
                    f1()
                    print(a) -->20
                       
             ******* IMP ***   4) Before ,global declaration you can't use that varible...
                       for example: a=100
                                    def f1():
                                           print(a)  # a is used before global declaration which is invalid
                                           global a
                                           a=200
                                           print(a)
                                    f1()
                                ### Error: As, before global declaration u cant use that varible
                                
            VVI: How to access global variable inside a local function having same name
            
                 5) Use globals() functions : which returns a dictionary having all global varibles of the files as key and its values..
                   for example:
                        a=100
                        def f1():
                            a=200
                            print(a) ---> #200
                        f1()
                   
                    But , how to print a=100 
                 # d.get(key) or d[key] --> globals().get(key) or globals()[key]
                  a=100
                  def f1():
                    a=200
                    print(globals().get('a')) # a=100 ,globals {'a':100}
                    # or print(globals()['a'])
                  f1()

6) Recursion depth in python 3.8.8 = 1000 calls (n-1,n-1....n-999)
  
        sys.getrecursionlimit() ----> Returns Max limit of recursion depth
        sys.setrecursionlimit(10000) --> To set recursion depth
        
 
**************** VVIMP ******************************** 
7) Anonymous functions (Lambda Functions) --- > Fuction having no name  ( Nameless function) -->function used for instant use (one time use)
             1) Nameless function
             2) Use for Instant use (One time use)
             # Anonymous means someone with no identity or no name..
             
    syntax:   lambda n:n*n  ---> Anonymous function

            lambda input-argument:  expression

    So, to call anonymous function we have to give it a name after which its no longer anonymous...
            
               function_name =lambda input-argument: expression
               
               function_name(argument) # to call
    for example:
            # square of a no.  
            s=lambda n:n*n
            print(s(10))
            # square of first 10 nos.
            for i in range(11):
              print("Square of {} = {}".format(i,s(i)))

8) ********* VVI *******
   function as a argument to another function using lambda with filter(),map(),reduce()
   *** Example of these functions are
        1) filter(function,sequence) 
        2) map(function,sequence)
        3) reduce(function,sequence)
***NOTE*** # U can range() in sequence as well
  All of these built-in functions(# except reduce() its in the module functools) takes function as a argument...... )
  
  ++++++ IMP +++++++ More often we use lambda function as argument to these built-in(filter(),map(),reduce()) fucnction 


   1) filter(function_name,sequence) : -> Returns Filter object, must typecast to ur need..
      (built-in function )             -> The function as argrument will take each value  from the sequence and procces it.
                           ***NOTE*** # if i/p = 10 elements , then O/P will have < =10 elements (some maybe filtered)
                                       -> In filter() o/p is the element from the sequence
                                       -> filters some content from a list and filter it based on some function( based on some condition) and store the result into a list.. 
                       VVI *** NOTE**  -> function as a argument must return True or False .. therefoe use lambda function
                                       -> The function will applied on each element in the sequence and ... 
                                       if the function returns True then that element will be added into the result else return False
                                  -> Function is for condition based on which the sequence shold be filter
                                  -> if input_list (sequence)= 10 element then output_list(result) will have < = 10 elements 
                                  
                        for example : to filter even no. from  a sequence ... 
                       commonly used in  that types of problems where we have (to filter sequence based on some conditions(function))
NOTE : # filter() is used for conditional check to filter some values from a sequence
   For example: 1)  Using filter() without lambda       
                l=[0,1,2,3,4,5,6,7,8,9,10]
                def IsEven(n):
                  if n%2==0:
                    return True
                  else:
                    return False
                    
                l1=list(filter(IsEven,l)) # As filter() returns filter object , therefore must typre it before storing
                print(l1)
                        
       ****** Passing function as a argument to another function ********
        **** IMP *********** 
     ->   Same problem with lambda and filter() function
        example:  l=[0,1,2,3,4,5,6,7,8,9,10]
                  even=list(filter(lambda n:n%2==0,l)) # lambda function will return True or False based on the condition ( n%2==0 )
                  print(even)                          # if its True filter function will add that element into the l1(result)
            OR
            #l=[0,1,2,3,4,5,6,7,8,9,10]
            even=list(filter(lambda n:n%2==0,range(11))) # lambda function will return True or False based on the condition ( n%2==0 )
            print(even)
    
    2) map(function_name,sequence) :  -> Returns map object therefore type it according to ur need.
     (built-in function )  ***NOTE***   # i/p =10 element, then o/p will also have 10 elements                                
                                      -> For every i/p element(from sequence) , a o/p will be genrated  
                                      -> The function as argument , which will return some value and that value will be added into the result
                                      -> ***note ** O/P element can be anything (like diffrent than  sequence) not like filter where o/p is from the sequence only
                                      -> For every I/P value(sequence) , A mapped value will be genrated by appling some function.
                                      -> Here , if input contains 5 elements , then compulsary output will also contain 5 elements.
                                         for example: find square of each element in a list
                                              if l=[1,2,3,4,5,6,7,8,9,10]
    o/p should be mapped with the input  , then o/p -> l1=[1,4,9,16,25,36,49,64,81,100]
                                             
                                       Here , Each element is mapped with its corresponding element in the i/p
NOTE:# map() is used for modification ,to perform some operations maybe square function , add function, multiplication function etc 
       Example: map() without lambda  
                    l=[1,2,3,4,5,6,7,8,9,10]  # i/p
                    def squareit(n):
                       return n*n
                    l1=list(map(squareit,l))  # l1->o/p 
                    print(l1)     # l1=[1,4,9,16,25,36,49,64,81,100]
                    
                    # I/P = 10 elements , and O/P = 10 elements which are not from the sequence
     
       Example : Same problem with lambda function 
                l=[1,2,3,4,5,6,7,8,9,10]  # i/p
                l1=list(map(lambda n:n*n,l))  # lambda  will return squares of values mapped to l (ie. corresponding to i/p values)
                 # l1=[1,4,9,16,25,36,49,64,81,100]
                OR
                #l=[1,2,3,4,5,6,7,8,9,10]  # i/p
                l1=list(map(lambda n:n*n,range(1,11)))  # lambda  will return squares of values mapped to l (ie. corresponding to i/p values)
                # l1=[1,4,9,16,25,36,49,64,81,100]
                 
  ********** NOTE ******************
   map() is also valid for multiple sequences (If both sequences are having different length then remaining elements will be ignored ,
                                                only element which can be mapped will be added)
                                           (ie. upto common length the result will be stored , other elements will be ignored)
  for example:
               l1=[1,2,3,4,5]
               l2=[5,10,15,20,25]                 # lambda will take two argument as i/p from 2 sequences
               l3=list(map(lambda x,y:x*y,l1,l2)) # lambda function will take each value from sequences l1 and l2,
               print(l3)                          # And return the multiplication of corresponding values fron both the list
               # l3=[5,20,45,80,125]
               
 Conclusion : filter() is used for conditional check to filter some values from a sequence
              map() is used for modification ,to perform some operations maybe square function , add function, multiplication function etc
              
                                                  
        3) reduce(function_name,sequence)  : -># reduce() function is in functools module
   (NOT bulit-in function -functools module) -> reduce() function always return 1(ONE) value , therofore# NO need of typecasting here  
                                             -> reduce() function reduces element from a given sequence into ONE element by applying some function.
                                            (For example: There is salaries of employess, then what will be sum of all salaries, average ,
                                                          aggregate,count like that by appling some function)
                                *** NOTE*** # IF i/p is 10 elements , then o/p is 1(ONE) element
                                             
                                             -> The function(as a argument) is responsible for reducing it into 1(ONE) element..
            Here, lambda will take multiple input arguments from one sequence only 
        Example 1: from functools import reduce
                 l=[1,2,3,4,5,6,7,8,9,10]
                 result=reduce(lambda x,y:x+y,l) # It will keep taking 2 values(alternately) from the sequence and keeps on 
                 print(result)                   # adding 2 elements from sequence till ONE value is genrated
                 # result=55
                 
        Example 2 : # to find sum of first 100 nos. using reduce()
                    from functools import reduce
                    sum=reduce(lambda x,y:x+y,range(1,101))  
                    # sum= 5050                    