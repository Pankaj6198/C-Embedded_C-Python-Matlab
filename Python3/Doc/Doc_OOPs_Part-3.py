
######################################################### OOPs PART- 3 ############################################################

# VVI :
 1) How to use member of one class inside other:
   -> In Two ways :
                   1) by HAS-A relationship (Also,known as Composition)
                   2) by IS-A relationship (Also,known as Inheritance)
                   
 2) By composition ( HAS-A relationship ):
 
   -> By using, creating an object of one class inside another class , we can access methods of one class inside another class... 
      This apporch is nothing but HAS-A relationship or composition..
   -> Main advantage of HAS-A relationship : Code Reusablity
   ->(Composition) can be Inner class ... (University and department example) ie.. without existance of outter class object , inner class object can not exist...
  # NOTE:(NOT a Inner class) Aggregation is also a HAS-A relationship, but its diffrent from composition ,here without existing object,another class object may exist
           # Ex: Department HAS A Proffesor : ie, if department shutsdown,still professor objects can exist,as they can transfer to different department.
             
  
  Ex 1:
  class Engine:
      def useEngine(self):
         print("Engine Specific Specification")
  class Car:
      def __init(self):
        self.engine=Engine()
      def useCar(self):
        print("Car required Engine functionality")
        self.engine.useEngine()
  c=Car()
  c.useCar()
  
  Conclusion: 
  # class Car HAS-A Engine refferance  
  
  Ex 2: 
  
  class Car:
      def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
      def getInfo(self):
        print('Name:{},model={},color={}'.format(self.name,self.model,self.color))
  class Employee:
      def __init__(self,ename,eno,car):
        self.ename=ename 
        self.eno=eno
        self.car=car
      def getEmpInfo(self):
        print("Employee Name :",self.ename)
        print("Employee No :",self.eno)
        print("Employee Car Info :")
        self.car.getInfo()
  c=Car('Innova','2.5V','Grey')
  emp=Employee('Durga','872425',c)
  emp.getEmpInfo()
  
  Conclusion: 
  # class Employee HAS-A Car refferance
  
  
  """ VVI """
  3) by Inheritance ( IS-A relationship)
    
    -> Inheritance : Parent to Child Relationship
    
    ->  Parent/base class 
        child/derived class
    
    -> Parent class members are by default available to the child class 
       and Hence,child class can reuse parent class functionality without rewriting.. # Code Reusablity
       
    -> Child class can define new members also..
       Hence,child class can extend parent class functionality.. # Code Extendibility
       
    -> parent class will contain common methods , which will be used by child class..
       and specfic method will be in child class (plus parent class (common methods also))
       
    -> class P:
            def m1(self):
                print("Parent Method")
       class C(P): # Inheritance : C = Child , P = Parent , therefore C will have both method of P as well as method of itself
            def m2(self):
                print('Child Method')
       c=C()
       c.m1() # Inheritance, method inherted from parent class P
       c.m2()
       
       # O/P : 
       #  Parent Method
       #  Child Method
       
    -> Example :
       class P:
            a=10 # Static Variable
            def __init__(self):
                print('Parent Constructor')
                self.b=20 # Instance variable
            def m1(self):
                print('Parent Instance Method')
            @classmethod
            def m2(cls):
                print('Parent Class Method')
            @staticmethod
            def m3():
                print('Parent Static Method')

       class C(P):
            pass

        c=C()
        print(c.a) # All inherited from Parent
        print(c.b)
        c.m1()
        c.m2()
        c.m3()
            
        # O/P :
        #Parent Constructor
        #10
        #20
        #Parent Instance Method
        #Parent Class Method
        #Parent Static Method
        
        
        
        
     " IMP "   
    4) Difference b/w IS-A relationship(inheritance) and HAS-A relationship(Composition) :
    
    -> Inheritance(IS-A) : If we want to extend functionality with some more extra functionality ...
                            then,we should go for IS-A Relationship(Inheritance)...
                            
                          Ex: Employee IS A Person
                          
    -> Composition(HAS-A) : If we dont want to extend and just we have to use existing functionality...
                            then, we should go for HAS-A Relationship(Composition)
    
                          Ex: Employee HAS A Car

      
    EXAMPLE:

class Car:
	def __init__(self,name,model,color):
		self.name=name
		self.model=model
		self.color=color
	def getinfo(self):
		print('\tCar Name:{}\n\tModel:{}\n\tColor:{}'.format(self.name,self.model,self.color))
class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def eatndrink(self):
		print('Eating Biryani and Drinking Beer')
class Employee(Person): # IS-A realationship
	def __init__(self,name,age,eno,esal,car):
		super().__init__(name,age)
		self.eno=eno
		self.esal=esal
		self.car=car
	def work(self):
		print('Coding Python Programs..')
	def empinfo(self):
		print('Employee Name:',self.name)
		print('Employee Age:',self.age)
		print('Employee Number:',self.eno)
		print('Employee Salary:',self.esal)
		print('Employee Car Information:')
		self.car.getinfo() # Employee using Car Functionality (HAS-A realtionship)

car=Car('Innova','2.5V','Grey')
e=Employee('Durga',48,872425,10000,car)
e.eatndrink() #Employee using Person class functionality
e.work()
e.empinfo()   



""" VVVI """
#NOTE:

 4) Types of Inheritance : 

    1) Single Inheritance  :  When one child class inherits only one parent class..( PARENT <---- CHILD)
                              ( Single parent to Single child relationship)
                            -> single parent and single child
                            -> child class will have aceess to parent class properties
                            
                            Ex:  class P:
                                    def m1(self):
                                        print('Parent Method')
                                 class C(P):
                                    def m2(self):
                                        print('Child Method')
                                 c=C()
                                 c.m1()
                                 c.m2()
    
    2) Multi-level Inheritance : When a class inherits a child class(grandchild class), it is called Multilevel Inheritance.(Parent <--- Child <----- GrandChild)
                                 The class which inherits the child class is called a grandchild class. Multilevel Inheritance causes grandchild and child relationships. 
                                -> The grandchild class has access to both child and parent class properties.
                                -> Inheritance will be in levels, one after the another
                                
                                Ex: # Two levels of inheritance
                                    class P:
                                        def m1(self):
                                            print('Parent Method')
                                    class C(P):
                                        def m2(self):
                                            print('Child Method')
                                    class Gc(C):
                                        def m3(self):
                                            print('GrandChild Method')
                                 Grand_child=C()
                                 Grand_child.m1()
                                 Grand_child.m2()
                                 Grand_child.m3()
                                
    3) Hierarchical Inheritance : when multiple classes inherits same class at same level ... |                   Parent    # Hierarchical structure
                                  -> One parent but multiple child                            |                  +       +
                                Ex                                                            |                 /         \
                                   class P :                                                  |                /           \
                                      def m1(self):                                           |             Child_1      Child_2               
                                          print('Parent Method')                              |
                                   class C1(P):
                                      def m2(self):
                                          print('Child 1 Method')
                                   class C2(P):
                                      def m3(self):
                                          print('Child 2 Method')
                                   c1=C1()
                                   c2=C2()
                                   c1.m1()
                                   c1.m2()
                                   c2.m1()
                                   c2.m3()
                                                
    4) Multiple Inheritance : when single child class inherits from multiple parent classes.. |                  Parent1    Parent2       # Hierarchical structure
  (" Not applicable in JAVA") -> Multiple parent <---- single child                           |                       +       +
                              -> Example (mom,dad) <---- single child                         |                        \     /
                              -> Reverse of Hierarchical Inheritance                          |                         \   /
                                                                                              |                         Child               
                              Ex:                                                             |
                                  class P1:
                                    def m1(self):
                                        print('Parent 1 Method')
                                  class P2:
                                    def m2(self):
                                        print('Parent 2 Method')
                                  class C(P1,P2):# Order is also important
                                         print('Child Method')
                                         
                                 c=C()
                                 c.m1()
                                 c.m2()
                                 c.m3()
   
     " IMP "  
     'Note': # JAVA ,C#,.NET doesnot support multiple Inheritance
  ie. In java if we try to define multiple parent class , it will give error
  Because of ' ambiguity problem(due to same method name in both class )' or also called as ' diamond access problem ' 
   Ex:                               
                                  class P1:
                                    def m1(self):
                                        print('Parent 1 Method')
                                  class P2:
                                    def m1(self):
                                        print('Parent 2 Method')
                                  class C(P1,P2):# Order is also important
                                         print('Child Method')
                                         
                                 c=C()
                                 c.m1() # which m1() should be called  : m1() from P1 will be called
                                 
                                 # O/P :
                                 # Parent 1 Method
                                 
  # Same problem also occur in python ,but it resolve it in different manner
  
            P1 (contains m1())       P2 (contains m1())
                            +         +
                             \       /
                              \     /
                               \   /
                                 C                    
                   (from child class if u call m1() ) # which m1() method u r calling , as both parent has m1() #### Ambiguity
                    # therefore , there is no way to solve this problem in java
     " IMP "
     In python,
     ambiguity problem(due to same method name in both class ) or also called as ' diamond access problem ' 
     is resolved as :
     In python, Order of(class C(P1,P2):) is important in multiple Inheritance...
     thus, the order decides that which m1() method should be called ,through Child class object....
       
     As, if it is :
     class C(P1,P2) # m1() from P1 will be called, if its not there then m1() in P2 will be called
     class C(P2,P1) # then , m1() of P2 will be called
     
    5) Hybrid Inheritance : Combination of single,multi-level,Hierarchical,Multiple.. inheritances
       # So, which order method will be called depends upon MRO algorith
       ie. how the method will be search and from which class the method will be executed..(if method have same name)
       Here, method resoultion takes place with the help of algorithm 'MRO'# Method Resolution Order 
       as, in hybrid multiple parents,childs will be are there ,combination of  4 inheritance will be there....
       " MRO Algorithm" --> ## Covered in point:5
        
     
    6) Cyclic Inheritance : The concept of inheriting members from one class to another class in Cyclic way .
       (# NOT SUPPORTED IN PYTHON,JAVA becoz .. It is not required)                    
                            ex:  
                              if A is child of A # Cyclic Inheritance  ## Its not required 
                              or if B is child of A and A is child of B # cyclic inheritance  
                                                                        # Its same as defining one class therefore cyclic is not required
    
    "VVI NOTE":
    Really, Cyclic inheritance is not required. Hence programming language like Python , Java does not provide support.
  

 # IMP 
 5)  MRO(Method Resolution Order) Algorithm : # how method will be searched in hybrid inheritance
     "Also known as C3 algoritm,  " 
     -> Proposed by Samuele padroni 
     -> In hybrid inheritance the method resoultion order is decided based on MRO algorithm.
     -> How method will be resolved for any class..
"VVI"  -> It follows " DLR " : " Depth First Left to Right "
          -> ie. Child will get more priority than parent.
          -> Left Parent will get more priority than Right Parent.
     -> MRO of any class can be found using ' mro()' function.
        print(classname.mro())
         
 ## NOTE: 
 " VVVI"  """ -> For every class in python  there is one parent class is there which is object class 
                 ie.. Every class in python is child class of object class....
              -> Object class acts as a root class ..
              -> Rarely used
          """
    "IMP"       
   -> how to check mro of any class : classname.mro() 
   
   -> Example 1 :   2 level hybrid (simple)
   
                             Object Class (bulitin Root class) 
                                 ^
                                 |
                                 |
                                 A         {  
                               +   +       # Hierarchical 
                              /     \      # Inheritance
                             /       \       
                            B         C    }  {  
                             +       +         # Multiple
                              \     /          # Inheritance
                               \   /
                                 D           }    
                          
                          d = D()
                          d.m1() # how m1() will be searched 
                          # first check D , then left parent class B, then right parent class C , and then check in A, atlast in object class
                          # D.mro() - DBCAO
                    ## O/P :
                   [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
     
                          
    # How m1() will be searched :
   d.m1()  -> First, m1() will be searched in class D , And if not found ,
             then it will search in class B(left Parent class first)(left to right priority) ,and if not then class C,
             if not found, then class A, then at last it will search in root class ie. object class ..
             if, then also its not found then it will throw attribute error...
             
   ** classname.mro()
    - A.mro() : A,if method is not available then search in object
    - B.mro() : B,A,object
    - C.mro() : C,A,object
    - D.mro() : D,B(left to right,high priority),C,A,object
                          
   class A:pass
   class B(A):pass  
   class C(A):pass  
   class D(B,C):pass   
   print(D.mro()) # to show mro of class D ## classname.mro()
   print(C.mro()) # to show mro of class C
   
   
   Example 2:  3- level hybrid
   
   
                              Object Class (bulitin Root class) 
                              +   ^     +  
                             /    |      \
                            /     |       \
                          A       B         C  
                          +     +   +      + +
                           \   /     \    /  |
                            \ /       \  /   |  
                             D         E     |
                              +       +      |   
                               \     /       |   
                                \   /        |
                                  F _ _ __ _ |        
  
    - D is the child for A and B .
    - E is the child for B and C .
    - F is the child for D , E and C .    
      
     class A:pass
     class B:pass
     class C:pass
     class D(A,B):pass
     class E(B,C):pass
     class F(D,E,C):pass 
     print(A.mro()) # A,O
     print(B.mro()) # B,O
     print(C.mro()) # C,O
     print(D.mro()) # D,A,B,O
     print(E.mro()) # E,B,C,O
     print(F.mro()) # F,D,A,E,B,C,O   ## IMP @ keep left : complete all left first
     
    proof:
     class A:
            def m1(self):
                print("A class method")
     class B:
            def m1(self):
               print(" B class method")
     class C:
            def m1(self):
               print(" C class method")
     class D(A,B):
            def m1(self):
               print(" D class method")
     class E(B,C):
            def m1(self):
                print(" E class method") 
     class F(D,E,C):
            def m1(self):
               print(" F class method")
     
     f=F()
     f.m1() # F class method, if not found then search in D,then, A ,following the order( MRO )  
            # MRO of F :  F,D,A,E,B,C,O 
            
  

  6) Internal working of MRO algoritm :   
            
       for class X
    
   MRO(X) = X + merge(MRO(P1),MRO(P2).....,parent List)       
     
     P1,P2.... -> Immediate Parents
     
     
  "IMP"   
   7) super() Function : To access methods or variables of parent class inside child class ' when  naming conflict occurs '
                         ie. methods having same name in child and parent class both like constructor or any other method.
                         then , we use super() method..
                         
                         -> # NOTE: If there is no naming confict, then u can use self also.... 
                         
                         -> To call parent class constructor in child class use of super() is compulsary..
                            due to naming conflct of constructors.. 
                         
                         -> super() is use to access  parent methods,varibles inside child class explicitly when there is a naming conflict...
                         # NOTE : we can also access parent class members with the help of self
                         #  but using self u cant call parent constructor from child class due to naming confilct(method with same name)
                          Therefore , we use super() to access parent class method in child class..
                         
                         -> Parent class members are by default available to the child class.
                            In the child class we can access parent class members  directly.
                            
                         ->   If parent class and child class contains a member with the same name , then to 
                              call explicitly parent class members from the child child class we should use super().
                              
                         -> super() is a built-in function which is useful to call the super class(Parent class) constructors, methods
                            and variables explicitly from the child class
     
     Ex:
          class P:
                def __init__(self):
                    print("Parent Constructor")
                def m1(self):
                    print("Parent Method")
          class C(P):
                def __init__(self):
                    print("Child Constructor")
                def m1(self):
                    print("Child Method")
                    super().__init__() # Parent Constructor
                    super().m1()       # Parent Method
          
          c=C()  # Child Constructor
          c.m1() # Child Method
          
          

    8) How to call method of a particular super class (Parent class) :
      # In  Multi-level Inheritance
      
      By using super() we can call immediate parent class methods.
      if we want a particular super class (Parent Class) method ..
      
      -> Two ways : # To access m1() of B super class from E
                    1) classname.methodname(self)
                        Ex: B.m1(self) # for m1() of B class
                        It will call m1() methof of A class
                        
         'VVVI '    2) super(classname(),self).m1()                    
                        Ex: super(C,self).m1() # for m1() of B class
                      It will call m1() method  of super class of C , which is B..
                      ie. super class of C , which is B .. m1() will be executed  
                        
           " VVI NOTE ": Here, C will be used as class name not B....
                      As, B is the super class(parent class) for C...
                      And super() is used to access parent members from child...
                      
                         
    Ex:  #  To call m1() of B super class from E class
      
      
      #  Multi-level Inheritance
      class A:
          def m1(self):
                print("A class method")
      class B(A):
          def m1(self):
                print("B class method")
      class C(B):
          def m1(self):
                print("C class method")
      class D(C):
          def m1(self):
                print("D class method")
      class E(D):
          def m1(self):
                print("E class method")
                B.m1(self) # B class method
                ## other way
                super(C,self).m1() # B class method
 # NOTE: As , super class of C is B.. As super() is use to access parent members(B) from child class (C).. 
 # like .. in intermidiate parent class super().m1() will used in C class
      e=E()
      e.m1()    



     9)  # VVI NOTE:
     
         We cannot use super() to access parent class instance variable from child class..
         if both class has same instance variable..[ Naming confict]
         it is because... one object can store only one copy of instance variable..
         (ie. only one copy of b will be store inside object, therefore u cant access b of parent and child class diffrently )
         we should use self only...
      
     Ex:  
     
        class P:
            a=888
            def __init__(self):
                self.b=999
        class C(P):
            def __init__(self):
                #self.b=20
            def m1(self):
                print(self.b) # 20
                print(self.a) # 888
                print(super().a) # 888
                print(super().b) # Error , u can not access instance variable of parent class using super() if there is naming confict
      
      10) From child class constructor and instance method ,use can directly call any method of parent class (instance,class method,static method)
          super().__init__() , super().m1()
          
          Ex: 
             class P:
                def __init__(self):
                   print("Parent Constructor ")
                def m1(self):
                   print("Parent Instance Method")
                @classmethod
                def m2(cls):
                   print("Parent Class Method") 
                @staticmethod
                def m3():
                   print("Parent Static Method")
             class C(P):
                def m1(self):
                    super().__init__()
                    super().m1()
                    super().m2()
                    super().m3()
             c=C()
             c.m1()
        
 
      11) From class method of child class, how to call parent class constructor and instance methods indirectly???
          super(C,cls).__init__(cls) # accessing parent methods from child class method
          ex: 
             class P:
                def __init__(self):
                   print("Parent Constructor ")
                def m1(self):
                   print("Parent Instance Method")
             
             class C(P):
                @classmethod
                def m1(cls):
                   super(C,cls).__init__(cls)   # accessing parent methods from child class method
                   super(C,cls).m1(cls)
             c=C()
             c.m1()
             ## or C.m1()
    
    11) How to call parent class static and class method from child class static method..
        super(C,C).m1() # classname twice
     Ex:
        class P:
                @classmethod
                def m1(cls):
                   print("Parent Class Method") 
                @staticmethod
                def m2():
                   print("Parent Static Method")  
        class C(P):
                @staticmethoddef 
                def m3():
                   super(C,C).m1()
                   super(C,C).m2()
        c=C()
        c.m3()
        
        