    
#################################################################################################################################################          

  KEY POINTS 

 1)  a,b=[eval(x) for x in input("enter no :").split()]  # a,b= input("enter no :").split()
   print(a,b)
   print(type(a))
 
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
 NOTE: It will not give error , but it will give genrator object (a type of sequence)
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






  
