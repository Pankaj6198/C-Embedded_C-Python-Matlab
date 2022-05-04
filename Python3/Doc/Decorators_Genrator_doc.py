########################################################################################################################################
                                               

                                             Decorator Functions
                        -------------------------------------------------------- 
        
        'Basics require to understand decorators:
       
                1) Everything in python is an object, even function name aswell..
                
                    def f1():
                            print('Hello')
                            
                    print(f1)  # f1 --> reference to the function object      
                    
                  # f1 is the reference variable pointing to the function object
                  
         
           ' VVI' 2) Function Aliasing : For existing function we can give another name(alias) .
                   
                   For example:
                   
                   def wish(name):                       # Wish is the reffrence variable pointing to the function object
                            print('Good morning',name)

         'vvvvi'  greeting = wish # Creating Alias name for the function 
                  wish('P') # Good morning P
                  greeting('P') # # Good morning P  
                  
                  # both referance greeting and wish points to same object
                  # One function , two referance variables  
                

                3) A function can return another function:
                
                   def outer():
                        def inner():
                            print('inner function execution')
                        return inner # Return function object
                    
                   f1 = outer() # outer() function will be executed and returns inner fuction object 
                                # For that inner function object we r using f1 to refer  
                   f1() # o/p: inner function execution

                   # f1 is the reffreance/alis to the inner object 

                  'Passing function as argument  
                  ex: 
                        def f1(func):
                             func()  # Calling function that is been passed as argument to f1
                        def f2():
                             print('f2 function')

                        f1(f2) # Passing f2 function as argument to f1 function            

                        # So, internally f2 function will be called...
                        
                        # Output: f2 function

            
                'Introductions to Decorators 
                
                1)   Decorator is a function which can take a function as a argument and extends
                     its functionality and returns the modified function with extended functionality

                     Syntax:
                            def decor(input_func):
                                def output_function():
                                    ....... # Extra functionality
                                return output_function
                                    
                      Main objective of decorator functions is that we can exend the functionality
                        of existing function without modifing that function
                        
                        
                ------------------            -------------------------------------------              ----------------------------------------------     
               | INPUT_ Function  |    ----> | Decorator Function                       |   ---------> | Output function with extra functionalities |
                -------------------          |(Adding Extra functionalities to decorate |              | (ie. return inner)                         |
                                             |  like. customised response)              |              |--------------------------------------------| 
                                             |-------------------------------------------               
   ***VVI  # VVVVVVVI: To use the extended functionality we call input function only... but the inner function of decorators will be called internally   
           #vvvi NOTE:           
              '1) The inner function(extended functionality) must have same argument as of input function
             ' 2) The link b/w the decorator function and the input function is developed by @decorator_name (written before input function)
             ' 3) When ever we call any function , first of all PVM will check whether there is decorator configured for that function.. 
             '   if yes then it will call inner(decorator)      
             ' 4) Decorators must be defined first, and then the input fuction, so that the link can be establised
             '    (Order is important)
             ' 5) when @decor is used , then decorator function will be called always and inside decorator we can call input function
              '    but if we want to call original function sometimes and decorator function sometime then for that 
              '    insted of using @ , we simple pass input function to the decorated function
              '    ex: decorated_wish = decor_for_wish(wish)
              '        so, if wish() is called , the normal function will be called
              '        and if decorated_wish() is called then, decorated function will be called
             
                Example 1 :
                
                        def decor_for_add(func): # func=add (function aliasing)
                                def inner(a,b)
                                    print('#'*30)
                                    print('The sum: ',end='')
                                    func(a,b) # print(a,b) original function
                                return inner  # call inner
                                
                        @decor_for_add      # Link b/w decorator function and input function      
                        def add(a,b):# Input function which is to be decorated
                            print(a+b)
                        
                        add(10,20) # decorator Inner method will be executed
                        
                        
                    Output:
                      #########################################
                      The sum is 30
                      #########################################
            'VVI   Execcution flow :    
                    
                  1) At first , PVM will check whether a decorator is associated with the add(a,b) method
                   [Note: the decorator method(inner) and input function must have same argument list else it will throw error]
      ' VVVI'     2) Then at add(10,20), if PVM finds any decorator associated with the function then it will call the function which is been 
                      return by the decorator which in this case which is inner(a,b) ..... 
                      
                      
                  Example 2:
                            
                      def decor_for_wish(func):
                          names = ['PM','CM','Minister']
                          def inner(name):
                              if name in names:
                                print('#'*50)
                                print('Special Message:')
                                print('Hello {}, VIP Personal')
                                print('Very Very Good morning!!!!!')
                                print('#'*50)
                              else:
                                func(name) # Execute normal function for normal persons
                          return inner  
                      
                      @decor_for_wish   # instead of @ we can also use decorated_wish = decor_for_wish(wish) as well
                      def wish(name):
                            print('Good Morning :',name)
                            
                      wish('Durga') # O/P:Good Morning Durga
                      wish('CM') 
                      #O/P : wish('CM)
                      ###################
                      Special Message:
                      Hello CM, VIP Personal
                      Very Very Good morning!!!!!
                      ###################
                      
                      
                  **** Decorators can be used for customized response by adding extra functionality

                   
                   Example 3:
                      
                      def smart_div(func):
                          def inner(a,b):
                            if b==0:
                                print('Stupid, Cant divide a no. with zero ')
                            else:
                               func(a,b) 
                            return inner
                      @smart_div    
                      def div(a,b):
                          print(a/b)
                                
                      div(10,2) # 5
                      div(10,0) # Stupid, Cant divide a no. with zero 
                  
                  
    
              4)  Decorator Chaining : multiple decorator for same function
                
                example 1:
                
                    def decor1(func):
                        def inner1():
                            print("Decorator 1 execution")
                        return inner1    
                    def decor2(func):
                        def inner2():
                            print("Decorator 2 execution")
                        return inner2    
                    @decor1 # Only decor1 will be executed
                    @decor2
                    def f():
                        print('Original Function')
                              
                    # OUTPUT:
                     Decorator 1 execution
                     
                     'Reason :                   decor2 will return inner2
                     --------       ----------   and will be input for decor1   ----------  decor1 returns inner1      ' Only Final output is printed
                     | f()  |  ---> | decor2 |  ------------------------------> | decor1  | ---------------------------> inner1
                     --------        ---------                                  ----------            
                     
                     decor2 is nearest to f() therefore  f() will be input to decor2.
                     Atlast the final decorator output function will be executed.
                     
                example 2:
                
                    def decor1(func):
                        def inner1():
                            print("Decorator 1 execution")
                            func()
                        return inner1    
                    def decor2(func):
                        def inner2():
                            print("Decorator 2 execution")
                            func()
                        return inner2    
                    @decor2 # Only decor2 will be executed
                    @decor1
                    def f():
                        print('Original Function')     

                    #Output:
                    Decorator 2 execution
                    Decorator 1 execution
                    Original Function
                    # Reason:
                    # Pipeline will be decor2 will be called --> then decor1 as input to decor2 is decor1 ----> then finally fun() as input to decor1() is func()[original function]
                              
                                             




                                             Generator Functions
                        --------------------------------------------------------
                        
                        
                        
               1) Generator is a special type of function, which is responsible to generate a sequence of values.
                 
                 We can write generator fuctions just like orinary functions, but it uses a spcial keyword 'yield' to return values
                 
                 # Traditional way (Collections) vs Generator
                
                  1) Genrators are most suitable while handing huge data like lakhs of records from database..
                     As here the objects are been genrated on demands thus our application never fails to genrates values....
                   
                  2) Whereas in traditional way like list , it genrates all objects at the begining itself.
                  
                  
                  example:
                  
                   'Traditional Approch' :
                   
                   l = [x*x for x in range(1000000000000)]
                   print(l)
                   
                   # Output: 
                   
                   whole Application will be failed/hanged
                   
                   'Generator Approch' :
                   
                   l = (x*x for x in range(1000000000000))
                   print(type(l)) # class generator
                   
                   while True:
                         print(next(l))
                         
                   # Output: 
                       # All values will be printed
                   
                   
                   
               2) write a generator function to generate values 'A','B','C' ?
               -> 
                    def mygen():
                        yield 'A'
                        yield 'B'
                        yield 'C'
                    
                    g = mygen()
                    print(type(g)) # <class 'generator'>
                    print(next(g)) # 'A'
                    print(next(g)) # 'B'
                    print(next(g)) # 'C'
                    print(next(g)) # StopIteration Exception    
                        
               ' NOTE: If u dont know the no. of iteration and doesnot want StopIteration to be thrown by PVM then

                VVVI :  Better apporch to print the content of generator is :
               ---------------------------------------------------------------
                def mygen():
                        yield 'A'
                        yield 'B'
                        yield 'C'
                    
                g = mygen()
                for x in g:
                    print(x)
                # Output:
                # A   
                # B
                # C       
                        
                ##(Here u will never get stopiteration exception)     

                
                3) Write a generator function to generate first n values?
                ->

                    def first_n_values_generator(n):
                        i=1
                        while i<=n:
                            yield i
                            i=i+1
                    gen = first_n_values_generator(100)
                    for x in gen:
                      print(x)
                        
                        
                4) Write a generator function to generate values for countdown (after 1 sec) with provided max value?  
                ->
                   def countdown_generator(num):
                        while num>=1:
                             yield num
                             num=num-1
                   gen = countdown_generator(10)
                   import time
                   for x in gen:
                     print(x)
                     time.sleep(1)# pause for 1 sec
                    
                5) Write a generator function to generate fibonacci sequence ?
                -> # Fibonacci sequence for infinite times
                    def fibonacci_sequence():
                        a,b = 0,1
                        while True:
                            yield a
                            a,b = b,a+b
                    gen = fibonacci_sequence()
                    for x in gen:
                        print(x)
                   '---> Output : infinite fibonacci values'
                   
                   # fibonacci_sequence less equal to 100 value
                    def fibonacci_sequence():
                        a,b = 0,1
                        while True:
                            yield a
                            a,b = b,a+b
                    gen = fibonacci_sequence()
                    for x in gen:
                        if x <=100:
                            print(x)
                        else:
                            break
                    '---> Output :  0 1 1 2 3 5 8 13 21 34 55 89

                    
                   # fibonacci_sequence upto to 100 numbers
                    def fibonacci_sequence(num):
                        a,b = 0,1
                        i=1
                        while i<=num:
                            yield a
                            a,b = b,a+b
                            i=i+1
                    gen = fibonacci_sequence(100)
                    for x in gen:
                        print(x)                        
                    '---> Output : 100 fibonacci numbers '
                        
                        
                        
       # NOTE : Performace wise and memory wise genrator are very good therefore used in genrating many objects(lakhs..)
       
       
       
       A) Advantages (Genrators) :
       
            1) Memory Utilization is improved
                ( As value are not stored like traditional collections )
                          
            2) Performance wise also genrators is good

            3)  Best suitable if we want to handle very huge volume of data like handing data from
                lakhs of files,handling lakhs of records from database etc

       B) Disadvantages :
       
            1) No storage of data
            2) We cannot ask a Particular element (as values r genrated one by one)
                



        Decorator vs generator:
        ---------------------------
        
          Decorator : If we want to extend functionality of exisiting function 
                      without modifing that
                      
          Generator : If we want to generate a sequence of values then we should go for generators...
          
                        
                        
                         