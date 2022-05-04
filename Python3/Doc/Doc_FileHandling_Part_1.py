########################################## File Handling ##########################################

# File Handling

           1) Whatever data stored in python collections like list,set,dict etc, is ' temporary '.
              Once PVM shutdown, all these objects will be destroyed and data will be gone.

           2) Sometime, our programming requirement is to store our data 'permanently' for future purpose.
              To store data permanently the following are various possiblities :

                1) 'File'
                2) 'Database'
                3) More Advance storage areas like 'Big Data'
               
             Files are very common permanently storage areas to store our data permanently.  
             
             
           3) Types of files : There are 2 types of files :

                1) 'Text files': We can use text files to store character data/text data.
                                  Eg: abc.txt,test.py
                                
                2) 'Binary Files' : We can use binary files to store binary data like images,video files,audio files etc..
                                    ex: guido.jpg , baahubali.mp4
                                    
                                    
                                    
                                
           4) Opening a file :  Using pythons in-build function 'open()' 
                               # Syntax: f=open(filename,mode)
                                ex: f=open('abc.txt','r') # Open file in read mode
                   
                -> Various Modes to open a file : 
                
                   # There are 7 modes for text file: r,w,a,r+,w+,a+,x
                   # There are 7 modes for Binary file: rb,wb,ab,r+b,w+b,a+b,xb
                   
               ' VVVI NOTE ' # Modes for binary files are same as text file 
                             # But, U just haveto suffixed it with 'b' but rules remains the same...
                             like => rb,wb,ab,r+b,w+b,a+b,xb .
                  
                 1) 'r' ----> read :
                     -> Open an existing file for read operation.
                     -> File pointer is always positioned at beginning of the file.
                     -> If specific file does not exist then we will get FileNotFoundError.
                     -> This is default mode.
                   'NOTE':# Same rules for rb mode in binary   
                     
                     
                 2) 'w' ----> write : # Overwrite previous data   
                     -> Open an existing file for write operation.
           'Note'    -> If the file already contains some data then' that data will be over-written'.
                     -> If the specific file is not already available, 
                        then this mode will create that file.
                   'NOTE':# Same rules for rw mode in binary         
                    
                 3) 'a' ----> append : # over-write wont happen
                     -> Open an existing file for append operation.# It is also to write data in file but doesnot overwrite the content.
            'Note'   -> It wont over-write existing data.
                     -> If specific file is not already available then this mode will create that file.
                    'NOTE':# Same rules for ab mode in binary
                    
                 4) 'r+' ----> read & write : # first read then write, here, while performing write data it will over-write the previously exixting content
                     -> To read and write data to the file .
             'Note'  -> The file pointer is placed at beginning of the file.
             'Note'  -> While writing old data ,will be over-written
                     -> If specific file does not exist then we will get FileNotFoundError.
                        This mode wont create any new file.
                     'NOTE':# Same rules for r+b mode in binary
                     
                 5) 'w+' ----> write & read : # first write then read, here, while performing write operation it will over-write the data..
                     -> To write and read data.
             'Note'  -> It will overwrite existing data.
             'Note'  -> If the specific file is not already available, 
                        then this mode will create that file.
                     'NOTE':# Same rules for w+b mode in binary   
                     
                 6) 'a+' ----> append & read : # First append , then read, here,while performing write operation it will not over-write the previous content...
                     -> To append and read data from the file.
            'Note'   -> It wont over-write existing data.
                     -> If specific file is not already available then this mode will create that file.
                     'NOTE':# Same rules for a+b mode in binary   
                        
                 7) 'x' ----> Exclusive # also meant for write operation only
                     -> To open a file in exclusive creation mode for write operation.
            'Note'   -> If the ' file already exists' then we will get FileExistsError.
                        (ie. file should not be already there)
                    -> Always creayes a new file for writing..
                    'NOTE':# Same rules for xb mode in binary
            
           
           5)Closing a file :
           
                  1) After completing our operations on the file, it is highly recommended to close the file.
                     bcoz while opening a file certain system resourses are allocated,due to which performance can degrade
                     So closing will deallocate the system resource. thus , performace can be improved
                     for this we have to use close() method
    'VIIMP'       -> Whenever we are closing the file, all system resourses which are associated with that file will be released.
                     If we are not closing the file, then there may be performance issues.
                   
                   
                    # f.close()
                  ex: f = open('abc.txt','mode') # Perform read and right operation
                      f.close()
                           
           
            6) Various properties of File object :
            
                    -> Once we opened a file, we will get File object. 
                       We can get various details related to that file by using the following
                       attributes and methods.
                       
                       Ex: f=open('abc.txt','w')
                        
                       # Variable 
                       1) f.name ---> Name of the opened file.
                       2) f.mode ---> Mode in which the file is opened
                       3) f.closed ---> returns boolean value indicates that whether the file is closed or not.
                       # Methods
                       4) f.readable() ---> returns boolean value indicates that whether the file is readable or not.
                       5) f.writable() ---> returns boolean value indicates that whether the file is writable or not.
              
            7) # Write Dynamic Data(through keyboard) to Dynamic File
                    fname = input('Enter file Name: ')
                    f = open(fname,'w') # 'w' - If file is not there, will create new file
                    while True:
                        data = input('Enter Data to Write : ')
                        f.write(data+'\n') # Adding newline character after each input from the user
                        option = input('Do u want to add some more data[Y|N]:')
                        if option.lower()=='n':
                            break
                    f.close()
                    print('Data written to the file successfully') 


'IMP'       8) Reading Character data from text files - read(),read(n),readline(),readlines()
                    
                  -> We can read character data from a text files by using the following methods:
                     
                     # f = open('abc.txt','r')
                    1) f.read() ---> To read total data from the file.
                      Ex:  f = open('abc.txt','r')
                           data=f.read()
                           print(data)
                           f.close()
                       
                    2) f.read(n) ---> To read 'n' characters from the file.
                      Ex:  f = open('abc.txt','r')
                           data=f.read(10) # to read 10 characters
                           print(data)
                           f.close()
                    
                    'NOTE' : If specfic no. of character(ie. n ) > Total character of the file
                             then, all characters will be read...
                           -> ie if n > total no character present in file  
                           Ex: data = f.read(10000000000) # file has only 3 characters
                           # Here, all characters will be read 
                     
                    'NOTE' : If n is negative, then also it will read all characters present inside the file.    
                            ex: data= f.read(-1) # Here, all characters will be read
                    
                    3) f.readline() --> To read only one line
                    
                      'NOTE': If control reaches 'end of file'(ie if there is no next line in the file)
                              then ' readline() method returns empty string'
                      
                       Ex 1: # Content of abc.txt(mobile nos.)
                           # 9812334561
                           # 7777777777
                           # 4812364565
                           # 8888888888
                           f = open('abc.txt','r')
                           line1=f.readline() # to read first line
                           print('First Mobile no. :',line1,end='') # as line already has \n ,and print() will also add \n, therefore end='' for not printing \n
                           line2=f.readline()
                           print('Second Mobile no. :',line2,end='')
                           line3=f.readline()
                           print('Third Mobile no. :',line3,end='')
                           f.close()
                    
  'VVVVVI'               Ex 2: # Read complete data line by line using readline()
                            f = open('abc.txt','r')
                            line=f.readline() # to read first line
                            while line != '': # Check if line is not empty
                                print(line,end='')# line already contain '\n',
                                line=f.readline()
                            f.close() 
                                
                    
                     4) f.readlines() ---> To read all lines into a list
                     
                     Ex: # Content of abc.txt
                         #Sunny
                         #Bunny
                         #Chinny
                     f=open('abc.txt','r')
                     l=f.readlines() # To read all lines into a list
                     for line in l:
                        print(line,end='') # Line already has '\n' 
                     f.close()
                     
                     # O/P :
                             ['Sunny\n','Bunny\n','Chinny\n']
                     
                     
 'VVVI'      9)# Write a program to read data from one file(input.txt) and write to another file(output.txt) ?
               
               #Content in input.txt
               #Sunny
               #Bunny
               #Chinny 
               fin = open('input.txt','r')
               fout = open('output.txt','w')
               data = fin.read()
               fout.write(data)
               fin.close()
               fout.close()


 'VVVVI'     10) Opening a file using with Statement : # Can be used to close a file automatically when control reaches end of with block
                            
                          Syntax:  with open('abc.txt','w') as f:
                                        ......
                                        ......
                                        ......
                                        ......
            
            
                          -> The with statement can be used while opening a file.
                             We can use this to group file operation statements within a block.
                             
                          -> Advantage :
                                  
                     'NOTE'    1) It will take care of closing of file automatically once 
                                  control reaches end of with block.
                               
                     'NOTE'    2) Even, in the case of Exceptions also, file will be closed Automatically
                                  And,we are not required to close explicitly.
            
                           
                          ->  Example : 
                          
                                        with open('abc.txt','w') as f:
                                                    f.write('Sunny\n')
                                                    f.write('Bunny\n')
                                                    f.write('Chinny\n')
                                                    print(' IS file closed: ',f.closed) # False ## Checking wheather file is closed or not
                                        print(' IS file closed: ',f.closed) # TRUE ## Checking wheather file is closed or not            
                          
                                        
        'VVVVVI'        Q1) What is the advantage of using with block while opening a file ?
                            ->  After completing our operations on the the file will be closed automatically 
                                and we are not required to close explicitly.
                                            
        'VVVVVI'        Q2) What is the differance between :
                                f=open('abc.txt','w')  and
                                with open('abc.txt','w') as f
                            ->
                                 1) f=open('abc.txt','w')    
                                    In this we have to close the file explicitly
                                 
                                 2) with open('abc.txt','w') as f:
                                    In this case we are not require to close file explicitly
                                    and it will be closed automatically.
                                
                
                11)  tell() and seek() methods:
                
                
                      1) tell() method : Returns current position of the file pointer(cursor)  
                                         from beginning of the file.
                                         
                           -> The position(index) of the first character in files is zero just like string index.
                           -> Syntax:  f.tell()
                           
                       Ex: #Content in abc.txt
                           #Durga
                           f=open('abc.txt','r')
                           print(f.tell()) # 0 --> Begning of the file
                           print(f.read(2)) # Du --> Read 2 character, file pointer will move to 'r'
                           print(f.tell()) # 2 --> index of 'r'
                           print(f.read(3)) # rga --> file pointer will move to '\n'
                           print(f.tell()) # 5
                      
                      
                      2) seek() method : # To move the file pointer to a specific position
                         "IN PYTHON3, WE CAN ONLY SEEK FROM BEGINNING"
                         
                            -> We can use seek() method to move the cursor(file pointer) to specificied location.
                             
                   'NOTE'   -> Python 2.x Terminology :
                                        
                                        f.seek(offset,fromwhere/refference) 
                               -> offset: No. of characters from the refferance, where file pointer is to be moved
                               -> reffrence: From where / refferance to move offset        
                                  -> 0 ---> From beginning of file(default value)
                                  -> 1 ---> From current position
                                  -> 2 ---> From end of the file
                               -> Ex:f.seek(10,0) # Move file pointer to 10 character from begging of the file          
                                    
                                         
              'VVVVVI'      -> Python 3.x Terminology :
                               
                               -> Only zero allowed in python 3 as a refferance/fromwhere
               'VVI'           -> Hence, we can always seek only from beginning of the file.
                               
                               -> f.seek(3) # Move file pointer to 3 characters from beginning 
                               
                              "IN PYTHON3, WE CAN ONLY SEEK FROM BEGINNING"



            12) How to check whether the given file exists or not ?
            
                -> We can use os library to get information about files in our computer.
                   we can check whether a particular file exists or not by using isfile() function.
                
 "NOTE"         ->  os.path.isfile(fname)
                    # Returns TRUE if file exists else return false


  'VVI'     Q1: Write a program to check whether the given file exists or not.
                if its available then print its content ?
            -> 
                import os
                fname=input('Enter file Name: ')
                if os.path.isfile(fname):
                    print('File Exist:',fname)
                    f=open(fname,'r')
                    text=f.read()
                    print('The content of the file is:')
                    print('*' * 40)
                    print(text)
                    print('*' * 40)
                else:
                    print("File does not exist:",fname)
  
  
  
  'VVI'     Q2: Program to print number of lines,words and charaters present in the given file ?
            ->
            # Program to print number of lines,words and charaters present in the given file ?    
            import os
            fname=input('Enter file Name: ')
            if os.path.isfile(fname):
                print('File Exist: ',fname)
                lcount=wcount=ccount=0 # line,word,character count 
                f=open(fname,'r')
                for line in f:
                    lcount=lcount+1
                    no_of_words_in_current_line=len(line.split()) # No. of words in current line
                    wcount=wcount+no_of_words_in_current_line
                    no_of_characters_in_current_line=len(line) # '\n' will also be included ,string length of line will be No of characters present in given line.. 
                    ccount=count+no_of_characters_in_current_line
                    
                print('The number of Lines:',lcount)    
                print('The number of Words:',wcount)
                print('The number of Characters:',ccount)
            else:
                print("File does not exists: ",fname)
            
             
                
                
         13) Handling Binary Files :
                    # Handling binary data    
                    f1=open('durgasoftguido.jpg','rb')
                    data=f1.read()
                    print(type(data)) # bytes
                    f2=open('udemyguido.jpg','wb')
                    f2.write(data)
                    print('udemyguido.jpg image is ready')
                    f1.close()
                    f2.close()

         
 'VVVI'  14) Handling CSV files :
 
                 ' CSV '  ==> ' Comma Separated Values'   
        " A group of records in  
             " tabular form  
             (Like excel file)
              
            -> As the part of programming, it is very common requirement to write
               and read data to/from csv files.
               
            -> Python provides csv module to handle csv files.
                      
'VVVVVVI'   -> Writing data to csv file :  # By using csv writer object
               ----------------------------
               For witing into the csv file,we need 'csv writer object' pointing to CSV file which will perform CSV write operations. 
               # csv writer object is use to write data in csv file 
                'NOTE : FOR WRITING DATA , CSV WRITER OBJECT IS REQUIRED'
               
                " Example :  
                w = csv.writer(f) # Returns writer object to write data 
                print(type(w)) # <class '_csv.writer'>
            
                  -> Write Example : 'NOTE : FOR WRITING DATA , CSV WRITER OBJECT IS REQUIRED'
                    # Writing Data  to csv file
                    import csv
                    with open('emp.csv','w',newline='') as f:#newline='' # To,not to include new(empty) row after adding new row; As by default, when we add row to csv , it will empty extra row between every two rows
                            w = csv.writer(f) # Creating csv writer object 
                            w.writerow(['ENo.','EName','ESal','EAddr'])
                            while True:
                                eno= int(input('Enter Employee Number'))
                                ename= input('Enter Employee Name')
                                esal= float(input('Enter Employee Salary'))
                                eaddr= input('Enter Employee Address')
                                w.writerow([eno,ename,esal,eaddr])
                                option=input('DO u want to insert one more record [Yes|No]:')
                                if option.lower()=='no':
                                    break
                    print('Writing data to the file completed successfully')
                    
            
            -> Reading data from csv files: # by using csv reader object
               ----------------------------
                ' Example :
                r=csv.reader(f) # Returns reader object to write data
                print(type(r)) # <class '_csv.reader'>
                data=list(r) # converting reader objectinto list object which will contain nested list constaing rows..
                print(data) # Return nested list containg rows
                # List inside list
                # [ ['ENo.','EName','ESal','EAddr'],
                #    [101,'Sunny',1000,'Pune']
                #    [102,'Bunny',2000,'Satara']
                #    [103,'Chinny',3000,'Mumbai']
                # ]
         
                Read Example :'NOTE : FOR READING CSV FILE , READER Object IS REQUIRED '
                # Reading Data from csv file
                import csv
                with open('emp.csv','r') as f:
                        r=csv.reader(f) # returns csv reader object
                        # print(type(r)) # <class '_csv.readerer'>
                        data=list(r)
                        for row in data:
                            for column in row:
                                print(colunm,'\t',end='')
                            print()
                # OUTPUT:
                # -------    
                  ENo.  EName   ESal    EAddr
                  101   Sunny   1000    Pune
                  102   Bunny   2000    Satara
                  103   Chinny  3000    Mumbai





          15) Zipping and Unzipping File :
              ' MODULE : zipfile '
              ' Class  : ZipFile         '
              #(Grouping multiple files into a single entity)
                It is very common requirement to zip and unzip files.
              
              The main advantages :
              
              1) It is very convenient to use
              2) To impore memory utilization
              3) We can reduce transportation/transfer time
              4) Wecan improve performance etc.
              
              
            ->   To perform zip and unzip operations ,python contains one 
                 inbuilt module 'zipfile'. This module contain a class 'ZipFile'
                 ' MODULE : zipfile '
                 ' Class  : ZipFile '         
                              
                              
                              
                              
                              
                              