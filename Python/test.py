    
##################################################################################################################################################          

        # KEY POINTS 

  #a,b=[eval(x) for x in input("enter no :").split()]  # a,b= input("enter no :").split()
  #  print(a,b)
  #  print(type(a))
 
#  the sentence 'The quick brown fox jumps over the lazy frog'  --> A meaningful sentence which have all 26 alphabets within it .......

#  Anagram (these are those strings which are equal in length and have same characters) for ex. --> SILENT LISTEN  

# a=[]    # list method extend is used to extend list, but we give string as a input then each character of that string will be added in the list   
    # a.extend('hii')  #---> a=['h','i','i']
    # Extend is same as update in set

# tuple with 1 element is created as t=(10,) , as if comma is not provide it will just consider parenthesis that is used in maths ... (10)+200+3 

# Tuple packing and unpacking (also aplicable for all other data types except dictionary (key value pair)) 
  
  # packing --> to pack variables into a tuple/other data type
  
  # unpacking --> to unpack tuple element into different variables
  
  # for example:
   
    
   # packing:  a=10
             # b=20
             # c=30
             # t=a,b,c  #---> packing a,b,c,d into tuple   t=(10,20,30)          
  
  # NOTE: IF THERE IS NO PARENTHESIS IT WILL CONSIDER AS TUPLE EX: T=a,b,c,data , if t=[a,b,c,d] then it will be list
   
   # unpacking:
             # t=(10,20,30)
             # a,b,c=t   #--> a=10 b=20 c=30
             
  
  # in case of set : values given to a,b,c will be unpredictable as order is not preservved in set
                    # a=10;b=20
                    # s={a,b}
                    # a=20, b=10 ---> values can be anything (10 or 20) 

# Tuple comprehension not supported in python( As tuples r immutable) --> 
#  NOTE: It will not give error , but it will give genrator object (a type of sequence)
#    t=(x for x in range(10))


# Dictonary (Only tuple elements can be used as items in dictionary)
  # d={100:"hii",200:"heyy"}
  # To create dictionary with dict keyword 
  #  ---> dict() takes only one argument  
  
     # And that must be  list of tuples , tuples of tuples or set of tuples   
    # d=dict(20:"hi")--> INVALID  , it accepts only one argument like list of tuples
   #  like  --> d=dict([(100,'hii'),(200,'hey')])   ---> list of tuples
   #            d= dict(((100,'hii'),(200,'hey')))  ---> tuples of tuples
   #            d= dict({(100,'hii'),(200,'hey')})  ---> set of tuples
   
 # d.items()  --> returns list of tuples 
 # NOTE  : 
    #d.pop(key)  --> returns value associated with the key and will remove that item from dictionary
    #d.pop() ---> will through keyerror
    # d.popitem()----> will remove random item from dict
    # del d[key]  --> will remove the item with specific key
    # del d  ---> delete the object d (object eligible for gc(garbage collection) )
    #  d.clear()---> clear all items from dict
    #   d1=d  ---> will create refference(alasing) object d1 both having same id
       #d1=d.copy() ---> cloning (only content will be same but object will be different , id will be different)

    #d.get(key,default_value) ---> retuns value associated with key 
      # d.get(key)  if key is not found ,  returns None (by default)
      
 # VVI:  d={100:'hi',200:'hey'} 
  # Adding items to dictionary: 
  #      d[key]=value ---> in this approch if key already present , it will overwrite the value . id key not present add new item to dictionary 
  #      d.setdefault(k,v)  --->in this approch if key already present, it will not overwrite(ccontent of dict will remains the same),
  #                             old value remains the same and returns old value, 
  #                             And if key is not present then item with particular k,v will be added in dictionary
  #  For Ex:   
                # d={100:'hi',200:'hey'}  
                # d[100]='ok'
                # >>> d
                # {100: 'ok', 200: 'hey'}
                # >>> d.setdefault(100,'ohh')
                # 'ok'
                # >>> d
                # {100: 'ok', 200: 'hey'}  
                
  # d.update(d1) #only one argument  ---> to extend dictionary  , same as in set update method(can have more than one argument (sequence))  
  #                                       and in list extend method  (only one argument)       
   


#################################################################################################################################################

############ STRING BASED PROBLEMS ##########################


# a="hello world world hello"
# b=[]
# c={}
# b=a.split()
# print(b)

# for word in b:
# 	count=0
# 	for i in b:
# 		if i==word:
# 			count+=1
# 	c[word]=count
# print(c)

# for char in a:
# 	b.append(char)

# for i in b:
# 	c[i]=0;
# 	count=0
# 	for j in b:
# 		if j==i:
# 			count+=1
# 	c[i]=count

# print(c)

###################################################

#a={}

#str="hhi i am pankajjj"

#for i in str:
#    count=0
#    for j in str:
#        if(i==j):
#            count+=1
#    a[i]=count
#print(a)
            
###########################################

#str="hi pankaj hi hi it me pankaj"
#a={}
#l=str.split()
#for word in l:
#    count=0
#    for ele in l:
#        if word==ele:
#            count+=1
#    a[word]=count
#print(a)   

################################################

#s="a2c3b1"
#output=''
#for ch in s:
#  if ch.isalpha():
#    c=ch
#  else:
#    output=output+ int(ch)*c
#print(''.join(sorted(output)))      

#######################################################
 

# s="aaabbccc"
# i=0
# count=0
# pre=s[0]
# output=''
# count=0
# while i<len(s):
   # if s[i]==pre:
      # count+=1
   # else:
      # output=output+str(count)+pre
      # pre=s[i]
      # count=1  
   # if i==len(s)-1 :
      # output=output+str(count)+pre    
   # i+=1 
# print(output)

############################################################


# s='a4k3b2'  #predicted output ==> aeknbd  -->prev char + digit will get that char
# prev=s[0]
# val=0
# output=''
# i=0
# while i<len(s):
  # if s[i].isalpha():
    # val=ord(s[i])
    # prev=s[i]
  # else:
    # output=output+prev+chr(ord(prev)+int(s[i]))
  # i+=1
# print(output)
  
 
############################################################

#remove duplicate char from string

# s='paapppppannnnkkkajj'
# i=0
# output=[]
# while i<len(s)-1:
   # if s[i] not in output:
      # output.append(s[i]) 
   # i+=1
# print(''.join(output))  
   
#############################################################

#No. of occurance of each character in a string

# s='abbabbaacdcd' 
# l=[]
# i=0
# while i<len(s):
    # if s[i] not in l:
       # l.append(s[i])
    # i+=1   
# i=0
# while i<len(l):
    # print(l[i],"occurred",s.count(l[i]),"times")
    # i+=1    
    

# Same using dict
 
# s='aaabbddqwwsszzs'
# d={}
# for ch in s:
  # d[ch]=d.get(ch,0)+1 # d.get(key) will return value associate with that key 
# print(d)               # and if that key is not available it will return None
                      # # 2nd argument in d.get() is the default value that it will return if key is not found
# print(sorted(d)) # to show sorted keys..... sorted always return o/p in list                  
                 # sorting based on keys

####################################################################

# s="aabbcddeaa"  #predicted o/p -> 4a2b1c2d1e
# d={}
# output=''
# for ch in s:
   # d[ch]=d.get(ch,0)+1
# for k,v in d.items():
   # output=output+str(v)+k
# print(output)

####################################################################

#find no. of vowels present in a string

# s='pankaj iioa'
# d={}
# l=['a','e','i','o','u','A','E','I','O','U']
# for ch in s:
    # if ch in l:
       # d[ch]=d.get(ch,0)+1
# print(d)
# # Or u can print individually
# for k,v in d.items():
  # print('{} occured {} times'.format(k,v))
 
########################################################################

#find the occurance of a given substring
# s='abcdpankaj123pankajsdfghs'
# subs='Pankaj'
# count=0
# pos=-1
# i=0
# count=0
# while 1:
  # pos=s.find(subs,pos+1,len(s))
  # if pos==-1:
    # break
  # print("Substring",subs,"found at index",pos)
  # count+=1
# print(subs,"Occured:",count)

##############################################################################

# s='B4A1D3'   #Predicted o/p => ABD124
# s_alp=''
# s_dig=''
# for ch in s:
  # if ch.isalpha():
    # s_alp=s_alp+ch
  # else:
    # s_dig=s_dig+ch
# s_alp=sorted(s_alp) #sorted function returns a list
# s_dig=sorted(s_dig)
# print(''.join(s_alp + s_dig))


#################################################################################################################################################



