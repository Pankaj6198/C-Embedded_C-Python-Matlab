
######################################################### OOPs PART- 2 ############################################################

1) Instance Method : Inside instance method , if we r using instance variable then that method refers to particular object.
                    -> first argument is always self,which referes to the current object(# Note: self is not a keyword, insted of self it can be delf,elf anything)
           #NOTE    -> Inside instance method we can access instance variable(self.variable) and static variable(class_Name.variable)
           #Note    -> Outside the class, we can access instance method and variables using only object refference
           
           #IMP    -> Using self , to access instance variable within the class
                
                 ex: class Student:
                        def __init__(self,name,roll_no):
                            self.name=name
                            self.roll_no=roll_no
                        def display(self):
                            print("Hi",self.name)
                    s1=Student('Pankaj',108)
                    print(s1.name,s1.roll_no) # Accessing instance variable outside the class using object reference variable
                    s1.display()

# IMP
2)  Examples of instance methods: getter and setter methods

    1) Getter and Setter Methods : To set and get values of instance variables using getter and setter methods.
                                # Fixed syntax in any programming language
                                # Most of the time, IDE are responsible for genrating these method,
                                # examples of instance method 
                             
             1) Setter Method : To set values to the instance variable
                               ->  Also,known as mutator method # Changing method,its going to set/change the values of instance variable
                
                Syntax:  def setVariableName(self,variable):
                            self.variable=variable
                          
                # To set marks of the student
                    Ex:    def setMarks(self,marks): # setter method for marks property
                            self.marks=marks
                            
             2) Getter Method : To get values from instance variable
                               -> Also, known as accessor method .
                 
                 Syntax: def getVariableName(self):
                            return self.variable
                 
                        # To get marks of the student 
                        def getMarks(self): # Only self will be there , no other argument will be there as, we want to get something
                            return self.marks
                 
                # Initiasing instance variable without constructor .. using instance method
             Ex: class Student:
                    def setName(self,name):
                        self.name=name
                    def getName(self):
                        return self.name
                    students=[]
                    for i in range(2):
                        s=Student()
                        name=input("Enter Name:")
                        s.setName(name)
                        students.append(s)
                    for i in students:
                        print("Name:",i.getName())
                     
 3) class method: Only static variables can be used inside class method
                -> declared using @classmethod decorator
                -> first argument is always 'cls'( refers to class level object)
         # NOTE -> Inside class method we can only access static variable(by cls or class_name) , not instance variable
         # NOTE -> Outside class , we can access class method and static variable by using both class_name and object refference\
         
                class Test:
                    a=10
                    @classmethod
                    def m1(cls):
                        print(cls.a)
                        
    Ex: To count no. of objects created
    ->  class Test:
            count=0
            def __init__(self):
                Test.count+=1
            @classmethod
            def getCount(cls):
                print("No. of objects created :",cls.count)
        print(Test.count) # 0
        t1=Test()
        t2=Test()
        t3=Test()
        t4=Test()
        t5=Test()
        print(Test.getCount()) #5 
        
 4) static method(Gendral method):  Inside a method , if we r not using any instance variable and static variable, then such method are called as static method
                                 
                                 -> Used for gendral purpose
                                 -> declared using @staticmethod decorator
                                 -> outside the class ,static method can be accessed using class_name or object referance if its been declared
                                    using decorator only  then...
                                 
                             Ex: class Test:
                                    @staticmethod
                                    def average(x,y):
                                        return (x+y)/2
                                    @staticmethod
                                    def sum(x,y):
                                        return x+y
                                 print(Test.average(10,10))
                                 print(Test.sum(10,10))
                                 print(t.average(10,10))
                                 print(t.sum(10,10))
                                 
  
  """ IMP """
   # VVIMP
 5) If we are not using decorator , then what will be the method ?
   -> # NOTE: for class method, @classmethod is compulsory
   -> # NOTE: for static method , @staticmethod is optional
   
   -> Without , any decorator the method can be instance or static method....
      -> if we are 'calling that method using object referance' , then it will be ' instance method'
      -> And,if call that method using 'class_name', then it will be 'static method' 
      
    Ex: def Test:    # without decorator
            def m(x):# It can be instance method or static method , depending on the call
                pass
        t=Test()
        Test.m(10) # call m() using class_name , m will be considered as a static method
        t.m() # m will be considered as instance method , where x is acting as self
        
 
  "IMP"  
 6) Accessing Members of one class inside other another class : # passing referance object of one class as a argument to static method of another class...

    ex: 
 
 class Employee:
   def __init__(self,eno,ename,esal):
      self.eno=eno
      self.ename=ename
      self.esal=esal
   def display(self):
      print("Employee No. : ",self.eno)
      print("Employee Name : ",self.eno)
      print("Employee Salary. : ",self.eno)
         
 class Manager:#If decorator not mentioned then the method can be either static method or instance method,depends upon how the method is been called(using classname/object ref)
    def updateEmpSal(emp): # static method(gendral method) , emp is the refferance object of Employee class
        emp.esal+=10000 # Accessing esal variable of Employee class using emp object 
        emp.display()   # Accessing display() method of Employee class using emp object
         
         emp=Employee('108','Jason',55000)
         Manager.updateEmpSal(emp)  # static Method(updateEmpSal), as method is been called using class_name(Manager)
         
         
     ### VVIMP   
  7) Inner classes : class inside another class ... 
                    
                -> When we should go for inner classes :  Without existing of one type of object, if there is no chance of existing another object.
                                                          then,we should go for inner classes...
                Example 1:  There is a university object ,which contains cse,it,ece brances as a separate object..
                              suppose, this university involves in some illegal activity,and government decides to close this university....
                              So, university closes which implies now university object is not there which futher implies branches object will also be not there
                Conclusion :
                Therefore,without existance of university object there is no chance of branchs/departments object
                    
                    class University: # Outer class
                           class Department: # Inner class
                              pass
                      # As, without University object,there is no chance of existing Deparment object

                Example 2: Without Car object,there is no chance of existing Engine object.Hence we should declare Engine class inside Car class
                            class Car: # Outer class
                                class Engine:  # Inner class
                                    pass
                     # Without Car object,there is no chance of existing Engine object
                     
                Example 3: Without Head,there is no chance of existing of Brain. Hence we should declare Brain class inside Head class
                
                           class Head:
                                class Brain:
                                   pass
                    # Without Head,there is no chance of existing of Brain


       -> Advantages of inner classes :
            
            1) It improves modularity of the application : As we, do not have to declare each class outside / separately, instead we can declare within it class....
            
            2) It improves security of the application : For example ,University class. U can not directly access deparment object , first u have to go through the 
                                                                        University object.Thus,it improves security.
    
    #### IMP

    -> How to create inner class object : outter_object.Inner_class()
       Ex:
           o=Outer()
           i=o.Inner()
           
           or
           
           i = Outter().Inner()
           
           
    -> How to access inner class method :  o=Outer() # Outer class object creation 
                                           i=o.Inner() # Inner class object creation
                                           i.m1()  # Accessing inner class method
                                                    # or Outter().Inner().m1()
    
        Example: Demo inner class implementation
     ->
     
        class Outer:
            def __init__(self):
                print("Outer class Object Creation...")
        class Inner:
            def __init__(self):
                print("Inner class Object Creation...")
            def m1(self):
                print("Inner class Method")
            
        o=Outer() # Outer object created, 
        i=o.Inner() # Inner object creation, As it is a part of outter object we cant directly create inner object.. 
        i.m1()     # Or i=Outer().Inner()
                    # Or Outer().Inner().m1()
                    # Accessing inner class method
        
        # o/p -> Outer class Object Creation...
        #        Inner class Object Creation...
        #        Inner class 
        
        
        
   8) nested inner class : 

        class Outer:
            def __init__(self):
                print("Outer class Object Creation...")
            class Inner:
                def __init__(self):
                    print("Inner class Object Creation...")
                class InnerInner
                    def __init__(self):
                        print("InnerInner class Object Creation...")
                    @staticmethod
                    def m1(self):
                        print("Nested Inner class static Method")
        
        #static method can be accesed using object ref / class_name
        
        # both are valid
         # Outer().Inner().InnerInner.m1 
         Outer().Inner().InnerInner().m1 
         
      " IMP" 
     9)   Creating inner class object automatically when,outer object is been created
     
     Example 1: 
class Human:
    def __init__(self,name):
        print("Human Object creation")
        self.name=name
        self.head=self.Head() # Creating Head() object automatically,when Human object is created with head as refferance variable
    def info(self):
        print("Hiii..I am ",self.name)
        self.head.talk()
        self.head.brain.think()
    class Head:
        def __init__(self):
            print("Head object Creation")
            self.brain=self.Brain() # Creating Brain() object automatically,when Head object is created with brain as referance variable
        def talk(self):
            print("Talking")
        class Brain:
            def __init__(self):
                print("Brain object creation")
            def think(self):
                print("Thinking...")
human=Human("Pankaj")
human.info()
# O/P:
#   Human Object creation
#   Head object Creation
#   Brain object creation
#   Hiii..I am  Pankaj
#   Talking
#   Thinking...
          
          
            
        Example 2: 
        
        class Person:
            def __init__(self,name,dd,mm,yyyy):
                print("Person object creation")
                self.name=name
                self.dob=self.Dob(dd,mm,yyyy)  # Creating Dob object automatically , when person object is been created
            def info(self):
                print("Name :",self.name)
                self.dob.display()
            
            class Dob:
                def __init__(self,dd,mm,yyyy):
                    print("Dob object creation")
                    self.dd=dd
                    self.mm=mm
                    self.yyyy=yyyy
                def display(self):
                    print("DOB={}/{}/{}".format(self.dd,self.mm,self.yyyy))
        p=Person('Pankaj','21','02','2001')
        p.info()
        # O/P
        #Person object creation
        #Dob object creation
        #Name : Pankaj
        #DOB=21/02/2001
        
        
   10) Nested Methods : declaring method inside another method..
   
            -> Same as nested functions(In procedural)
            ->when u should go for nested methods ? When inside a method , any functinality requires multiple times
      
      ex1:
      
      class Test:
        def m1(self):
            def m2():
                print('Hii')
            m2()
            m2()
      t=Test()
      t.m1()
     # Hii
     # Hii
     
     ex2:
     
    class Test:
        def m1(self):
            def average(x,y):
                print((x+y)/2)
            average(10,20)
            average(10,10)
    t=Test()
    t.m1()
# o/p
#15.0
#10.0


 
   11) Garbage Collection (gc): destroys useless object (Garbage collector) 
   "IMP" -> Useless object is that object which has no refferance variable pointing to it..
     -> Garbage Collector : # A assistance , which keeps on running in background to destroy useless object.....
     -> Garbage collector is responsible for destroying useless object                      
     -> Becoz,of this the chance of failing Python program with memory failure is very less..
        Unlike,C++ programming language in which , the programmer is responsible to create and delete the object... 

   12) When we say a object is ready for garbage collection ?
    -> object with no refferance variable...ie. A useless object
      ie. When a object is not been refered by any refferance variable
      
      
   "IMP"
   13) How to enable and disable Garbage Collector (gc) :
   
    Note: -> By default gc is always enabled.
          
      -> To disable : we need to import buildin module 'gc' module .... 
                    
                       import gc
                       
          1) gc.isenabled() - Returns True if  gc is been enabled else False 
                               "Note :" By default gc is been enabled
                               
          2) gc.disable() - Use to disable gc    
      
          3) gc.enable()  - Use to enable  gc.
          
     Ex:  
            import gc
            gc.isenabled() # True
            gc.disable()
            gc.isenabled() # False
            gc.enable() 
            gc.isenabled() # True
          
     # VVI : Reason behind disabling gc can be: Performance will be increased as it won't run in background
            
      NOTE : Its not common to disable gc
         
        1) If u feel that in ur application memory problem won't be raised.(Has lots of memory)
        
        2) If u know , u r creating very less object...
        
     # Performace can be increases by disabling gc,as it wont be running in the background ,disable only if 
     # u feel ur application wont give memory problem or u r creating very less object 
     
     
     
     "VVI"
     14) Destructor : To perform clean-up activities likes ( Resource deallocation activities like closing database connection or network collection etc..)
     
         def __del__(self):
         {
            clean-up activities
         }
     
         -> destructor will be called , when an object is available for gc....
         
         -> Destructor is special metthod and name should be __del__() # Resource Deallocation
            constructor : __init__()#initialization
            
  "IMP"  ->  Just before destroying an object , " Garbage collector(GC) always calls destructor to perform clean-up activities " (like
             clean-up activities likes (Resource deallocation activities like closing database connection or network collection etc..)
         
         -> Once, Destructor execution completes the garbage collector automatically destroys that object...
         
         -> If the object is not been referred by any refferance variable , then that object is eligible for gc..
            ie( 0 reffrence variable)
            # Can be done by initializing that refferance variable to None or using del
             t=Test() # t :reffrence vaiable to Test()
             t=None # Now,t not reffering to any object and eligible for garbage collection
             or using
             del t
             
 "NOTE" : -> By default , at end of execution all object are eligible for garbage collection.. 
 
         -> By default at the end of execution gc will destroy all object,
            thus,by default destructor will called at the end of the program/execution
         
         -> Ex 1:  Default call to destructor(after end of the program ), as by default at the end of application all object is eligible for gc
          
          # Implicit / default call to destructor(after end of the program )
         class Test:
            def __init__(self): # Constructor
                print(" Object initialization activity")
            def __del__(self): # Destructor
                print("Fulfilling last wish of the object before destroying it by gc and performing clean-up activities")
         t1=Test() # constructor will be called 
         t2=Test()
         print("End of application") # After executing this line , all object will be eligible for gc ,before that destructor will be called twice for objects
         
         # O/P :
         #Object initialization activity
         #End of application
         #Fulfilling last wish of the object before destroying it by gc and performing clean-up activities
         #Fulfilling last wish of the object before destroying it by gc and performing clean-up activities
         
         -> ex 2: Explicit call to destructor( making object eligible for gc before end of application )
         
         class Test:
            def __init__(self): # Constructor
                print(" Object initialization activity")
            def __del__(self): # Destructor
                print("Fulfilling last wish of the object before destroying it by gc and performing clean-up activities")
         t1=Test() # constructor will be called 
         t2=Test()
         t1=None # Using ,initializing None to object ,object available for gc before end of execution , 0 refferance variable is pointing to the object
         del t2 # Using del,0 refferance variable is pointing to the object, available for gc
         print("End of application")
         
         #o/p
         #Object initialization activity
         #Fulfilling last wish of the object before destroying it by gc and performing clean-up activities
         #Fulfilling last wish of the object before destroying it by gc and performing clean-up activities
         #End of application
         
   """ NOTE : """ object is only avaiable for gc ,when it has no refferance variable pointing to it.....
                 Then, only destructor will also be called...
                 
                 
  ' VVI IMP Questions ':
  
  1) what is the differance between del t1 and t1=None ? # For making object eligible for gc
  ->  1)  del t1
       -> t1 deleted and corresponding object eligible for gc , we can not use t1 anymore...
       -> If we dont want object and corresponding reference variable , then we have to this approach...
      
      2)  t1=None
        -> t1 now onwards pointing to None object, Its just the reassigning of refferance variable. Also ,the object is eligible for gc 
        -> ie. we can use t1 (but its value is None)
        -> If we want referance variable but not the object 
        
  2) How to find no. of refferance variable of an object ?
   -> By sys module getrefcount() function 
        sys.getrefcount()  -> returns no. of referance variable (self is included by default,automatically added by interpreter)
   
   ex: import sys
       class Test:
            pass
       t1=Test() 
       print(sys.getrefcount()) # 2 {t1 and self(included by default)}
       
   3) Differance b/w constructor and destructor ?
   -> 
       Constructor :  
                    1) Name of the constructor : __init__()
                    2) Used for : initialization activities
                    3) Called : Just after creating an object ; PVM will execute constructor automatically to perform initialization activities.
        
       Destructor :
                    1)Name of the destructor : __del__()
                    2)Used for : clean-up activities
                    3)called : Just before destroying an object ; gc will execute the destructor automatically to perform clean-up activities.
                    
     
     