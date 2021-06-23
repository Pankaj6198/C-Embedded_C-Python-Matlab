
###################### Factorial ###########################################

# without recursion

def factorial(n):
  fact=1
  num=n;
  while n>=1:
    fact=fact*n;
    n=n-1
  print("Factorial of {} = {}".format(num,fact))

factorial(5)



# with recursion

def factorial_rec(n):
  num=n;
  if n==0:
   fact=1
  else:
   fact=n*factorial_rec(n-1)
  return fact
#print("Factorial of 5 = ",factorial(5))
    # Within a range
for i in range(10):
  print("{}!={}".format(i,factorial_rec(i))) 
  
###################################################################################
  

############################### Fibonacci ##########################################

# Print fibonacci series without recursion 011235

def fibo(n):
  a,b=0,1
  c=0
  for i in range(n):
    print(c)
    a,b=b,c
    c=a+b

fibo(6)
# Print fibonacci series with recursion

n=5
def fibo(n):
  if n<=1:
   return n
  else:
   return fibo(n-1)+fibo(n-2)
    
for i in range(n):
    print(fibo(i))
