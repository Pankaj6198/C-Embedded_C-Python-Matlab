
Module : -> A file(.py) which contains varibles,functions , classes etc
         -> Every .py file is a called a module
          like: test.py is a also a module
         -> user define module can be accessed similar to built in module
            like : import pattern.py  or 
            import With_Without_Recurtion
            With_Without_Recurtion.factorial(5)
         -> modulename.variable or modulename.function_name() or class   
 NOTE: Whenever we are using a module , a separate complied file is genrated with " .pyc " extension(which is complied version of module/ .py file).
       which will be stored inside a folder " __pycache__"
       So, when we, import that module in ,some other file then " .pyc " file of that .py file is been fecthed for using functions , variable of modules which is been created..

# LIKE : if we create a .py file (With_Without_Recurtion.py) which has prototype of factorial() function
         So," With_Without_Recurtion.pyc " will be genrated and will be strored inside a folder " __pycache__"
        While ,  importing " With_Without_Recurtion.py " into a separete file ( test.py ) , the "With_Without_Recurtion.pyc" version of file will be feched to 
        access the module like to access factorial() function...
        
 1) Module Aliasing  :
 
      -> import With_Without_Recurtion as fact # here fact is alias name( other name or reference name)
      fact.factorial(5)
      With_Without_Recurtion.factorial(5) # NameError
      # After using aliasing , u can not use the original name 
  
     -> from ... import method  (Useful in directly accessing the content of module without using modulename. )
     # for using directly the functions,variable of module without using modulename.
      EX:
      from With_Without_Recurtion import factorial
      factorial(5)
      
 2) Member Aliasing : Giving other names to a method of the module
  
  Ex:  from With_Without_Recurtion.py import factorial as f,factorial_rec as fact_with_recursion
       With_Without_Recurtion.py . f(5)
       With_Without_Recurtion.py . fact_with_recursion(5)
       
  3) Various possiblities of import statement :
     1) import module1
     2) import module1,module2,module3
     3) import module1 as m1 # module alising
     4) import module1 as m1,module2 as m2,module3 as m3 #  multiple module alising with single import 
     5) from module1 import member # direct access to members without using module.member statement
     6) from module1 import member,member1,member2 # Multiple members for direct access
     7) from module import * # Direct access to all members of module
     8) from module1 import member1 as m1 # member aliasing
     9) from module1 import member1 as m1,member2 as  m2 # multiple members alising with single import

  4) Module Reloading: -> By default module is reloaded only 1(ONCE) time , therefore any change(adding new functionality, new function) in the module , we won't able to 
                       access, as each time " old version" of " .pyc " file of module is reloaded by appling multiple same import statement.
                       
                      -> Any change in module won't be access while importing it, as  by default old copy of module.pyc is stored in __pycache__ folder 
                      -> therefore , we need to explicitly reload module , to access upgraded version of module, whose new .pyc will be created.
                      -> " reload( Module_name)" is used to reload module explicitly, to access upgraded version of module in same python file
                      -> 
                      -> " reload() " method is in " imp " module..
Issue without using reload() -> 
                       
                         import time
                         import module1  # old copy of module which has add() only
                         module1.add(10,20)
                         time.sleep(30) # wait cursor on screen for 30 sec , meanwhile update module1 by introducing another function product in it...
                                         # Now, updated version of module1 has,2 methods add() and product
                      module1.product(10,20)# NameError : As PVM(python virtual machine) will load old copy of module1.pyc by default  so, therefore only add() is accessable                                       
                 
                # It will throw NameError as product() not initialised
                
       This can be solved using reload() in " imp " module to reload() module explicity,such that upgraded version of module can also be accessed..
        Ex:              from imp import reload
                         import time
                         import module1  # old copy of module which has add() only
                         module1.add(10,20)
                         time.sleep(30)
                         reload(module1) # reloading explicitly,the updated version of module1
                         module1.product(10,20)
                     #  30
                     #  200
    
    5)  Every python file is a module
       
     1)  -> dir() : returns list of members present in the current module/file ,also some extra members are added by the python interpreter for internal purpose.
         -> EX: # With_Without_Recurtion.py is opened
              print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
                           #  '__name__', '__package__', '__spec__','factorial', 'factorial_rec', 'i']
         -> dir() -> To listout members of current module.
         -> dir(module_name) -> To listout members of specific module # NOTE : Before that it must ne import in the file..
         #  VVVI : Differnce between dir() and help() :
         -> dir() will return a list with all methods available inside a given module..
         -> help() : Provides documentation related to that module. // module must be imported before
           
     2) Extra members added by python interpreter(pvm) inside a module . (Special Variables)
        -> __doc__ : Holds doc strings
        -> __file__ : Holds file name
    VVI -> __name__ : To decide whether its a direct or indirect execution of file/module. # covered in ponit no.3 
        -> __loader__ : which loader is responsible to load this module
        -> __package__ : Module related to which package ( Package is a collection of modules)
        -> And some more....
        
        Ex: """  This module contains some builtin members
            demo example"""
            print(__doc__) # o/p -> This module contains some builtin members demo example
            import os
            # Use of __file__
            print('File Name :',__file__) #  o/p -> test.py
            print('absolute path :',os.path.abspath(__file__)) # o/p -> C:\Users\Nutan\Desktop\Codes\test.py
            print('Directory Name :',os.path.dirname(os.path.abspath(__file__))) # o/p -> C:\Users\Nutan\Desktop\Codes
      
VVVI 3) __name__ : To decide whether its a direct execution or indirect execution of file/module.
   (special variable)  If its a "direct execution" it " __name__ "holds " __main__ " , and 
                  if its a " indirect execution" ,the module is been executer using other file/module(importing that file in other file),
                    then " __name__ " holds " module_name "                  
                 -> Direct execution means just executing the file through cmd. # just like main program
                 Ex: # Module1.py file is opened
                     print(__name__) # O/P -> __main__ 
                  # Executed using cmd directly (Normal case)
                  
                 -> Indirect Execution(using import statement ) is done by importing that module inside other module/file. 
                   # test.py is opened
                   import Module1.py # Module1.py executing.. Indirect execution : Module/file Module1.py containing print( __name__)
                   print("test module") # O/P ->  __name__ ='Module1'
                                        # test module
    
    4) Working with random module  : Use to genrated random nos. or random objects .
       ** IMP Fuctions in random module is :
        1) random() :Genrates random float no. between 0 and 1 .# NOTE : 0 and 1 are not included (Not inclusive)| (Same name as module_name) 
                     -> " does not take any argument "
                     -> 0<x<1 [0 and 1 not included]
                     
        2) uniform(start,end) : Genrates random float no. between the range. 
                              ->  start<x<end " start and end are not included " [Not inclusive]
                              
        3) randint(start,end) : Genrates random int no. between a range
                              ->  start=<x<=end " end points are included , start and end included"  [inclusive]
                     
        4) randrange([begin],end,[step]) :   Genrates random int no. from begin and end-1 #Note : like range() and slice operator
                                           * begin is optional & default value is 0
                                           * step is optional & default value is 1
                                         Ex:  from random import randrange
                                              randrange(5) # -> 0 to 4 ->Range will be [0,1,2,3,4] # From 0 to 4 a random no. will be genrated
                                              randrange(1,11) # -> 1 to 10 -> Range will be [1,2,3,,..10] # From 0 to 4 a random no. will be genrated
                                              randrange(1,11,2) # -> 1 to 10 with 2 steps -> Range will be [1,3,5,7,9] # From 1 to 10 a random odd no. will be genrated
                                              randrange(0,11,2) # -> 0 to 10 with 2 steps -> Range will be [0,2,4,6,8,10] # From 1 to 10 a random even no. will be genrated
                     
        5) choice(indexable_sequence) : Genrates random object from list,tuple,string etc # Note: Sequence must be indexable like string,list,tuple
                             Ex1: from random import choice 
                                 fruits=['Apple','Orange','Banana','Grapes']
                                 print(choice(fruits)) # O/P 'Orange'
                             
                             Ex2: # Genrating random alphabet
                                  from random import choice
                                  alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                                  print(choice(alphabets)) # A
                                  
 Q1: Genrate a random 6-digit OTP.
         -> from random import randint
            print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')
            # o/p -> 463476
            
Q2: Genrate a random password of 6 length where odd positions are symbols and even positions are digits.
         -> from random import choice
            digits='0123456789'
            alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            print(choice(alphabets),choice(digits),choice(alphabets),choice(digits),choice(alphabets),choice(digits),sep='')
            #Q4I7I9
            
 Q3: Genrate fake employees data for database testing :
             Parameters: 
            1)Employee Name  :  # Name should contain 3 to 10 characters and first character must be in uppercase and remaing in small
            2)Employee Number : # Must start with "e-" followed by 4 digits .. ex: e-1234
            3)Employee salary : # folat value from 10000 - 50000
            4)Employee City    : # cities=['Hyderabad', 'Chennai', 'Bangalore', 'Pune' , 'Delhi', 'Mumbai']
            5)Employee Mobile No. : # Must contain exactly 10 digits , It should be indian no. ie. first digit must be from 6 to 9
            6)Designation  : # designations=['Software Engineer', 'Senior Software Engineer', 'Team Lead', 'Project Lead' , 'Project Manager']

    -> 
from random import *
alphabets='abcdefghijklmnopqrstuvwxyz'
digits='0123456789'
cities=['Hyderabad', 'Chennai', 'Bangalore', 'Pune' , 'Delhi', 'Mumbai']
designations=['Software Engineer', 'Senior Software Engineer', 'Team Lead', 'Project Lead' , 'Project Manager']

def get_fake_name():
	name=choice(alphabets).upper() # First character of name should be uppercase
	n=randint(2,9) # Name must be of length 2 to 9  (Genrates Random int no. from 1 to 9 both included)
	for i in range(n):  # Random name from 2-9 characters
		name=name+choice(alphabets)
	return name

def get_fake_eno():
	eno='e-'
	for i in range(4):
		eno=eno+choice(digits)
	return eno

def get_fake_salary():
	esal=uniform(10000,50000) #  genrates Random float no. from 10000 to 50000  [Inclisive]
	return esal

def get_fake_city():
	city=choice(cities)
	return city

def get_fake_mno():
	mno=choice('6789')  # Indian no. must start with 6 to 9 digit only other 9 digits  can be anything
	for i in range(9):
		mno=mno+choice(digits)
	return mno

def get_fake_designation():
	designation=choice(designations)
	return designation

def get_fake_emp_data():
	print('Employee Name:',get_fake_name())
	print('Employee Number:',get_fake_eno())
	print('Employee Salary:{:.2f}'.format(get_fake_salary()))
	print('Employee City:',get_fake_city())
	print('Employee Mobile Number:',get_fake_mno())
	print('Employee Designation:',get_fake_designation())

for i in range(10):
	get_fake_emp_data()
	print() 






*********************************************************** Package *******************************************************
    
    function -> module -> package -> library
    # To use package it must be in current working directory and the file(ie. test.py in this case) from which we are importing must be same directory
    # both must be in codes folder
    1) Package : Collection of modules into a single unit
                -> Package is simply a  folder/directory with multiple modules/files
   Before " Python 3.3 version " -> A folder/directory will be called package only if it  contains " __init__.py " file else it won't be called as package 
                  even if this file ( " __init__ .py") is empty no problem.
                -> But, its a good practice to include __init__.py in package even if it is python 3.8   
   Note : Now, " In python 3.8 " -> Its( " __init__ .py") optional in higher version.
   
          Note   -> Package can also contain sub-packages/sub-folder ie, sub-folder inside a folder...
                    ex: Inside loan package(folder) , there is car_loan and home_loan sub-package/subfolder
                       So, to access file inside sun-module , can be access by"  loan.car_loan.file_name.py or loan.home_loan.file_name.py "  
    
    2) Advantages of Package :
        
        1) Naming conflicts can be resolved .
           ie .. suppose loan package/folder contain two sub-packages/folder car_loan and home_loan . Both sub-packages/folder have a account.py file .
              So, if u want to access account file of car_loan , then u can access it  by " loan.car_loan.account.py  "
              similary,account file of home can be accessed..
              It is only possible with the help of packages,... " package_name.file.py "
          If, it was not there, then we could have only store one file with same name....
        
        2) We can identify our component uniquely..
         ie: which account.py file belongs to which folder/module
         
        3) Modularity Increases (Separate components can be maintained and identified)
          
        4)  Readablity increases (files are managed in folder form)
        
        5)  Maintanabilty improves
        
        
    3) Example : To acccess f1() from test.py  
                E:/python 
                |
                |-------> test.py
                |
                |-------> pack1
                |        |----> __init__.py (Optional for python 3.3 onwards )
                |        |----> module1.py 
                |        |      |--> contains f1()
                |        |
 
 ----------->  # module1.py opened
               def f1():
                print(" This f1() is from module1 of pack1")
                
               # test.py opened
               import pack1.module1
               pack1.module1.f1() # O/P -> This f1() is from module1 of pack1
           OR
              from pack1.module1 import f1
              f1() # O/P -> This f1() is from module1 of pack1
  
    
VVIMP  4) Importance of " __init__.py "   :
          VVVI:
            NOTE: -> #  At the time of using a package , if we want to perform any activity automatically ,
                    # then we have to define that activity inside this " __init__.py " file.
     
            -> Hence , " __init__.py " file is meant for " initialization activty "
            -> " __init__.py " anything written in this file will be executed automatically, if u are using that package by import ..
                ex: from pack1.module1 import f1
           
           
 IMP    5) Relationship b/w functions,module,package and library
         
            1) Functions : A piece of block , which contains multiple statements and can be invoked/called throughout the program
            2) Modules : A python file which has collection of variables,functions,class etc present in it. 
            3) Packages : A folder/directory ,which has collection of related modules,submodules in it
            4) Library : Collection of related packages.
        
        
    Note : To Use package it must be in current directory of of that file in which we are using that package...

        5)  How to install a python package :
           
           # Need of installing is that... then we can access that package from anywhere, by default
           
         ->  To do so, We need to create a " setup.py " script in same directory where that package is present
           
        E:/python 
                |
                |-------> setup.py
                |
                |-------> patterns # Package 
                |        |----> __init__.py (Optional for python 3.3 onwards , Good practice to include )
                |        |----> shapes.py
                |        |      |--> f1()
                |        |
         
         -> Create a setup.py script in same directory where that package is present.
         -> Use setup() from setuptools(buildin) module in that script " setup.py "
         -> Ex:  # setup.py opened
                 from setuptools import setup,find_packages
                 setup(name='patterns',version='0.1',packages=['patterns']) # name='Package_name' , version= # own software , 
                                                                            # package=['How many packages u want to install']
              OR
                setup(name='patterns',version='0.1',packages=find_packages()) #packages=find_packages() to install all packages inside that directory
              
         -> So, Now to install it...
            Go to, current directory : type " pip install . "
            # If package is devleoped by 3rd party 
            then , pip install package_name
            Ex: " pip install django" , 
                " pip install pymysql ",
                " pip install selenium " ,
                " pip install faker " # To genrate fake data
    
            
         -> To uninstall package :
            " pip uninstall package_name "         