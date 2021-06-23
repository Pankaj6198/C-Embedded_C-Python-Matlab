
######################################################### OOPs PART- 4 ############################################################

A)  Polymorphism :
 
 1) Polymorphism : ->  Poly means Many , Morphs means Forms
                   ->   Polymorphism means ' Many Forms '
                   ->  One name but multiple forms is the concept of Polymorphism
                
               Example 1: ' Operator Overloading ':
               
                    + operator : One operator many behaviour
                    
                    10+20 = 30 , arithmetic operation
                    'a' + 'b'= 'ab' , string concatination
                    
               => known as ' Operator Overloading ' (One operator many behaviour)
                
                
                Example 2: ' Method overriding '
                 ie.. if the child is not satisfied by parent method implementation,
                      then, child is allowed to redefine that method based on its requirements...
                      
                      class P:
                           def marry(self):
                                print('Subhalaxmi')
                      class C(P):
                           def marry(self):     # Overriding
                                print('Katrina Kaif')
                                
                      c=C()
                      c.marry() # Katrina Kaif
  
 2) Overloading :
                   1) Operator Overloading: -> Same operator for multiple purposes
                                            -> Python supports operator overloading
                                            -> Java wont provide support for operator overloading
                                            # NOTE: In java '+' can be used for string concatination,
                                            # but it does not allow '+' operator to apply on objects...
                                            # In python its applicable('+' operator on objects) but, not directly, after some changes
                                          -> Example 1: 
                                            
                                            + operator : One operator many behaviour
                                             10+20 = 30 , arithmetic operation
                                            'a' + 'b'= 'ab' , string concatination

                                          ->    Example 2: 
                                            
                                            * operator : One operator many behaviour
                                            10*20 = 200 , arithmetic operation
                                            'b'*2 = 'bb' , Repetation Operator

                                           -> To apply operations(like *,+,/,>=,<=,==) between two objects, for that compulsary magic method must be implemented before... 
                                   'NOTE'  -> In python, whenever we use '+' operator between objects, it internally calls a special method ' __add__() ',
                                               therefore, u have to define __add__ ,( magic method) when u use '+' operator for objects..otherwise it will throw error
                                              ex:  # For adding two objects only
                                            class Book:
                                                    def __init__(self,pages):
                                                            self.pages =pages
                                                    def __add__(self,other): # mandatory to add, without this special method u can not add objects
                                                        total_pages=self.pages+other.pages
                                                        return total_pages
                                            b1=Book(100)
                                            b2=Book(200)
                                            print(b1+b2) # b1  will goes to self and b2 will goes to other
                                                          # internally calls to magic method __add__(self,other) with self will have b1 and other will have b2 
                                           # Output : 300
                                   
                                        """  NOTE : adding multiple objects , we need some changes """
                                        
                                        class Book:
                                                def __init__(self,pages):
                                                        self.pages=pages
                                                def __add__(self,other):
                                                        print('add method executed...')
                                                        return Book(self.pages+other.pages)
                                                def __str__(self):
                                                        return 'The Total Number of Pages: {}'.format(self.pages)
                                                def __mul__(self,other):
                                                        print('mul method executed...')
                                                        return Book(self.pages*other.pages)


                                        b1=Book(100)
                                        b2=Book(200)
                                        b3=Book(500)
                                        b4=Book(600)
                                        #print(b1+b2*b3+b4)
                                        #print(b1*b2+b3*b4) 
                                        print(b1+b2+b3+b4)  # __add__ will be called 3 times, for b1+b2,b2+b3,b3+b4 
                                        # O/P : 
                                        add method executed...
                                        add method executed...
                                        add method executed...
                                        The Total Number of Pages: 1400
                                        

                                         -> Operators and Corresponding magic methods :
                                            ( called automatically, when we perform arithmetic operations on objects )
                                            # NOTE: U have to define it explicitly , these magic method
                                            ( Magic  Methods : To overload operatator, we must implement coresponding magic method)
                                           # self , other will refer to the two operands objects(b1,b2)
                                            1) +  => __add__(self,other)              8) +=  => __iadd__(self,other)
                                            2) -  => __sub__(self,other)              9) -=  => __isub__(self,other) 
                                            3) *  => __mul__(self,other)             10) <   => __lt__(self,other)                                            
                                            4) /  => __div__(self,other)             11) <=  => __le__(self,other)
                                            5) // => __floordiv__(self,other)        12) >  => __gt__(self,other)
                                            6) %  => __mod__(self,other)             13) >=  => __ge__(self,other)
                                            7) ** => __pow__(self,other)             14) ==  => __eq__(self,other)
                                        
                                        -> overloading of > and <= operator of student class object
                                        ( if u want to use > operator between two student object , complusary u have to implement corresponding magic method)
                                        class Student:
                                               def __init__(self,name,marks):
                                                     self.name=name
                                                     self.marks=marks
                                               def __gt__(self,other):
                                                     res=self.marks>other.marks
                                                     return res
                                        s1=Student('Shiva',100)
                                        s1=Student('Ravi',200)
                                        print(s1>s2) # False
                                        print(s1<s2) # True  , not require to implement __lt__() as __gt__() is implemented 
                                        # Note: If we didn't implement magic method we will get error
                                       
                                       -> Overloading of multiplication operator for Employee Objects
                                          
                                          -> order is important : first argument while operation(e*t) ,class related to first argument class must contain  magic method,
                                                                  else it will throw error
                                          (e*t)--> here, magic method should be implemented in e(Employee class),as  here first argument is e 
                                          (t*e)--> magic method should be implemented in t(timeSheet class),as  here first argument is t

                                          Ex:
                                          
                                          class Employee:
                                                 def __init__(self,name,salaryPerDay):
                                                           self.name=name
                                                           self.salaryPerDay=salaryPerDay
                                                 ## magic method __mul__(self,other) must be define in Employee class , as PVM will always call magic method from first argument
                                                 ##  (ie. e is first argument in e*t )
                                                 def __mul__(self,other)                        # self will refer to e object and other will refer to t object ,
                                                     res= self.salaryPerDay * other.workingDays   # automatically passed when operation b/w objects (e*t) operator overloading
                                                     return res
                                          class TimeSheet:
                                                 def __init__(self,name,workingDays):
                                                        self.name=name
                                                        self.workingDays=workingDays
                                                        
                                          e=Employee('Ravi',500)
                                          t=TimeSheet('Ravi',25)
                                          print(" This month salary : ",e*t) # NOTE:  __mul__() must be in Employee class as its e*t , 
                                                                            # Always PVM will call magic method from first object/argument(ie. e is first argument in e*t )
                                          # O/P :
                                          #  This month salary : 12,500          
                                                                              ##  to overload any method compulsary corresponding magic method(here __mul__(self,other)) 
                                                                              ## is required  else it will give TypeError
                                          
                                          NOTE:  
                                         -> if it was print(" This month salary : ",t*e) then t ie.timeSheet class should contain the magic method...
                                          but here, it is e*t , thus magic method is implemented in Employee class...
                                          Thus,print(" This month salary : ",t*e) will throw error as magic method is  implemented in Employee class 
                                          becoz first argument is e not t ...
                                        -> if both have magic method, then both (e*t) or (t*e) will work...                    
       
       # VVVI NOTE:       
       -> Importance of __str__ : ->  Whenever we print any referance of a object , internally __str__() is called...
                                   # default implementation of __str__() is
                                   # <__main__.Student object at 0x00000200B1CA8BE0>
                                   # <__main__.Student object at 0x00000200B1CE3580>
                                  
                                 -> But, if u want something meaningful(like name etc.) instead of this , then u must implement __str__() method
                                 ie. tto provide meaningful string representation for our object, we have to override(override with default) __str__() method in our class.. 
                         Example:              
                                  class Student:
                                        def __init__(self,name,rollno,marks):
                                            self.name=name
                                            self.rollno=rollno
                                            self.marks=marks
                                        def __str__(self):
                                            #return self.name
                                            return 'Name:{},Rollno:{},Marks:{}'.format(self.name,self.rollno,self.marks)
                                  s1=Student('Ravi',101,96)
                                  s2=Student('Shiva',102,98)
                                  print(s1)
                                  print(s2)
                                
                                 # Output ,when __str__() is implemented
                                   Name:Ravi,Rollno:101,Marks=96
                                   Name:Shiva,Rollno:102,Marks=98
                                   
                                 #  Output ,when __str__() is not implemented ,( default implementation of __str__() ) 
                                       <__main__.Student object at 0x00000200B1CA8BE0>
                                       <__main__.Student object at 0x00000200B1CE3580>      
                                                            
                                       
                   2) Method Overloading : ' Both methods having same name but different argument list' 
             'NOTE' # Supported in java
             'NOTE' # Not supported in Python, bcoz its is a dynamically typed language ie. In python we cant define the type explicitly...
                   -> if u try to implement methods with same name but diffrent arguments, than last copy will be consider while calling..
                    Ex:
                       class Test:
                            def m1(self):
                                print("no-argument method")
                            def m1(self,x):
                                print("one-argument method")
                            def m1(self,x,y):                 # This copy will be considered
                                print(" Two-argument method")    
                       t=Test()
                       t.m1(10,20) # Valid 
                       # O/P :  Two-argument method"
                       
                       t.m1()   # Error, 2 arguments should be given
                       t.m1(10) # Error, 2 arguments should be given
                       
                        
                   
      'NOTE'       -> " method overloading not supported in python : "
                     Other ways to implement the same functionality method overloading
                     (function with same name but different argument)
                   ->   Two ways :
                       1) using Default agrument
                         ex: # Only for three argument
                             class Test:
                                    def m1(self,a=None,b=None,c=None):  # default Argument - None 
                                        if a is None and b is None and c is None :
                                            print("no-argument method")
                                        elif a is not None and b is None and c is None :
                                            print("one-argument method")
                                        elif a is not None and b is not None and c is None :
                                            print("two-argument method")
                                        else:
                                            print("three-argument method")
                             
                            t=Test()
                            t.m1()         # no-argument method                 
                            t.m1(10)       # one-argument method
                            t.m1(10,20)    # two-argument method
                            t.m1(10,20,30) # three-argument method
                          
                       
                       2) using variable length argument
                         Ex 1: # Any number of argument
                              class Test:
                                    def m1(self,*args):  # Variable length Argument
                                        print("{}-Argument/s passed to m1() method".format(len(args)))
                              t=Test()
                              t.m1()  # 0-Argument                
                              t.m1(10) # 1-Argument  
                              t.m1(10,20) # 2-Argument
                              t.m1(10,20,30) # 3-Argument
                              t.m1(10,20,30,40) # 4-Argument
                              t.m1(10,20,30,40,50,60,70) # 7-Argument
                              
                              
                         Ex 2:  class Test:              # Internally args ==> tuple
                                    def m1(self,*args):  # Variable length argument 
                                        self.sum=0
                                        print("variable length argument")
                                        self.sum=sum(args)
                                        print("Sum =",self.sum)                        
                                t=Test()
                                t.m1()    # Sum = 0              
                                t.m1(10)  # Sum = 10
                                t.m1(10,20)  # Sum = 30
                                t.m1(10,20,30) # Sum = 60
                                t.m1(10,20,30,40) # Sum = 100
                                t.m1(10,20,30,40,50,60,70) # Sum = 280

                   3) Constructor Overloading :
             'NOTE' # Supported in java
             'NOTE' # Not supported in Python, bcoz its is a dynamically typed language ie. In python we cant define the type explicitly...
                   if u try to implement constructors with same name but different arguments, than last copy will be consider while calling..
                   
                   # Same as method overloading:
                   but, we can implement same fuctionality using default arguments and variable length arguments..
                   
      "VVII"       -> How to define a constructor with variable number of argument:
                       
                       1) Using Default arguments :  
                       
                       # Only for three argument
                        class Test:
                                def __init__(self,a=None,b=None,c=None):  # Default Value
                                        print("Constructor with 0/1/2/3 nos. of argument/s ")
         
                        t=Test() # Constructor with 0/1/2/3 nos. of argument/s 
                        t=Test(10) # Constructor with 0/1/2/3 nos. of argument/s 
                        t=Test(10,20) # Constructor with 0/1/2/3 nos. of argument/s 
                        t=Test(10,20,30) # Constructor with 0/1/2/3 nos. of argument/s 
                       
                       
                       2) Using Variable length argument :
                       # For any no. of argument
                       class Test:
                                def __init__(self,*args):  # Default Value
                                        print("Constructor with variable no. of arguments ")
         
                        t=Test() # Constructor with variable no. of arguments
                        t=Test(10,20,30,40,50,60) # Constructor with variable no. of arguments
                        t=Test(10,20,10,20,30,30,10) # Constructor with variable no. of arguments
                        t=Test(10,20,30,40,50)# Constructor with variable no. of arguments
  
   
   # NOTE:
   |---------------------------|------------------------------|---------------|  
   |                           |              Python          |    Java       |
   |---------------------------|------------------------------|---------------|                  
   | 1)Operator Overloading    |     Supported                | Not supported |
   |                           |                              |               |
   | 2) Method Overloading     |  NOT                         |  supported    |
   |                           |( but can be implemented using|               |          |
   |                           | default or variable length   |               |
   |                           |   argument)                  |               | 
   |                           |                              |               |
   | 3)Constructor Overloading |   NOT                        |  supported    | 
   |                           |                              |               |  
   |---------------------------|------------------------------|---------------|                                      
  

 3) Overriding : -> if child is not satisfied/happy with the parent method , then child can redefine the same parent method...
                   ie. whatever members present in parent class are by default available to 
                      the child class through inheritance.Sometimes child class may not satisfied with parent class implementation,
                      then child class is allowed to redefine that method based on its requirement.
                   This proccess is called overriding.
                 -> It is applicable for methods and constructors  
                 -> 1) Method Overriding:
                 Ex:
                     class Parent:
                            def property(self):
                                print('Land+Gold+Cash+Power')
                            def Marry(self):    # Parent wants his child to marry Appalamma
                                print('Appalamma')
                     class Child(Parent):# Single Inheritance
                            def Marry(self):  # Method overriding 
                                ## super().Marry() # to call Marry() of parent class from child method
                                print('Katrina Kaif ') # But, child wants to redine parent method as, he is not statified with parent method
                     c=Child()
                     c.property() # Land+Gold+Cash+Power
                     c.Marry() # Katrina Kaif 
                   
                ##Note : To access parent method from child class method , we use super().Marry() in child method 
             
                   
                   2) Constructor Overriding : Parent class constructor is by default available to child class
                                               but, if child is not satisfied with parent class constructor , than child can redefine it..
                                              Ex:
                                                  class Parent:
                                                        def __init__(self):
                                                            print(" Parent Constructor")
                                                  class Child(Parent):
                                                        def __init__(self): # Constructor Overriding
                                                            print(" Child Constructor")
                                                  c=Child() # Child Constructor
                                                           
 
 
 # VVI
 4) Abstraction(In gendral term) : Something which does not have completeness (Abstract) or just ' Outline '
 
    # NOTE :
    Abstraction(In OOPs term) : hiding the internal implementaion and 
    ('Covered in point no 7')   just highlighting or displaying the functionality to the end users.. 
    
       1) Abstract Method
       2) Abstract Class
       3) Interface : # syntaxtically not there in python ;but same functionality can be implemented
                      # LIke in java, it has interface keyword , but in python there is nothing like that
 
                1) Abstract Method : Method which has declaration but does not have implementation(ie. empty implementation using pass )  (not has completeness)
                                   -> ie. Sometimes we dont know about implementation, still we can declare a method.
                                          Such typre to methods are called abstract method. 
                                       => abstract method has only declaration but not implementation(ie. empty implementation)
                                   
                   "IMP" Declaration -> declared using ' @abstractmethod ' decorator which is present in ' abc module'
                                   -> Hence, compusary we should 'import abc ' module
                                   
                                   Ex:  
                                         from abc import abstractmethod
                                         class vehicle:
                                                @abstractmethod
                                                def getNoOfWheels(self): # abstract method 
                                                     pass                   # Without knowing vehicle type u can nt return no of wheels
                                                                            # Empty implementation
                                   
                       "VIMP"    -> Child classes are responsible to provide implementation for parent class abstract method ....
                                 
                                 -> abstract method implementaion is given by child class...
                                    and its it compulsary to give implementation to abstract class by child class..
                                 -> Abstarct methods acts as a guideline to the child class ie. which methods are compulsarory to be implemented)
                                        
                       'NOTE:'   -> If parent method is abstract , compulsaory child have to give implemenation
                                 -> And if, parent method is not abstarct then its not compulsory for child to implement that method.
                                 
                               Ex: from abc import ABC,abstractclass
                                   class Vehicle(ABC): # abstract class
                                         @abstractmethod
                                         def getNoOfWheels(self): # Abstract method
                                                pass
                                   class Bus(Vehicle): # Must have Implementaion of getNoOfWheels() abstract method
                                        pass
                                   
                                   b=Bus()  # TypeError : child class Bus , Must have Implementaion of getNoOfWheels() abstract method
                       
                2) Abstract Class : Partially implemented class ..
                                    ie.sometimes implementation of a class is not complete,
                                       such type of partially implemented classes are called Abstract classes.
                        
                      #  Abstract class defines abstract methods...
                      # Anstarct class can contain both abstract method and non-abstract method.
                       
                        Abstract class ==> Partially implemented class .
                        Concrete class ==> Completely implemented class / complete class.
                        
                   "NOTE"      -> We cant create object for abstract class with atleast one abstract method.. (as it is partially implemented) 
                               
                               -> we can also create abstract class with no abstract method.
                                
                               
                  'NOTE: VVI'  -> 'Every abstract class in python should be child class of ABC(Abstract Base Class) class',
                                  which is present in abc module.
                                   ABC => Abstract Base Class 
                   Declaration ->  Abstract class must be child of 'ABC class' present in abc module 
                               Example:
                           #Every abstract class is child class of ABC class     
                           from abc import ABC,abstractmethod
                           class Vehicle(ABC):# Abstract Class
                                @abstractmethod
                                def getNoOfWheels(self):
                                    pass
                                
                     'NOTE' -> Child classes are responsible to provide implementation for parent class abstract method.
                            
                     "VVI NOTE" : Each child class has to compulsary ,implement abstact method of parent class 
                     
                     Example: #NOTE: U can create object of abstract class
                     
                               from abc import ABC,abstractmethod
                               class Vehicle(ABC):   # Abstract class
                                    @abstractmethod
                                    def getNoOfWheels(self): # Abstract Method : method with
                                        pass                 # child will be responsiable for implementation
                              
                               class Bus(Vehicle): # Concrete class: completly implemented class
                                     def getNoofWheels(self): # Complete implementation of abstact method
                                         return 6   
                               
                               class Auto(Vehicle): # Concrete class
                                    def getNoOfWheels(self):
                                        return 3
                                      
                               b=Bus()
                               print(b.getNoOfWheels) # 6
                               a=Auto()
                               print(a.getNoOfWheels) # 3
                               
                               
                  'VVI NOTE' -> IF A CLASS CONTAINS AT LEAST ONE ABSTRACT METHOD AND IF WE ARE EXTENDING ABC CLASS THEN
                                INSTANTIATION IS NOT POSSIBLE.(IE. OBJECT CREATION IS NOT ALLOWED)
                                
                            " FOR ABSTRACT CLASS WITH ABSTRACT METHODS, INSTANTIATION IS NOT POSSIBLE"
                
 #  VVVI example :
 
               from abc import * 
               class CollegeAutomation(ABC): # Interface --> Prototype of  Requirement Specification 
                    @abstractmethod          # Can not create object for CollegeAutomation()
                    def m1(self):pass
                    @abstractmethod
                    def m2(self):pass
                    @abstractmethod
                    def m3(self):pass
                
                class AbsClass(CollegeAutomation):  # Abstract class  --> Partial Implementation
                    def m1(self):                   # Can not create object for AbsClass() as, m3 is not implemented
                        print(' m1 method')
                    def m2(self):
                        print(' m2 method')
                        
                class ConcreteClass(AbsClass): # Concrete class  ---> Complete Implementaion
                     def m3(self):             # m1() and m2() inherited from AbsClass
                         print("m3 method")    # object can be created as all methods are implemented

                c=ConcreteClass() # object created
                c.m1()
                c.m2()
                c.m3()
                a=AbsClass() # Error: Can not create object for AbsClass() as, m3 is not implemented
                b=CollegeAutomation() # Error: Can not create object for CollegeAutomation(),as it has only abstract methd
                                        # case : abstract class with only abstarct methon ==> interface
                
###############################################################################################################
   # VVIMP :          
  "FAQs" :
           Q1) What is abstract method ?
           ->  The method which has only declaration but not implementation
               (ie. empty implementaion)           
  
           Q2) How to declare abstact method ?
           -> By using @abstractmethod decorator , which is present in abc module
           
           Q3) What is abstarct class ?
           -> partially implemented class
           
           Q4) How to declare abstract class in python ?
           ->  The class should be child class ABC
           
           Q5) Who is reponsible to provide implementaion for abstarct methods ?
           -> child classes are responsible to provide implementaion for parent class abstarct methods
           
   "IMP"   Q6) What is the advantage of declaring abstract methods in parent class ?
           ->  By declaring abstract methods in parent class we can provide guidelines to the child classes,
                such that which methods compulsary they should implement.
           Ex: 
               from abc import ABC,abstract
               class Vehicle(ABC):
                    @abstractmethod
                    def getNoofWheels(self):
                        pass
               class Bus(Vehicle): # Must have parent class abstact method implemenation
                    pass           # ie, getNoofWheels() not been implemented in child class

                b=Bus() # TypeError : child class Bus , Must have parent class abstact method implemenation
                        # ie. getNoofWheels() not been implemented in child class
                        
                        
    
  
 """ IMP """ 
    " MOST IMPORTANT CONCLUSION OF ABSTRACT CLASS AND ABSTRACT METHOD "  

   1) If A Class Contains At Least One Abstract Method And If We Are Extending Abc Class Then
      Instantiation Is Not Possible.(Ie. Object Creation Is Not Allowed)
                                
      " For Abstract Class With Abstract Methods, Instantiation IS NOT POSSIBLE"
      
        Case 1:  # Concrete class or  NOT a abstarct class and has NO abstract methods )
                class Test: # Not a abstarct class 
                    pass
                t=Test()     # Vaild    
    
        Case 2: # Abstract class with no abstract method
                from abc import *
                class Test(ABC):
                    pass
                t=Test() # Vaild 

        Case 3: # Abstract class with abstract method
                from abc import *
                class Test(ABC):
                    @abstractmethod
                    def m1(self):
                        pass
                t=Test() # InVaild : TypeError
            
        Case 4: # Not a abstract class but has abstract method
                from abc import *
                class Test:
                    @abstractmethod
                    def m1(self):
                        pass
                t=Test() # valid
    
    
    2) If we are craeting child class for abstract class,then for every abstract method of parent class 
       compulsory we should provide implementation in the child class , otherwise child class is also
       abstract and we can not create object for child class..
       
        Case 1: # Abstract class with 1 abstract method but not implemented in child class
                from abc import *
                class Test(ABC):
                    @abstractmethod
                    def m1(self):
                        pass
                class SubTest(Test): # Not provided implementation for the abstract method (m1())
                        pass
                s=SubTest() # Error : child class Subtest , not contain implementation for the abstract method (m1()) of parent abstract class
        
        Case 2: # Abstract class with 2 abstract method but only one abstarct method is implemented in child class
                from abc import *
                class Test(ABC):
                    @abstractmethod
                    def m1(self):
                        pass
                    @abstractmethod
                    def m2(self):
                        pass
                class SubTest(Test): # Not provided implementation for the second abstract method (m2())
                       def m1(self):
                          print("m1 method")
                s=SubTest() # Error : child class Subtest , not contain implementation for the second abstract method (m2()) of parent abstract class
                s.m1()
                
        Case 3:  # Abstract class with 2 abstract method and all  abstarct method has been implemented in child class
                from abc import *
                class Test(ABC):
                    @abstractmethod
                    def m1(self):
                        pass
                    @abstractmethod
                    def m2(self):
                        pass
                class SubTest(Test): 
                       def m1(self):
                          print("m1 method implementaion")
                       def m2(self):
                          print("m2 method implementaion")
                s=SubTest()  # Vaild
                s.m1()  # m1 method implementaio
                s.m2()  # m2 method implementaio
                
        Case 4 :   #  Abstract class with one both non-abstract method and abstract method
                from abc import *
                class Test(ABC):
                    def m1(self): # Instance method /  non-abstract method
                        print("Non-Abstract method")
                    @abstractmethod
                    def m2(self):
                        pass
                class SubTest(Test): 
                       def m2(self):
                          print("m2 method implementaion")
                s=SubTest()  # Vaild
                s.m1()  #  Non-Abstract method
                s.m2()  #  m2 method implementaion
       
    
            Q.  Is a class can contain both abstract and non-abstract methods ?
            ->  Yes, but child class is responsible for abstract method implementaion.
                If a class contains both abstract and non-abstract methods then child class is responsible
                to provide implementaion only for abstract methods.

       
###############################################################################################################

          3) Interface : An Abstract class which has only abstract method.
          # syntaxtically not there in python ;but same functionality can be implemented
         # Like in java, it has interface keyword , but in python there is nothing like that
  # In java there is interface keyword, but in python we have do it explicity by declaring only abstract methods in abstract class
           
                    -> An abstract class can contains both abstract and non-abstract methods.
                    
            'IMP'   -> If an abstract class contains only abstract methods,such type of abstract class is nothing but interface.

                    -> 100% pure abstract class is nothing but interface.
                    
           "VVI"    -> interface acts as a prototype of requirement specification for implementing a system.
                        
       #IMP             
     "VVIMP" What is the purpose of interface ?
            ->  Interface acts as ' Service Requirement Specification'.  

            For example : A client requires a college automation system
                          with the following requirements
                        So, the interface acts as a prototype of requirement specification for implementing college automation system. 
                          like,
                          getMarks() ==> m1()
                          getStudentAttendance() ===> m2
                          getFeeInfo() ===> m3
                          
                 To show these specifications we can create a abstract class with all these methods as abstract methods\
                  which will be called as an interface..
                  
               Ex:  # Interface
                    from abc import * 
                    class CollegeAutomation(ABC):  # Abstract class with only abstract methods
                        @abstractmethod            # Prototype for requirement specification
                        def m1():
                            pass
                        @abstractmethod
                        def m2():
                            pass
                        @abstractmethod
                        def m3():
                            pass
                            
                   So, this is the Interface , and  the implementation part can be distributed to other people
                 like some company durgasoft , ss,etc wants to give implementaion to the interface..
                
                which can be like..
                
                    class DurgaSoftImpl(CollegeAutomation):
                            """ Implementation to CollegeAutomation """
                            def m1(self):
                                print("m1 method")
                            def m2(self):
                                print("m2 method")
                            def m3(self):
                                print("m3 method")
                 
                    d=DurgaSoftImpl()
                    d.m1()
                    d.m2()
                    d.m3()
                 
     # VVI : 
     Example:    
              from abc import * 
               class CollegeAutomation(ABC): # Interface --> Prototype of  Requirement Specification 
                    @abstractmethod          # Can not create object for CollegeAutomation()
                    def m1(self):pass
                    @abstractmethod
                    def m2(self):pass
                    @abstractmethod
                    def m3(self):pass
                
                class AbsClass(CollegeAutomation):  # Abstract class  --> Partial Implementation
                    def m1(self):                   # Can not create object for AbsClass() as, m3 is not implemented
                        print(' m1 method')
                    def m2(self):
                        print(' m2 method')
                        
                class ConcreteClass(AbsClass): # Concrete class  ---> Complete Implementaion
                     def m3(self):             # m1() and m2() inherited from AbsClass
                         print("m3 method")    # object can be created as all methods are implemented

                c=ConcreteClass() # object created
                c.m1()
                c.m2()
                c.m3()
                a=AbsClass() # Error: Can not create object for AbsClass() as, m3 is not implemented
                b=CollegeAutomation() # Error: Can not create object for CollegeAutomation(),as it has only abstract methd
                                        # case : abstract class with only abstarct methon ==> interface
      
      

 # VVVI : Interface vs  Abstract Class vs Concrete Class
 
       example: If i want to build 1000 floor apartment...
               for that ,first i will call an architect who will give me a plan(like a prototype)
               plan never talks about the implementaion...
               Then i will go to a builder and show  him the plan based on that he will give me the time require to bulid
               it.. suppose it is 5 years...
               
               So,
               
               Interface ======>    plan (5 years)
  (Never talks about implement)       |
                |                     |
                |                     |
                +                     +
         Abstract Class =====>     Partially (After 2 years -300 floors completed)
                |                  completed
                |                     |
                |                     |
                |                     |
                +                     +
         Concrete class ====>     Fully completed
                                (1000 floors completed) 
                         
      
     #     Interface vs  Abstract Class vs Concrete Class

        1) If we do dont know anything about implementation and just we requirement specification
           then we should go for ' interface ' .
           (" SRS - Service Requirement Specification ")
        
        2) If we are talking about implementation but not completely 
           then we should go for ' abstract class '.
           (' Partially implemented class')
         
             
        3) If we are talking about implementaion completely and ready to provide services
           then we should go for ' concrete class '.
            ( " Fully implemented class ")
            
  # VVVI    
    Example :  from abc import * 
               class CollegeAutomation(ABC): # Interface --> Prototype of  Requirement Specification 
                    @abstractmethod          # Can not create object for CollegeAutomation()
                    def m1(self):pass
                    @abstractmethod
                    def m2(self):pass
                    @abstractmethod
                    def m3(self):pass
                
                class AbsClass(CollegeAutomation):  # Abstract class  --> Partial Implementation
                    def m1(self):                   # Can not create object for AbsClass() as, m3 is not implemented
                        print(' m1 method')
                    def m2(self):
                        print(' m2 method')
                        
                class ConcreteClass(AbsClass): # Concrete class  ---> Complete Implementaion
                     def m3(self):             # m1() and m2() inherited from AbsClass
                         print("m3 method")    # object can be created as all methods are implemented

                c=ConcreteClass() # object created
                c.m1()
                c.m2()
                c.m3()
                a=AbsClass() # Error: Can not create object for AbsClass() as, m3 is not implemented
                b=CollegeAutomation() # Error: Can not create object for CollegeAutomation(),as it has only abstract method
                                        # case : abstract class with only abstarct methon ==> interface
                
                
########################################################################################################################################                
                
   
  #  VVVI : 
  
  5) Public , Private , Protected :  # Just naming conventions
  
                  x=10 ===> Public
                __x=10 ===> Private
                 _x=10 ===> Protected
                 
                 
             1) Public members : ' Members accessable throughout the program '. ie. within the class and outside the class aswell
             
                -> If a member (either method or variable) is public, then we can access that member from anywhere 
                    either within the class or outside of the class .
                 
                -> ' Members accessable within the class and outside the class aswell.'
                
                -> By default every member present in python class is public.
                    Hence we can access from anywhere either within the class or from outside the class
                
                Example :
                        class Test :
                                def __init__(self):
                                    self.x=10           # Public variable: by default
                                def m1(self):           # Public method: by default
                                    print("Public method")
                                def m2(self):
                                    print(self.x)  # accesssing public variable within the class
                                    self.m1()      # accesssing public method within the class
                        t=Test()
                        t.m2()  # 10 Public method
                        # Accessing outside the class
                        print(t.x) # 10
                        t.m1()    # Public method
                        
                       
                                    
              2)   Private Members : ' Members accessable within the class only '
        ( prefix with 2 underscore: __x,__m1() )
                   
                    -> If a member is private then we can access that member only within the class 
                       and from outside the class we can not access.
                     
             'NOTE' -> We can declare a member as private explicitly by prefixing with two underscore symbols.
             
                 Example:
                            class Test:
                                def __init__(self):
                                    self.__x=10    # Private Variable : Accessable within the class
                                def __m1(self):    # Private method : Accessable within the class
                                    print("Private method")
                                def m2(self): # Public method : can be call from outside the class
                                    print(self.__x) # Accessing within the class :private
                                    self.__m1()
                            t=Test()
                            t.m2() # 10 Private method
                            print(t.__x) # AttributeError : 'Test' object has no attribute '__x'..as Private members not accessable outside the class
                            t.__m1()  # AttributeError : Test' object has no attribute '__m1()'..as Private members not accessable outside the class
             
            
            # VVVI:
            'NOTE' -> By default, private members outside the class are not accessable..
   "VVVVI"      """ But there is a hidden way to access private members outside the class """
                 ## But, Most of the time we dont do it  
              
      "Note" -> Internally in python for private members, ' Name mangling ' concept is applied..
               ie. for every private member python ,internally ' Name mangling ' will happen..
               
               'Name Mangling' ==> Every private member name will be converted into a new name
              
'VVI NOTE'  ->  private members Name will be changed to ==> _ClassName__VariableName
'VVI NOTE'   -> Hence , we can access private variable from outside of the class as,
               print(objectreferance._ClassName__VariableName)
    
             for example :
             
  'NOTE'     __x ==> _Test__x ==> this new name will be allocated to __x ..
             __m1() ==> _Test__m1()
             
            therefore, while acccessing t.__x ==> it was throwing AttributeError as: 'Test' object has no attribute '__x'  
             
            So, new name for __x is _Test__x
            
          -> So, using this name you can access private members , even outside the class
              ( _Test__x )   using the concept of 'Name Mangling'
    
       Ex:  # Acessing private members from outside the class ; but most of thime we dont do it..
            class Test:
                def __init__(self):
                    self.__x=10    # Private Variable 
                def __m1(self):    # Private method 
                    print("Private method")
                t=Test()
                print(t._Test__x) # 10 ## objectreferance._ClassName__VariableName 
                t._Test__m1() # Private method 
       
       
       
       
       
              3) Protected class : Members can be accessed inside the class and only in child class 
                    ( _x=10 )    
                              'NOTE' # But 'IN python' if we try to access protected members outside the class , it will show the same result.
                  'VVVVVVI' :  -> But it is just naming convention and it is not implemented in python
                                  , may be implemented in future versions                                
                  
    'VVVVI'  # Protected , in pyhton is not implemented internally, it is just a naming convention ( _x )
                    # SO , you can access from anywhere 
                    
                  # vvi..NOTE : Protected is just naming convention ( _x) , 
                              # internally in python it is not implemented
                    
                               -> protected members we can access within the class from anywhere 
                                  but from outside of the class we can access only in child classes.
                               
                               -> We can declare members as protected explicity 
                                  by prefixing with one underscore symbol. 
                
                #  x=10   ===> Public 
                # __x=10  ===> Private
                #  _x=10  ===> Protected 
                
         Example :          
         
                    class Test:
                            def __init__(self):
                               self._x=10         # Protected
                            def m1(self):
                               print(self._x)     # Accessing _x within the class
                    class SubTest(Test):       # Child of Test Class
                            def m2(self):
                                print(self._x)    # Accessing _x in its child class
                    t=SubTest()
                    t.m1()  # 10
                    t.m2()  # 10
                    # Accessing outside the class
                    print(t._x) # 10 , becoz In Python Protected is not implemented internally
                                # It is just the naming convention to write protected members as prefixing one _        
                
                
                
                
  

 6) Data hiding : End user should not access the internal data directly..
                  End user must go through the validation/Authentication to access the data...
                  
                -> Hidding internal data from end user such that he can not access it directly..
                   Must go through the validation/authencation before accessing it..
            
         'NOTE'   -> By declaring data members as 'private', we can implement Data Hiding..
                  
                  Ex: 
                      1) Gmail:  End user must go through authentication for accessing mail\
                     
                      2) Bank :  Validation of user is require for a accessing account  for withdral or anything..
                  
                  Example:
                     
                      class Acccount:
                            def __init__(self,intial_balance):
                                self.__balance=intial_balance   # Private variable
                            # Accessing private members using Method
                            def getBalance(self):
                                # validation/Authentication part/code
                                return self.__balance # return if authencation is successful
                      a=Account(10000)
                      # print(a.__balance) ## error ; private members cant be accessed from outside the class
                      # Must be accessed , by calling method
                      print(a.getBalance()) # 10000
                  -> Our internal data should not go out directly.
                     ie. Outside person should not access our internal data directly.
                  
                  ->  Advantage of Data Hiding : Security 


                    
                  

  
   
   # VVVI:                            
 7) Abstraction: In OOPs, Abstraction means hiding the internal implementaion 
                 and just highlighting or displaying the functionalities to the end user..
                 
              -> Hiding internal implementation and 
                 just highlighting the set of services is the concept of abstraction      
                 
 'NOTE IMP'   Example 1: Through Bank ATM GUI screen, bank people are highlighting the set of services what they are offering 
                         without highlighting internal implementation.
                         Thid is nothing but abstraction.
                         
  "VVVIMP"    -> # How to implement Abstraction :
                   by using GUI screens, APIs we can implement abstraction.  
                  
            For Example : for web devleoper after python( djanjo + Rest API have to learn)
                        ->  Suppose ,we devleoped a django web application for jobs 'Durga Jobs'..
                        ->  Now, this web application can be used directly by the end user
                            (by opening the brower and search for www.durgajobs.com )
                          
                        -> Assume , that a android application wants to send a request to our django application 
                            and this android application is responsible to display jobs..
                            
                       --> Both application is complete diffrent one is django and other is android application     
                       --> So, Android application wants to communicate with django application..
                          so, these android people not require to aware django concepts ...
                          which brings in API in the middle..                           
                       -> So, Android application is sending GET request to API, then in API internally some method(GET method) is going to be executing..
                          which is reponsible for providing complete job information..
                       -> Now,Android application providing POST request to the API, then in API internally some POST method is goin to be execute..
                          which is responsible for creating job..                       
                       -> Here, Django application is responsible for maintaining complete job information 
                          , and just android application with the help of django is displaying job information..
                          and POST new job application ..
                       -> This is how this android application will communicate with this django application with the help of API ..
                       -> Conclusion  : Been android devleoper internally what is happing is not your job
                                        (ie. highlight the set of services what we are offering in your android application)
                       -> this is abstraction...

                                                                                                  
                    O         -----------------    GET Request      |-------------|       |------------------|                    O
                    |------>  |Display Jobs   |   -------------->   |             |--->   |                  |                    |    
                    |         |(Android)      |   POST Request      | GET method  |       |  Django          |   <------------    |                        
                   / \        | (Application) |  -------------->    |             |--->   |  Web Application |                   / \                  
                 End User     |----------------                     |             |       | ( Durga Jobs)    |                 End User          
               (Android User)                                       | POST method |       |------------------|                (Browser User)            
            [Android use will]                                      |-------------|                             (Browser userwill access web application directly)
          access django application                                     ' API '                                             (By open brower 'www.durgajobs.com')




                       
                        
    
    'IMP'     -> Advantages :
                  
                     1) Security
                     2) Enhancement will become very easy (any change wound not effect the end user)
                     3) Maintainablity and Modularity of the application
 
 
 
 
 
 
 
 
 
################################################################################################
 
    # Abstraction vs Data Hiding 
    
    Abstraction : Hiding internal implementation and 
                  just highlighting or showing fuctionalities to the end user..
    
    
    Data Hiding : Hiding internal data from end user 
                  such that he can not access the directly...
                  he must go through the authentication first for accessing ... 
 
 
 
########################################################################################################
 
 
 
 # VVI
 8) Encapsulation : Wrapping of data and its corresponding method into a single unit..
                    This proccess is called Encapsulation.
    
                  -> The process of Binding/Grouping/encapsulating data 
                     and corresponding  behaviour(method) into a single unit
                     is nothing but encapsulation..
                     
                  -> Ex: Class
                        ( Every python class is an example of enncapsulation)
          ' VVI ' -> Hiding data behind methods is the central concept of encapsulation..  
 
     "NOTE"       -> If any component follows data hiding and abstraction, 
                     such component is said to be encapsulated component.
                            
                       ' Encapsulation = Data Hiding + Abstraction '         
 
                  Example : Has ' Abstarction' and 'Data Hiding'..
                    
                   class Account:
                        def __init__(self,initial_balance):
                            self.__balance=initial_balance
                        def getBalance(self):
                            # validation/Authentication code
                            return self.__balance # return if authentication is successful
                        def deposite(self,amount):
                            #validation/Authentication
                            self.__balance=self.__balance + amount
                        def withdraw(self,amount):
                            #validation/Authentication
                            self.__balance=self.__balance - amount
                    
                    
                    'Abstraction' => End user screen  (GUI) highlighting functionalities like deposite withdraw method 
                    'Data hiding '=>private members  
                    ' Encapsulation = Data Hiding + Abstraction '    
 
            ' VVI ' -> Hiding data behind methods is the central concept of encapsulation..
 
           " IMP "  -> Advantages of encapsulation :
                        
                        1) Security
                        
                        2) Enhancement will become easy
                        
                        3) Maintainablity and Modularity will be improved
                
              #### IMP NOTE :

                1) The main advantage of encapsulation is security.
                        
                2) The main limitaion of encapsulation is it increase the length of the code
                   and slows down executing(Due to authentication factors)..
                   We should compromise with performance.
                   
              'NOTE' ->  If we want security we should compromise with performance
                     ->  If we want performance we should compromise with security..
                     
                     
                


############################################################################################################################################################################
 
                   
                   
                                                                # The Three Pillars of OOPs
                 

                 
                                                                 |--------------------|
                                                                 |  'Inheritance'     |
                                                                 |single,multiple,    |
                                                                 |multi-level,hybrid  |
                                                                 |heirarical ,cyclic  | 
                                                                 |--------------------|  
                                                                          ^  'Main Advantage'
                                                                          |  Code Reuseablity 
                                                                          |  and Extendablity
                                      'Main Advantage'                    |
                 |-----------------|     Security             ************************                            |-----------------|                                                                                                                       
                 | 'Encapsulation' |                          *                      *                            |  'Polymorphism' |    
                 |  (Abstraction,  |  <---------------------- *  3 pillers of OOPs   * ----------------------->   |  (Overriding,   |                                                                                                 
                 |   Data Hiding)  |                          *                      *                            |   Overloading)  |                          
                 |                 |                          ************************          'Main Advantage'  |                 |
                 |-----------------|                                                               Flexibilty     |-----------------|     
                                                                                               (same method name,but diffrent implentation
                                                                                                in parent class and child class ie. overloading )                      
                                                                                                                     

                   
################################################################################################################################################################################
                   
                   
                   