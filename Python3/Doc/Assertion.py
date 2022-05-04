###################################### Assertion #########################################

      # Assertions: Used to perform debugging as, a alternative to print() statements..        
        assert()   # As, after debugging we can disable assert() explicitly, 
                   # but, in case of print() statements we have to delete it explicitly. 
        
            1) Bug : The deviation between expected output and the orginal output.
        
            2) Debugging : The process of identified and fixing the bug is called debugging.
        
            3) The most common way of debugging is usage of print() statement.
       
                -> But the problem with the print statement is, after fixing the bug, compulsory we have to delete
                   the extra added print() statements, otherwise these will be executed at ruuntime which creates performance
                   problems and disturbs server logging/console output.
           
  'VVVI'    4) To overcode this problem, we should go for assert statements insted of print statements.
               -> Main advantage of assert() statements over print() statements is,
                  after fixing the bug we are not required to delete assert statement explicitly.
               -> Based on our requirement, we can enable or disable assert statements.

              # Hence the main purpose of assert statements is to perform debugging.

              
        
             5) For any project , the following three types of environment available :
                        
                        1) Devlopment environment (Dev env) 
                        2) Test environment ( QA env)
                        3) Deployment/Production enviroment (Live env)
                        
                -> Usually we can perform debugging either in development enviroment or
                   Test environment but not in production enviroment.
                -> Hence, assertion concept is only for Dev and Test Environment but not for
                   deployment/production enviroment.                
                   
                   
            6) Types of Assert Statements :

              `1. Simple version: 
              
                        'Syntax': assert conditional_expression
                  # In java , assert(conditional_expression)
                 
                   -> If condition is TRUE, then our assumption is statisfied 
                       and hence remaining code will be executed normally   

                   -> If condition fails then somewhere something goes wrong. Hence the program will be 
                      stopped by raising AssertionError. By seeing AssertionError,
                      programmer can analyse the code and fix the bug.
                      
                      
               2. Augmented Version (More simpler version) :
               
                        'Syntax': assert conditional_expression,message
                  # In java , assert(conditional_expression):"message"      
                        
                        -> If condition fails then message will be printed in addtion to
                           AssertionError, which is very helpful for debuggging easily.
               
               
             -> Example:

                    def squareIt(x):
                        return x**x # should be x**2
                    assert squareIt(2)==4,'The square of 2 should be 4' #   Augmented Version of assertion
                    assert squareIt(3)==9,'The square of 3 should be 9'
                    assert squareIt(4)==16,'The square of 2 should be 16'        
                    
                    print(squareIt(2))
                    print(squareIt(3))
                    print(squareIt(4))
                    
                 # Output :
                 #  assert squareIt(3)==9,'The square of 3 should be 9'
                 #  AssertionError: The square of 3 should be 9 
                 
                 
                 
                 
              7)  How to disable assert statements in python ? # By default in python assert statements are enabled..
                 
                  -> by using -O option
                  -> python test.py ==> Assert statements will be executed
                  -> python -O test.py ==> Assert statements wont be executed
                  
                  Example: # If same example is executed like this
                   output :
                  # C:\Users\Nutan\Desktop\Codes>python -O test.py
                  #  4
                  #  27
                  #  256
                  
                  
 'IMP'        8) Exception Handling vs Assertion  :

                 -> Assertion concept can be used to alert programer to resolve devlopment time
                    errors / bugs. It is applicable for Devlopment and Test environments.
                  
                 -> Exception Handling concept can be used to handle runtime errors.
                    It is applicable for production environment.