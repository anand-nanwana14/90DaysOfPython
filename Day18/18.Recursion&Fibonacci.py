def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(5))



def fibo(n):
  if (n==0 or n==1):
    return n
  else :
    return(fibo(n-1) + fibo(n-2))
# nterms = int(input("How many terms? "))  
# if nterms<=0:
#   print("Enter Positive int")
# else:
    print("fibonnaci series")
print("Fibonacci series")
for i in range(5):
  print(fibo(i))
  



