
##################################### Exception Handing PART-1 ###################################################################################

 1) In any programming language, there are 2 types of possible errors :

            1) Syntax Error :
                             -> The errors which occurs because of invalid syntax,
                                such type of errors are considered as syntax errors.

                             -> Programmer is responsible to correct these syntax errors.
                                Once all syntax errors are corrected, then only program execution
                                will be started.

            2) Runtime Error : # Exceptions

                'NOTE'       -> Also known as Exceptions.

                 'VVI'       -> While executing the program,at runtime if something goes wrong
                                because of end user input,memory problem,programming logic etc,
                                then we will get Run time errors

                 'VVVI'      -> ' Exception Handling concept is applicable for Runtime Errors '
                                 but not for syntax error..

                            Examples: #  ZeroDivisionError
                                      #  ValueError( For invalid coversions ,like "hii"=> int)
                                      #  FileNotError


 2)  # 3  Most Important Questions:

     1) What is an Exceptions ?
     -> An unwanted and unexpected event that distrubs normal flow of the program is called Exception.
       like InternetError,SleepingError,TypePuncureError..


     2) What is the main objective of Exception Handling ?
     ->
        1) It is highly recommended to handle exceptions.
        2) The main object of exception handling is to maintain the normal flow of the program..
           or graceful temination/normal termination of the application
           (ie. We should not block our resourses and we should not miss anything)

      Example:
             Suppose i want to perform some operations on data from db
            # Then ,things i need to do will be
             1) Create db connection
             2) Read data from db
             3) Perform some Operations
             4) Then , close db connections

             Suppose , somehow i got a exception while reading data from db (db connection is success )
             Due to which, program will abnormally terminated...
             And, , the db connection wont be closed..
             which give rise to loss of resourse as our one connection will be wasted...
             and same happens with mutiple people 10 , then the 11th person wont be able to establish a connection to db
             due to maximum connection request error,therefore total application , total project will be down...

     3) What is the meaning of Exception Handling ?
     ->  It is just way to define an alternative way to continue rest of the program nomally.
         This alternative is nothing but exception handling..
     ->  Exception Handling does not mean repairing an exception

     Example: # Trying to open a london file
               try:
   'Main Code'        # Read data from Remote file
                      #located at london
               except FileNotFoundError:
   'Alternative Code' #Use local file and continue
                      # rest of the program normally


 ## IMP
 3) Default Exception Handling :

     'IMP'  -> Every exception in python is an object..
                For Every exception type the correponding class is available.
            "NOTE" : # Every Exception class is the child class of BaseException class

            -> Whenever an exception occurs PVM will create the correponding exception object and will check for handling
               code. If handling code is available thenit will be executed
               and rest of the program will be executed normally.

            -> If handling code is not available then PVM will terminates program
               abnormally and print corresponding exception information to the console.
               The rest of the program wont be executed.

            -> To prevent this abnormal termination we should handle exceptions explicitly.
               Ofcourse using try-except blocks.


   4) Pythons Exceptions Hierarchy :

     # NOTE : BaseException class is the parent class for all Exception class

         ' NOTE ' : Most of the time in Exception Handling we will be dealing with Exception and its child classes

                -> Every Exception in python is a class.

                -> All exception classes are child classes of BaseException either directly or indirectly.

     "VVIMP"    -> Hence, BaseException acts as root for python Exception Hierarchy

       "NOTE"   -> Being a programmer , most of the times,we have to concentrate/handle
                   Exception and its child classes..


               " Partial Hierarchy "
            " Child classes of BaseException class"

                BaseException  # Parent class
                |
                |
                |------> Exception  # child class of BaseException
                |        |(for Exception ,further there is child class of Exception)
                |        |
                |        |------>  ArithmeticError   # child class of Exception
                |        |         |(for ArithmeticError ,further there is child class for ArithmeticError)
                |        |         |
                |        |         |------> ZeroDivisionError # child class of ArithmeticError
                |        |         |
                |        |         |------> OverflowError # child class of ArithmeticError
                |        |         |
                |        |         |------> FloatingPointError # child class of ArithmeticError
                |        |
                |        |
                |        |
                |        |------> LookupError # child class of Exception
                |        |        |
                |        |        |----> IndexError (In string,list when try to access out of range ) # child class of LookupError
                |        |        |
                |        |        |----> KeyError (In dict, when key is not found)  # child class of LookupError
                |        |
                |        |
                |        |-------> OSError  # child class of Exception
                |        |         |
                |        |         |----> FileNotFoundError # child class of OSError
                |        |         |
                |        |         |----> InterruptedError  # child class of OSError
                |        |         |
                |        |         |----> TimeoutError  # child class of OSError
                |        |         |
                |        |         |----> PermissionError  # child class of OSError
                |        |
                |        |-------> AttributeError # child class of Exception
                |        |
                |        |-------> EOFError # child class of Exception
                |        |
                |        |-------> NameError # child class of Exception
                |        |
                |        |-------> ValueError # child class of Exception
                |
                |------> SystemExit 'SystemError' # child class for BaseException
                |
                |
                |------> GeneratorExit # child class for BaseException
                |
                |
                |------> KeyboardInterrupt # child class for BaseException







    5) Customised Exception Handling by using try-except :

          -> The main advantage of Exception Handling is graceful termination ie.(Normal flow of the program sholud note be distrubed)

          -> 'NOTE' : It is highly recommended to handle exceptions.

 "VVI"    -> The code which may raise an exception is called Risky Code..
            and we have to take that code inside try block...

          -> And, The corresponding handling code we have to take inside except block.

          -> "NOTE" : The code which may raise exception is called as 'risky code'
               Ex: 10/0 ==> ZeroDivisionError # Risky code

 'NOTE'   -> In Python, 'try-except'
             In Java , 'try-catch'
             # In java, there is catch block instead of except block in python...

          ->  # Without try-except :
            print("Statement - 1 ")
            print(10/0)# Risky code # No handling code for ZeroDivisionError
            print("Statement - 3 ")

            # Output : Statement-1 will be printed
            and then program will be terminated by raising ZeroDivisionError...
            which is a Abnormal/non-graceful termination...


          -> # With try-except:
             ## Highly recommended
             'Syntax' :
                        try:
                            # Risky Code : Code which may throw exception
                        except:
                            # Handling Code / Alternative code
             Ex:

             print("Statement - 1 ")
             try:
                print(10/0)# Risky Code : Code which may throw exception
             except ZeroDivisionError:
                print(10/2) # 5.0
             print("Statement - 3 ")
             ## Normal/graceful Termination
             # Output :
             # Statement - 1
             # 5.0
             # Statement - 3


      6) Control Flow in try-except :

         try:
             stat-1  # Statements
             stat-2
             stat-3
         except XXX:
             stat-4

         stat-5

        "IMP"
        -> Important Cases -

            ' Case 1' : If there is no exception - # Except block wont't be executed
                        # Statements executed will be :
                        stat-1 , stat-2, stat-3 ,stat-5 , 'Normal Termination'

            ' Case 2' : If an exception raised at stat-2 and corresponding except block matched:
                        # Inside try block we only have to take risky code not the normal code.. Thus, the try mustbe small...
                        # Statements executed will be :
                        stat-1 , stat-2, stat-4,stat-5 , 'Normal Termination'

  "NOTE"    ' Case 3' : If an exception raised at stat-2 but corresponding except block does not matched:
               # Statement 1 will be executed and Exception will be raised ,and PVM will search for handling, which is not there...
               # Statements executed will be :
               stat-1 , 'Abnormal Termination'

  "NOTE"    ' Case 4' : If an exception raised at stat-4 or stat-5 :
                'NOTE' # If any statement which is not inside try block whether rasing an exception , then there will be abnormal termination
               # Statements executed will be :
               stat-1 , 'Abnormal Termination'


        -> Conclusion  :

     'IMP'  1) Within the try block block if anywhere an exception raised
               then rest of the try block wont be executed even though we handled that exception...
               Hence, inside try block we have to take only risky code
               and the length of the try block should be as less as possible...

     "IMP"  2) In addition to try block, there may be a chance of raising exception
               inside except and finally block also...

     "IMP"  3) If any statement which not part of try block, raising an exception
               then it is always Abnormal Termination...



      7)  How to print Exception Infomation on the console :

            Examples :
          -> try:
                 print(10/0)                  ## Hold ZeroDivisionError class object with msg as refferance variable
             except ZeroDivisionError as msg: # Exception object created with refferance variable msg (NOTE: msg is just a name , insted of msg it can be anything)
                 print(" Exception Type :",type(msg)) ## Exception Type : <class 'ZeroDivisionError'>
                 print(" Exception Type :",msg.__class__) ## Exception Type : <class 'ZeroDivisionError'>
                 print(" Exception Class Name :",msg.__class__.__name__) ## Exception Class Name : ZeroDivisionError
                 print(" The Description of Exception :",msg) ## The Description of Exception : division by zero

          -> Multiple Exceptions :
            # Possible Exception can occur in following code:
            # ZeroDivisionError,ValueError
             try:
                x=int(input('Enter First Number')) # ValueError possible
                y=int(input('Enter Second Number'))
                print("The result : ",x/y) # ZeroDivisionError possible
             except BaseException as msg: # It can handle either BaseException or its child class ## BaseException  " Parent class"
                print(" The Type of Exception :",type(msg))
                print(" The Type of Exception : :",msg.__class__)
                print(" The Name of Exception :",msg.__class__.__name__)
                print(" The Description of Exception :",msg)

            ## OUTPUT :
            Case 1: # ZeroDivisionError
                   If x=10 and y=0 ,  (10/0)
             # Output :
             The Type of Exception : <class 'ZeroDivisionError'>
             The Type of Exception : : <class 'ZeroDivisionError'>
             The Name of Exception : ZeroDivisionError
             The Description of Exception : division by zero

            Case 2: # ValueError
                    If x=10 and y='abc' , (10/'abc')
            # Output :
            The Type of Exception : <class 'ValueError'>
            The Type of Exception : : <class 'ValueError'>
            The Name of Exception : ValueError
            The Description of Exception : invalid literal for int() with base 10: 'asd'



      # VVVIMP
      8) Try with multiple except block :

                        -> The way of handling an exception is varied from exception to exception.
                        -> Hence, for every possible exception type,we have to take a separate except block.
                           try with multiple except blocks is possible and recommended to use.


            try:
                # Risky code....
            except ZeroDivisionError:
                # perform alternative arithmetic operations
            except FileNotFoundError:
                # Use local file instead of remote file(london file)


           -> If try with multiple except blocks available,then based on raised exception
            the cooresponding except block will be executed.

            Example:
            # Possible exceptions in below code are ZeroDivisionError and ValueError
                try:
                    x=int(input('Enter First Number')) # ValueError possible
                    y=int(input('Enter Second Number'))
                    print("The result : ",x/y) # ZeroDivisionError possible
                except ZeroDivisionError:
                    print(" Cannot divide with Zero ")
                except ValueError:
                    print(" Please provide int values only")

           -> If try with multiple except blocks available then the order of these except blocks is important.
    "IMP"     { VM will consider them "top to bottom" until matched  except block identified.
            # Order : Top to Bottom
  "NOTE"    # Parent class exceptions can handle exception of child class
            Example 1:
                    try:
                        print(10/0)
                    except ZeroDivisionError:
                        print("ZeroDivisionError")
                    except ArithmeticError: # Parent class of ZeroDivisionError
                        print("ArithmeticError")

                    # O/P :  ZeroDivisionError

            Example 2:  When order is change  # Order of seraching cooresponding except block is top to bottom
                    try:
                        print(10/0)
                    except ArithmeticError: # Parent class of ZeroDivisionError, As parent can handle child exceptions
                        print("ArithmeticError")
                    except ZeroDivisionError:
                        print("ZeroDivisionError")


                    # O/P: ArithmeticError


          # VVI
          9) Single except block that can handle multiple different exceptions :
              # In java it is done using multicatch block
             -> If handling code is same for multiple exceptions,the instead  of taking different except block,
                we can take single except block that can handle all those exceptions.

                like :# Parenthesis is compulsary

                 Syntax:
                        except (Exception1,Exception2,..): # For handling both exception at the same time
                    OR  except (Exception1,Exception2,..) as msg: # For printing Exception information on the console

       "NOTE" -> Parenthesis are mandatory ,As this group of exception internally considered as tuple....

              -> Example : # print Exception information on the console
                    try:
                        a = input("Enter 1st number : ")
                        b = input("Enter 1st number : ")
                        print("Result:",a/b)
                    except (ZeroDivisionError,ValueError) as msg: # Parenthesis is compulsarory as internally it is treated as tuple
                        print(" The Raised Exception:",msg.__class__.__name__)
                        print("Description  of Exception",msg)
                        print("Please provide valid input only")


        #VVVI
          10)  Default Except block :

               -> We can use default except block to handle any type of exceptions..

               -> In default except block,generally we can print exception to the console..

               ->   Syntax:
                           except:
                                  #statements

               -> Example :
                        try:
                            a = input("Enter 1st number : ")
                            b = input("Enter 1st number : ")
                            print("Result:",a/b)
                        except: # Default Except block: Can except any Exception
                            print("Default Except: Please provide valid input only")

               -> Order for searching corresponding except block is Top to Bottom...

               -> " NOTE : " Default exception block must be at last , else PVM will give error..

              -> If default except block is defined then compulsory it must be last except block,otherwise we will get SyntaxError..

              Example :
                        try:
                            print(10/0)
                        except: # Default except block    #### Invalid, Default exception block must be at last
                            print("Cant divide by Zero")
                        except ZeroDivisionError:
                            print("ZeroDivisionError")


                        # Output :
                         Error as Default except block must me at last

                -> This restriction is applicable only for default block not for
                   normal except block but for normal except blocks..
                   ie. normal except blocks can be in any order.


          ## IMP
            11) "Summary" : Various possinle combinations of except blocks

                 -> If except blocks is defined for only one exception then parenthesis are optional.
                    If multiple exceptions are there then perenthesis is compulsarory...

                 -> If we use parenthesis, then 'as' must be outside of parenthesis only..

                 # Valid combinations of Syntaxs:

                 1) except ZeroDivisionError :

                 2) except (ZeroDivisionError) :

                 3) except ZeroDivisionError as msg:

                 4) except (ZeroDivisionError) as msg:

                 5) except (ZeroDivisionError,ValueError) :

                 6) except (ZeroDivisionError,ValueError) as msg :

                 7) except: # default  exception block


                 # Invalid Combinations :

                 1) except (ZeroDivisionError as msg): # as msg must be outside of parenthesis
                 2) except ZeroDivisionError,ValueError: # Multiple exceptions must be in parenthesis , as internally it is tuple
                 3) except (ZeroDivisionError,ValueError as msg): # as msg must be outside of parenthesis


            # VVIMP
            12) Finally Block Purpose and Specialty :

                 -> It is not recommended to place cleanup code(resourse deallocation code like closing database connection etc)
                    inside try block, beacause there is no guarantee for execution of every statement inside try block.

                 -> It is not recommended to place cleanup code inside except block,
                    because if there is no exception then except block wont be executed.

                 -> Hence, We required some place to maintain cleanup code
                    which should be executed always irrespective of whether exception raised or not handled.
                    Such type of best place is nothing but finally block.

         "NOTE" #  Hence the main purpose of finally block is to maintain cleanup code.

                  -> Syntax:

                            try:
                                # Risky Code
                            except:
                                # Handling Code
                            finally:
                                # Cleanup Code

       "NOTE"     -> finally block will execute always no matter what is the case....
                     # Note: In only one case finally will not execute , if we shutdowm PVM explicitly by os._exit(0)
                     ie. The speciality of finally block is , it will be executed always irrespective
                         of whether exception raised or not raised and wheter exception handled or not handled.


                  -> Example :

                     1) Case-1: If No exception

                                try:
                                    print("try")
                                except:
                                    print("except")
                                finally:
                                    print("finally")

                        # O/P :
                          try
                          finally


                      2) Case-2: Exception raised but handled

                                try:
                                    print("try")
                                    print(10/0)  # ZeroDivisionError raised
                                except ZeroDivisionError:
                                    print("except")
                                finally:
                                    print("finally")


                            # O/P :
                              try
                              except
                              finally


                       3) Case-3: If exception raised but not handled

                                try:
                                    print("try")
                                    print(10/0)  # ZeroDivisionError raised
                                except ValueError:
                                    print("except")
                                finally:
                                    print("finally")

                            # O/P :
                              try
                              finally
                              Abnornal Temination : ZeroDivisionError

            "IMP"      4) Case-4 : If exit() function is used
                                   
                                   try:
                                        print("try")
                                        exit()
                                   except: # Default except block ; except all exception
                                        print("except")
                                   finally:
                                        print("finally")
                                    
                            # O/P :
                              try
                              except
                              finally
                              
                      # when using nornmal except  
                                        
                                   try:
                                        print("try")
                                        exit()
                                   except ZeroDivisionError: # Normal Except block
                                        print("except")
                                   finally:
                                        print("finally")
                                      
                                # Output:
                                    try
                                    finally
              

              
           # VVVVIMP      
        13) finally block vs os._exit(0) :

           "VVVI " : # os._exit(0) is used to shutdown PVM explicity 
                     # And this is the only case when, finally block can not be executed... 

              -> There is only one situation where finally block wont be executed
                 ie. whenever we are using os._exit(0)

              -> Whenever we r using os._exit(0) then PVM itself will be shutdown.
                 In this particular case finally block wont be executed.
              
              -> os._exit(0) ==> 
                 
                   -> Here " zero " represents " status code "
                   -> 0 ==> Normal Termination
                   -> Non-Zero ==> Abnormal Termination
                   -> This status code internally used  
           "NOTE"  -> Whether it is 0 or non-zero there is no difference in result of the program..
                      ie. PVM will be shutdown..
               
             Example:
                      try:
                          print("try")
                          os._exit(0)  # PVM will be shutdown from this point and no futher statements will be executed
                      except ZeroDivisionError:
                          print("except")
                      finally:
                          print("finally")  
                        
                     # O/P:
                        try
             
                OR  " No matter , If there is default except block"   
                      try:
                          print("try")
                          os._exit(0)  # PVM will be shutdown from this point and no futher statements will be executed
                      except:# default except block
                          print("except")
                      finally:
                          print("finally")  
                        
                     # O/P:
                        try
                
                   
                   
        # VVVI 
        14)  Interveiw question : 
         As,both is used for cleanup activiteies...    
                -> Finally block meant for maintaing cleanup code.
                -> Destructor meant for mainataing  cleanup code.
                
        "VVI" # Q1) Differance between finally block vs Destructor ?
                -> Difference is     
                -> finally block meant for cleanup activities realated to try block.
                   i.e whatever resourses we opened as the part of try block will be closed inside finally block.
                -> destructor meant for cleanup activities related to object.
                   whatever resourses associated with the object should be deallocated
                   inside destructor,which will be executed before destroying object.
                   
                 
         
         15)  Control flow in try-except-finally :
         
                try:
                    stat-1  # Statements
                    stat-2
                    stat-3
                except XXX:
                    stat-4
                finally:
                    stat-5
                stat-6
                
                
                case 1: If there is no exception...
                        # Statement 1,2,3,5,6 will be executed
                        # Normal termination
                
                case 2: If an exception is raised at stat-2 and corresponding except block matched...
                         Statement 
                         # Statement 1,4,5,6 will be executed
                         # Normal termination
                         
                case 3: If an exception raised at stat-2 but corresponding except block not matched...
                         # Statement 1,5 will be executed
                         # Abnormal termination
                         
                case 4: If an exception raised at stat-4 ...
                         # Statement 1,2,3,5 will be executed
                         # Abnormal termination
                         
                case 5: If an exception raise at stat-5 or stat-6 ...
                         # then it is always abnormal termination
             
             


                
          16) Nested try-except-finally blocks:
            
  'NOTE'    -> We take ' more risky code inside nested try-except-finally block ' 
               becoz, if its except block cant handle the code then...
               there is outer except block to handle...
            
   'VVVI'   -> If an exception is raised in outer except or outer finally block
               then, it will be always Abnormal termination...
               As , there will be no except block to handle the exception..   
            
            -> try-except-finally inside outer try block,
               try-except-finally inside outer except block,
               try-except-finally inside outer finally block..
               possible...
            like ...
               try:
                   try:
                   except:
                   finally:
               except:
                   try:
                   except:
                   finally:
               finally:
                   try:
                   except:
                   finally:
                            
   'NOTE'    -> if control not entered in the try block,then corresponding finally
                block wont be executed.
                
             -> Once control entered in the try block, compulsory the corresponding finally 
                block will be executed.
                
             -> Control flow  in nested try-except-finally :

                try:
                    stat-1
                    stat-2
                    stat-3
                    try:
                        stat-4
                        stat-5
                        stat-6
                    except XXX:
                        stat-7
                    finally:
                        stat-8
                    stat-9
                except YYY:
                    stat-10
                finally:
                    stat-11
                stat-12
                
                
                case 1: If there is no exception...# Only except block wont be executed
                        # Statement 1,2,3,4,5,6,8,9,12,11 will be executed
                        # Normal termination
                
                case 2: If an exception is raised at stat-2 and corresponding except block matched...
                         Statement 
                         # Statement 1,10,11,12 will be executed
                         # Normal termination
                         
                case 3: If an exception raised at stat-2 but corresponding except block not matched...
                         # Statement 1,11 will be executed
                         # Abnormal termination
                         
                case 4: If an exception raised at stat-5 and inner except block matched ...
                         # Statement 1,2,3,4,7,8,9,11,12 will be executed
                         # Normal termination
                         
                case 5: If an exception raise at stat-5 and inner except block not matched but outter except block matched ...
                         # Statement 1,2,3,4,8,10,11,12 will be executed
                         # Normal termination
                
                case 6: If an exception raise at stat-5 and both inner and outter except block not matched ...
                         # Statement 1,2,3,4,8,11 will be executed
                         # Abnormal termination
                         
                case 7: If an exception is raised at stat-7(Inner except block) and corresponding except block matched...
                         # * - problem may be raised at 4,5,6 therefore they may or may not execute
                         # Statement 1,2,3,*,*,*,8,10,11,12 will be executed
                         # Normal termination
                         
                case 8: If an exception raised at stat-7(Inner except block) but corresponding except block not matched...
                         # * - problem may be raised at 4,5,6 therefore they may or may not execute
                         # Statement 1,2,3,*,*,*,8,11 will be executed
                         # Abnormal termination
                         
                case 9: If an exception is raised at stat-8(Inner finally block) and corresponding except block matched...
                         # * - Assuming there is no exception raised at 4,5,6,7 or exception raised at 4,5,6
                         # Statement 1,2,3,*,*,*,*,10,11,12 will be executed
                         # Normal termination
                         
                case 10: If an exception raised at stat-8(Inner finally block) but corresponding except block not matched...
                         # * - Assuming there is no exception raised at 4,5,6,7 or exception raised at 4,5,6
                         # Statement 1,2,3,*,*,*,*,11 will be executed
                         # Abnormal termination
                         
                case 11: If an exception is raised at stat-9 and corresponding except block matched...
                         # * - 4,5,6,7 may or may not execute depending upon exception raised or not..
                         # Statement 1,2,3,*,*,*,*,8,10,11,12 will be executed
                         # Normal termination
                         
                case 12: If an exception raised at stat-9 but corresponding except block not matched...
                         # * - 4,5,6,7 may or may not execute depending upon exception raised or not..
                         # Statement 1,2,3,*,*,*,*,8,11 will be executed
                         # Abnormal termination

                case 13: If an exception raised at stat-10(outer except block)
                         # Its is always Abnormal termination, only finally block will be executed
                         As ,if an exception is raised in outer except or outer finally block
                         then, it will be always Abnormal termination...
                         becoz , there will be no except block to handle the exception..
                         
                case 14: If an exception raised at stat-11 or stat-12
                         # then its is always Abnormal termination because it is not part of try block
                         
                
               

          17) else block with try-except-finally :

    " Note "  if-else: -> If condition is false then only else will be executed.

              for-else: -> If loop executed without break then only else will be executed.

              while-else: -> If loop executed without break then only else will be executed..
              
          #IMP :
                
  " NOTE "    try-except-else-finally -> If there is no exception in try block then only else will be executed..  
             
  # VVVI : else is always uesd with except...if there is no except block and we r defining else block
           # then, its a syntax error..

   # ie.. without except block there cant be else block           
             
     "VVVI" -> else block is opposite to except ie. it will be executed if there is no exception
            ->  therefore, without except block , else block cant be there.
            
              Syntax:
                        try:
                            Risky code
                        except:
                            handling code
                            will be executed if an exception inside try
                        else:
                            will be executed if there is no exception 
                            inside try block
                        finally:
                            Cleanup Code
                            will be executedd always whether exception raised or not raised
                            and handled or not handled

            
            18) Examples 1:

                try:
                    print("try")
                except:
                    print("except")
                else:  # execute if there is no exception in try block
                    print("else") # else must be with except...  
                finally:
                    print("finally")

                # O/P :
                try
                else
                finally
                
                
                Example 2:
                
                try:
                    print("try")
                    print(10/0)
                except:
                    print("except")
                else:  
                    print("else") # without except block there cant be else block
                finally:
                    print("finally")
            
                # O/P :
                try
                except
                finally
            
            
                Example 3: # Invalid Example
                
                try:  
                    print("try")
                else: #INVALID  # without except block there cant be else block
                    print("else") 
                finally:
                    print("finally")
            
                # O/P :
                try
                Syntax Error
            
        ## IMP POINTS :
        # else block with try-except-finally 
        -> there is no chance of executing both except and else simultaneouly.
        -> If we want to take else block,compulsory except block should be there,
           i.e else without except block is always invalid.
           SyntaxError: Invalid syntax
        
        -> Example where try-except-else-finally is useful :
        
           f=None
           try:
               f=open('abc.txt','r')
           except:
               print(' Some problem while locating/opening file')
           else: # will be executed when there is no exception in try block
               print('File opened successfully')
               print('The content of the file :')
               print("#"*30)
               print(f.read())
           finally:
               if f is not None: # Check whether filed is opened or not
                    f.close()
        
        
       ##VVVI 
        19) Various possible combinations of try-except-else-finally
        
        
 'VVIMP'     1)  # Invalid
                  try:
                    print('try')
            
   'NOTE'       'Invalid' : compulsarory except or finally block must be there with try
              
             2) # Invalid
                except:
                    print('except')
                       
                'Invalid': except block without try is always invalid..
                
             3) # Invalid
                else:
                    print('else')
                
              'Invalid': Compulsory except must be there with else 
                         and with except block,compulsory try must be there..

             4) # Invalid
                finally:
                    print('finally')
                       
                'Invalid': without try block finally block is invalid..
                          As finally is meant for cleanup code(resource deallocation)
                           closing connection.. and without opening connection in try block
                           there is no possibility of closing..
                
             5) # Valid
                try:
                    print('try')
                except:
                    print('except')
                
                "Valid"
              
             
 'VVVIMP'    6) # Invalid
                try:
                    print('try')
                else:
                    print('else)
                
              "Invalid" : else without except is always invalid
              
              
 'VVIMP'    7) # Valid
                try:
                    print('try')
                finally:
                    print('Finally')
                
                  " Valid " 

 'VVVIMP'   8) # Invalid
                try:
                    print('try')
                else:
                    print('else')
                except:
                    print('except')
                    
            "Invalid" : except must be before else block, order is important..
                        Order : try-except-else-finally
            
'VVIMP'     9) # Invalid
                try:
                    print('try')
                else:
                    print('else')
                finally:
                    print('finally')
                    
            "Invalid" : else without except is invalid
            
            10) # Valid
                try:
                    print('try')
                except:
                    print('except')
                else:
                    print('else')
                finally:
                    print('finally')
                    
              " Valid " 
            
 'VVIMP'    11) # Valid
                try:
                    print('try')
                except:
                    print('except')
                try:
                    print('try')
                finally:
                    print('finally')
                    
              " Valid "
        
 'VVIMP'    12) # Invalid
                try:
                    print('try')
                except:
                    print('except')
                else:
                    print('else')
                else:
                    print('else')
                    
              " Invalid " : More than one else blocks is not possible...
                            but More than one except blocks are possible
                            
 'VVIMP'    13) # Invalid
                try:
                    print('try')
                except:
                    print('except')
                finally:
                    print('Finally')
                finally:
                    print('Finally')
                    
              " Invalid " : More than one finally blocks is not possible...
                            Only, More than one except blocks are possible
       
 'VVIMP'    14) # Invalid
                try:
                    print('try')
                print('Hello')
                except:
                    print('except')
                    
              " Invalid " : try-except-else-finally must be in continuation..
                            there must be no statements between try-except-else-finally
       
 " VVVVVI"  15) # Valid
                try:
                    print('try')
                    print(10/0)
                except ZeroDivisionError:
                    print('except1')
                except:
                    print('except2')
                else:
                    print('else')

                "Valid" : multiple except are valid
                          but, only one else is valid
                
                # try will be executed if there is no exception raised in try block

"VVI"       16) # Invalid
                try:
                    try:
                        print('try')
                except:
                    print("Outer except")
                
                " Invalid ": try must be with finally or except... try can not be alone...
            
            17) # Valid
                try:
                    try:
                        print('try')
                    finally:
                        print('finally')
                except:
                    print("Outer except")
                
                " Valid "
                
                
                
                
            ### Conclusions :

            1) whenever we are writing try block, compulsory we should write except or finally blocks.
                ' ie. try without except or finally is always invalid.' 
           
            2) whenever we are writing except block, compulsory try block should be there.
                ' ie. except without try is always  invalid'

            3) Whenever we are writing finally block,compulsory try block should be there..
                ' ie. finally without try is always invalid'
           
            4) Wherever we are writing else block, compulsory except block should be there.
                ' ie. else without except is always invalid' 
        
            5) We can write multiple except blocks for the same try...
                but we cannot write multiple else blocks and finally blocks.
           
            6) In try-except-else-finally order is important.

            7) We can write try-except-else-finally inside try,except,else and finally blocks.
               Hence nesting of try-except-else-finally is always possible.        
        
        
        

     # VVVI   
     20)   Types of Exceptions - Predefined and user defined
     
              1) Predefined Exceptions : Also known as inbulit exceptions or pvm exceptions.
                                         
                                        -> These will be raised automatically by python virtual machine whenever a 
                                           particular event occurs.
                                           
                                        -> Example 1 :
                                            
                                           print(10/0) # ZeroDivisionError
                                            
                                        -> Example 2 :
                                            
                                           x=int('ten') # ValueError     
              
              2) User defined exceptions:  Also known as customized exceptions or programmatic exceptions..
              
                                        -> Sometimes we have to define and raise exceptions explicitly to indicate that
                                           something goes wrong, such type of exceptions are called user defined exceptions
                                           or Customized exceptions or programmictic exceptions.
                                           
                                        -> Programmer is responsible to define these exceptions and python virtual machine not having
                                           any idea about these. 
                                           Hence we have to raise explicitly based on our requirement by using 'raise' keyword.
                                           
                                        -> InSuficentFundsException # While performing withdraw operation in bank
                                        -> InvalidPINException # while tring mutiple attempts im mobile recharge cupon codes
                                        -> TooYoungException# Matrimonial application
                                        -> TooOldException# Matrimonial application                
                
                
     21)  How to define and raise customized exceptions :
     
          -> Every exception in python is a class and it should be child class of BaseException.
          ->  Syntax:
                class NameofException(PredefineException):
                    def __init__(self,msg):
                        self.msg=msg
                        
          -> Example: 
            
                    class TooYoungException(Exception):
                            def __init__(self,msg):
                                self.msg=msg
                                
         -> TooYoungException is our exception class name and it is the child class of exception.
         
         -> We can raise exception by using 'raise' keyword.
         -> raise TooYoungException('message')
         -> Example:
            # Matrimonial Application
            class TooYoungException(Exception): # child class of Exception class
                  def __init__(self,msg): # msg for discription of exception
                        self.msg=msg
            
            class TooOldException(Exception):   # child class of Exception class 
                  def __init__(self,msg):
                        self.msg=msg

            age=int(input('Enter age'))
            if age>60:
                raise TooYoungException('Please wait some more time, defintly u will get best match')
            elif age<10:
                raise TooYoungException('Already crossed marage age, No chance of getting married')
            else:
                print('You will get match details by email')
            
            
            
#########################################################################################################################################################################################