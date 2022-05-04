##################################### Logging #############################################

    1) Python Logging : # logging module
                     -> It is highly recommended to store complete application
                        flow and exception information to a file.
                        This proccess of writing data to the file is called logging.
                        
           # The main advantages of logging are:
           ->  we can use log files while performung debugging.
           -> We can generate utilization reports like 
              no of requests per day etc.
              
  
    2) 6 Logging Levels : Can also be represented by corresponding integer numbers.
        # 6 Variables in logging module
        # 1-5 VVVI 
        1. CRITICAL(50):
            Represents a very seroius problem that needs high attention like ' Complete Application Failure'.
            
        2. ERROR(40) :
           Represents a serious error. Some part of the application not working properly.
           
        3. WARNING(30) :
           Represents a warning message, some caution needed. It is alert to the programmer.
           
        4. INFO(20) :
           Represents a message with some important information.
           
        5. DEBUG(10):
           Represents a message with debugging information.
           
        6. NOTSET(0):
           Represent that level is not set.
           
           
    3) How to implement logging :
    
      Q1) Write a python program to create a log file and write WARNING 
          and Higher level messages ?
      -> import logging
         logging.basicConfig(filename='log.txt',level=logging.WARNING) # WARNING and Higher level messages will be stored in log.txt
         # or  logging.basicConfig(filename='log.txt',level=30)
         print('logging Demo')
         # To store msgs in log file, only warning and higher level messages will be stored
         logging.critical('this is critical message') # msg will be stored in log file
         logging.error('this is error message') # msg will be stored in log file
         logging.warning('this is warning message') # # msg will be stored in log file
         logging.info('This is info message') # this will not be stored
         logging.debug('This is debug message') # this will not be stored
         
         # log.txt
         # CRITICAL:root:this is critical message
         # ERROR:root:this is error message
         # WARNING:root:this is warning message