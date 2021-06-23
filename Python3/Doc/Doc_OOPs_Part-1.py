
######################################################### OOPs PART-1 ############################################################

1) 3 Important terms used in OOPs :
    1) class : Blueprint/template of a object , represents which properties and action its can perform.
    2) object : A Instance of a class or physical significance of class
    3) reference variable : A variable , which can refer object. Using reference variable , we can perform required operation on an object.
                            Can access properties and method of object.
    
    
2) class Class_Name:
        """ Doc String """
        # variable inside a class // data members
        # functions inside a class // Methods
     
  Note:  To access Doc string of a class : 
        
        1st Way:
        print( Class_Name.__doc__ )  # Doc String
        
        2nd way:
        help( Class_Name ) # Gives Complete documentation of the class
   
   # Example of class:
    class Student:
    """ Doc String """
    def __init__(self):
        self.name='pankaj'
        self.rollno='108'
    def disp(self):
        print(self.name,self.rollno)
        
    reference_variable=Student()  # Object is been created with a refference variable
    reference_variable.disp()



   
        " VIMP "        
3) Type of variables allowed in python class : # covered in point no. 6 
    1) Instance variables( Object level variables)
    2) Static variables(class level variables)
    3) Local variables(method level variables )
    
4) Type of methods allowed in python class :
    1) Instance methods
    2) class methods
    3) Static methods 
    
5) Everything about " self variable " :
   
   -> "self variable " : A reference variable which points to current object within the class. # Note: self is the only variable which points to current object
   -> Value to self is provided automatically by the python interpreter .
   # VVI
   ->" self " variable is accessable only within the class , outside the class we have refference variable....
                      #  To access object within the class , we use self variable( instance variable ), 
                      #  outside of class , we use refference variable to access the object 
   
   Ex 1: class Test:
            def __init__(self):
                print(" Address of object pointing by self",id(self))
         t=Test() # Here, t is the referance variable pointing to the object outside the class
         print(" Address of object pointing by t",id(self))
        
        # O/P -> Address of object pointing by self 3006563515360
        #        Address of object pointing by t 3006563515360
    
   Conclusion : " Note"  Both the reference Variable "self" and "t" points to same object , 
                         only "self " is defined inside the class and " t " is defined outside the class. 
                
                
    Ex 2 :  class Test:
                def  __init__(self): # Constructor : 1st argument is always self
                    print(" Constructor ")
                def m1(self,x):  # Instace Method : 1st argument is always self 
                    print(" Value of x:",x)
            t=Test()
            t.m1(10)
              
            # O/P -> Constructor
            #        Value of x: 10
            
    Ex 3:class Student:
            def __init__(self,name,roll_no):# name,roll_no , local variable only this block can access
                self.name=name   # self.name --> Instance variable(Object level variable),which will be stored inside the s1 object...                           
                self.roll_no=roll_no#            Now only self variable can access name,roll_no in other methods as,roll_no and name are local to __init__
            def disp(self):
                print("Name:",self.name)
                print("Roll No. :",self.roll_no)
         s1=Student('Pankaj',108)
         s1.disp()
         
         # O/P -> Name:Pankaj 
         #        Roll No. : 108
        
    -> Conclusion: 1) 1st argument to " Constructor " and " Instance Method " is always " self variable"
                   2) Constructor(__init__(self)) is called automatically,when an object is been created.
                   3) " Constructor " are used to initialize the " instance variable(Object level variable)" 
                   4) "self variable" are used to declare " instance variable(Object level variable) " and to access " instance variable "
         " Note" : 5) " self " is " not " a keyword,insted of self we can write any name like delf,kelf anything ...but recommended is self as a name to identifier
         " IMP "   6) 1st Argument always points to current object ,no matter whether we name it as self,delf,anything........Recommended self
                      1st Argument(self) is also called as implicite variable......
         " VVVVVI" 7) " self " variable is accessable only within the class , outside the class we have refference variable....
                      #  To access object within the class , w use self variable( instance variable ), 
                      #  outside of class , we use refference variable to access the object        
                   8) We cant use " self " outside of the class
         Ex : class Student:
                def __init__(delf,name,roll_no): # 1st argument is always points to current object, we can name it anything self,delf,kelf,abc 
                  delf.name=name                              
                  delf.roll_no=roll_no
                def disp(kelf):  # 1st argument is self only only name here is different
                  print("Name:",kelf.name)
                  print("Roll No. :",kelf.roll_no)
              s1=Student('Pankaj',108)
              s1.disp()
              # O/P -> Name:Pankaj 
              #        Roll No. : 108
  
   
-> Constructor ( __init__ ) : -> Special method in python
                              -> Always named as ' __init__()'
                            -> Used to initialize the instance variable..
                            -> Must have atleast one argument 'self' 
                    NOTE :  ->  Constructor is called automatically ,when an object is been created...
                    "IMP"   -> U can also call constructor(__init__(self)) explicitly... like normal method
                        Ex: class Test:
                                def __init__(self):
                                    print("Constructor executing")
                            t1=Test() #Automatic call to constructor
                            t1.__init__() # Explicite call to constructor
                            t1.__init__()
                        # O/P : Constructor executing
                        #       Constructor executing
                        #       Constructor executing
    NOTE:
    " VVI " : Constructor / method overloading not applicable in python.....
            -> Overloading : methods/functions with same name ,but different nos. of arguments...
   
   'VVVI' :
   ''' overloading concept  is not applicable for constructors . Hence,we can't define multiple constructors within the same class....
       And,if we are trying to define multiple constructors, tehn only  the last constructor will be considered   '''
    
    " CONSTRUCTOR OVERLOADING IS NOT APPLICABLE IN PYTHON,IF WE TRY TO DO SO THEN,LAST CONSTRUCTOR WILL BE CONSIDERED"
    
    Ex: class Test:
            def __init__(self):
                pass
            def __init__(self,x):  # Only this constructor will be consider by the PVM....
                print(x)
        t1=Test(10) # Valid : As last one will be considered as constructor 
        t1=Test() # iNVALID : ERROR , constructor takes one argument x ....
 
  
   "IMP" 
6)  Types of variables in python class (instance,static,local) :
     
        1) Instance variable( "Object level variables ") : If the value of a variable is varied from object to object , 
                                                            such type of variables are called instance variable.
                                                           Ex: name , rollno of  students # for every student separate name,roll_no will be there....
      
                                                            class Student:
                                                                def __init__(self,name,roll_no): 
                                                                    self.name=name  # self.name,self.rollno instance variable will be initialize for every object... 
                                                                    self.roll_no=roll_no
                                                                    
                                                         -> For each object, a separate copy of instance variable will be created.
                                                         -> Most of the times, Instance variable will been initialized inside constructor
                                                            by using self .... ex: self.name ,self.rollno
        
        2) Static variable (" class level variable"):  If the value of a variable is not varied from object to object ,
                                                       such type of variables are called static variable.
                                                     Ex : School Name will be same for all students # So,only one copy of school name will be created ,
                                                                                                    #  and it will be shared by all objects.
                                                        class Student:
                                                            school_name='MIT' # Static Variable,(Only one copy of school_name will be shared with all objects)
                                                            def __init__(self,name,roll_no):
                                                                self.name=name
                                                                self.roll_no=roll_no
                                                     
                                                    -> In the case of instance variable, for every object a separate copy of instance variable
                                                       will be created ...
                                                       But, In in case of static variable at class level only one copy will be created,
                                                       and shared by every object of that class .
                                                    -> Most of the time , static variables should declared with in the class directly.

        3) Local Variable(" method level variable") : To meet the temporary requirements of the programmer , we need to declare
                                                      variable inside a method, this type of variable is called local variable.
                                                    
                                                    Ex: class Student:
                                                            school_name='MIT' # Static Variable,(Only one copy of school_name will be shared with all objects)
                                                            def __init__(self,name,roll_no):
                                                                self.name=name # Instance variable , for each object separate copy will be there.
                                                                self.roll_no=roll_no # Instance variable
                                                            def info(self):
                                                                x=10  # Local variable (declared inside a method) [method level variable]
                                                                for i in range(10): # i is local variable
                                                                    print(i)
                                                                    
                                                                    
                                                                  
 7) Types of methods in python class (instance,class,static) : 
 
        1) Instance method : A method , which is accessing instance variable in it.... 
   "When u r using instance variable"  -> Inside a method , if ur trying to access instance variable,
                              then , that method will be called as instance method.
                            -> In instance method, 'first argument' is always 'self'
                            ex: 
                            
                            class Student:
                                school_name='MIT' # Static Variable,(Only one copy of school_name will be shared with all objects)
                                def __init__(self,name,roll_no):
                                    self.name=name
                                    self.roll_no=roll_no
                                def getStudentInfo(self):   # Instance Method , as its accessing instance variable in it
                                    print("Student Name",self.name)
                                    print("Student Roll No",self.roll_no)
                                    
        
        2) class method  : " when u r using static variable"
        
                    "VVIMP" PREREQUISITE -> For, every class python will create a special object "class level object"(class name itself is the object) to hold 
                                           class level information (static variable/class level variable)...
                                           So to refer class level object , 
                                           A reference variable is created , named ' cls '....
                                           -> ' cls ' is the reference variable that refers to class level object(class_name)
                                              like 'self ' refers to current object(Instance level object)
                                              
              "Defination" -> Inside a method , if there are only static variable, no instance variable 
                           therefore, the method is no way realated to a particular object, it is a class level method
                           such types of method we have to declare as class methods..
                    IMP  -> To declare class method , we have to use " @classmethod " decorator
                         -> If a method access static variable(class level variable)
                         -> First argument is always 'cls'
         "Note"  " IMP " -> we have to declare class method with """ @classmethod """ decorator..
                Ex :
                    class Student:
                                school_name='MIT' # Static Variable,(Only one copy of school_name will be shared with all objects)
                                def __init__(self,name,roll_no):
                                    self.name=name
                                    self.roll_no=roll_no
                                def getStudentInfo(self):   # Instance Method , as its accessing instance variable in it
                                    print("Student Name",self.name)
                                    print("Student Roll No",self.roll_no)
                                    
                                @classmethod
                                def getSchoolInfo(cls): # cls ,reference variable pointing to class object,using cls u can access class variable / static variable
                                    print("School Name",cls.school_name) # accessing static variable using cls (class level variable)
                                    
                                    
                # cls and class object(class_name) will have same address
                
                  Ex:  class Test:
                            @classmethod
                            def m1(cls):
                                print(id(cls))
                       print(id(Test)) # class object (class name)
                       Test.m1()
                       
                       
        3) static method : " Gendral method " which will take some argument and may return something...
    ("when u r not using instance and static variable")    -> declared using " @staticmethod " decorator
      " Just like simple function"                        Ex: @staticmethod   
                                                              def getSum(a,b):
                                                                    return a+b
                                                                    
                                                             
        # Example of student class
        
         class Student:
            school_name='MIT' # Static Variable,(Only one copy of school_name will be shared with all objects)
            def __init__(self,name,roll_no):
                self.name=name
                self.roll_no=roll_no
            def getStudentInfo(self):   # Instance Method , as its accessing instance variable in it
                print("Student Name",self.name)
                print("Student Roll No",self.roll_no)
                                    
            @classmethod
            def getSchoolInfo(cls): # cls ,reference variable pointing to class object,using cls u can access class variable / static variable
                print("School Name",cls.school_name) # accessing static variable using cls (class level variable)
                
            @staticmethod
            def getSum(a,b):
                return a+b
                
 8) Various places to declare instance variables:
   
    1) Inside constructor using self :
    
        class Test:
            """ Demo Test class  """
            def __init__(self):
                self.a=10
                self.b=20
        t=Test() # a,b will be added to object (constructor)
        print(t.__dict__) # __dict__  : object dictionary [ contains all instance variable ]
        print(t.__doc__)
        # o/p ->  {'a': 10, 'b': 20}
        #         Demo test class
    
    #Imp
    ## NOTE : to show all instance variable of a object ,we can use object.__dict__
    
    2) Inside instance method using self :
        
       " Note " : here instance variable will be added ,only after the method is been called
    
        class Test:
           def __init__(self):
                self.a=10    # Instance variable
                self.b=20
           def m1(self):
                self.c=30  # Instance variable
        t=Test() # a,b will be added to object
        print(t.__dict__) # O/P -> {'a': 10, 'b': 20} , c will not be there, becoz m1 is not been called yet, but as constructor will be called automatically
        t.m1() # c will be added to object
        print(t.__dict__) # O/P -> {'a': 10, 'b': 20, 'c': 30} 

    3) Outside of the class by using object reference variable : object.variable_name=val
    
        class Test:
           def __init__(self):
                self.a=10    # Instance variable
                self.b=20
           def m1(self):
                self.c=30  # Instance variable
                
        t=Test() # a,b added to the object (constructor)
        t.m1() # c added to the object
        
        t.d=40 # instance variable from outside of  the class
        # d also added to the object 
        
        print(t.__dict__)
        
        # O/P  : {'a': 10, 'b': 20, 'c': 30, 'd': 40}
        
  
  
10)  How to access instance variable :


    1) Inside the class using self :
    
    class Test:
        def __init__(self):
            self.a=10
            self.b=20
        def display(self):
            print(self.a,self.b)
    t=Test()
    t.display() # O/P : 10 20
    
    
    
    


    2) outside the class using reference_variable of object :    
        
    class Test:
        def __init__(self):
            self.a=10
            self.b=20
    t=Test()
    print( t.a , t.b)
    
    
11) How to delete instance variable: 

    1) within the class:   del self.a

    2) outside the class : del objreferance.variable
  
    ex:  del t.a
    
        del t.a,t.b
    
    
    Ex: class Test:
            def __init__(self):
                self.a=10
                self.b=20
                self.c=30
                self.d=40
            def m1(self):
                del self.a
        t=Test()
        print(t.__dict__) # Before deleting instance variable a  ****** O/P : {'a': 10, 'b': 20, 'c': 30, 'd': 40}
        t.m1()
        print(t.__dict__) # Ater deleting 'a'
        
        # O/P ->  {'b': 20, 'c': 30, 'd': 40}
        
        
12) Various places to declare static variables : # using class name or cls( class method)
     ## Note: To show static variable of class  , we use class_name.__dict__   , also it will show some extra class properties
      #  Test.__dict__
    1) Within the class directly , but outside of any method or constructor :
    
        class Test:
            a=10   # Static variable
        print(Test.__dict__)  # static variables + some properties of class object
        
    2) Inside constructor using class name : 
    
       class Test:
            a=10 # static variable
            def __init__(self):
                Test.b=20 # static variable inside constructor using class name
    
    3) Inside instance method using class name :
    
      class Test:
        def m1(self):
            Test.c=30 # Staticc variable in instance method 
            
    4) Inside class method using either cls or class name :
    
    class Test:
        @classmethod
        def m2(cls):
            cls.d=40 # static variable inside class method using cls
            Test.e=50 # using class name
            
    5) Inside static method (gendral method) by using class name :
    
        def Test:
           @staticmethod
           def m3():
              Test.f=60 # ststic variable inside static method (gendral method) using class name
             
    6) Outside of class using class name :
    
        def Test:
            pass
        Test.g=70  #  static variable outside the class using class name

13) How to access static variables : # Using self,class_name,cls, object refference

    1) Inside constructor by using self or class name (Recommended) :
    
        class Test:
            a=10  # Static variable
            def __init__(self):
                print(self.a) # 10   ,accessing static variable inside constructor
                print(Test.a) # 10
                
                
    2) Inside instance method using self or class name :
      
       class Test:
           a=10 # static variable
           def m1(self):
                print(self.a) # 10 , accessing static variable inside instance method
                print(Test.a) # 10
                
    3) Inside class method by using cls or class name :
    
        class Test:
            a=10 # static variable
            @classmethod
            def m2(cls):
                print(cls.a)  # 10 , accessing static variable inside class method
                print(Test.a) # 10
     
     4) Inside static method(gendral method) by using class name :
            
        class Test:
            a=10 # static variable
            @staticmethod
            def m3():
                print(Test.a) # accessing static variable inside static method (gendral method)
                
     5) Outside of class using either object refference or class name :
     
        class Test:
            a=10 # static variable
        t=Test()
        print(t.a) # 10 ,accessing static variable outside of class
        print(Test.a) # 10
        
        
14) How to modify value of static variable: 
    # Only by using class name and cls (for class methods)
    
    class Test:
        a=10 # static variables
        b=20
        c=30
        d=40
        def __init__(self):
            print("Before Modification")
            print("a =",Test.a)
            print("b =",Test.b)
            print("c =",Test.c)
            print("d =",Test.d)
            Test.a=20 # a=20 ,a modified to 20
        @classmethod
        def m1(cls):
            cls.b=30 # b=30
            Test.c=40 # c=40
        @staticmethod
        def display():
            print("After Modification :")
            print("a =",Test.a)
            print("b =",Test.b)
            print("c =",Test.c)
            print("d =",Test.d)
    t=Test()
    Test.d=50 # d=50
    t.m1()
    t.display()
    
15) How to delete static variables:  # Using class name or cls
 
   class Test:
        a=10 # static variables
        def __init__(self):
            self.a=20 # a=20 ,a modified to 20
        @classmethod
        def m1(cls):
            cls.b=30 # b=30
            Test.c=40 # c=40
            del cls.b
    t=Test()
    del Test.a
    print(Test.__dict__)
    print('a' in Test.__dict__ ) # False

  # NOTE :
  """     We can only modify/delete static variable using cls ,class name , 
        But we can access static variable using object reference,self , class name,cls   """
        
     
16) Local variable: # to store temporary result 

    1) Declare directly inside a method/constructor  : # Accessable to that block only
    
        class Test:
            def __init__(self):
                a=10 # Local variable
                print(s)
 15)               
##################################################################################### 
# VVVVVI :
""" Print type or print class name of a object """  
'NOTE' : To print type of a variable:
        -> Two ways :
            1) type() method : 
            
            ex:
                x=10
                print(type(x))  # O/P : <class 'int'>

            2) variable.__class__.__name__ :  
                ex:
                x=10
                print(x.__class__.__name__)  # O/P : int  

            Also, it can be used to find class name ,ie. which object referance refers to which class...                
               Ex: # To print class name of a object using refobject.__class__.__name__ 
                    class Test:
                        pass
                    t=Test()
                    print(t.__class__.__name__) # Test
                    
                    
 ######################################################################################3333  
    
    
