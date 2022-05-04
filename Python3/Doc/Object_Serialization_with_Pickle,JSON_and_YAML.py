########################################################################################################################################
                            Object Serialization with Pickle,JSON and YAML
                        --------------------------------------------------------
                        
                        
          1)  Object Serialization (Pickle,json,yaml) :
              -----------------------------------------
              ('Serialization' --> Process of saving an object into the file(json,pickle,yaml) 
              ('Deserialization') --> Process of reading object from the file(json,pickle,yaml)
                
                -> The process of converting an object from python supported form to either file
                    supported form or network supported form, is called 'Serialization(Marshalinng or pickling)
                
                -> The process of converting an object from either file
                    supported for or network supported form to python supported form to ,
                    is called " Deserialization(Unmarshaling or Unpickling)  
            
               
                -> Object serialization:
                    1) Object serialization by using Pickle.
                    2) Object serialization by using JSON.
                    3) Object serialization by using YAML.
          
          
                
          2) Object Serialization by using ' Pickle ' :
            ---------------------------------------
            
            'NOTE': File use to store object(binary data) can be of any type ie. any extension..
            
            # BY using pickle module
                -> dump() function used for serialization
                    'Example': 
                        e=Employee(100,'Sunny',1000,'pune')
                        with open('emp.ser','wb') as f: # wb becoz object is a binary data and file name can be anything irrespective of the type of extension
                            pickle.dump(e,f) # Serialization : storing employee object e into emp.ser file.
      
                -> load() function used for deserialization
                
                 
            
            
 







































########################################################################################################################################