def func():
 try:
    l = [1,3,5,7,9]
    i = int(input("Enter the index: "))
    print(l[i])
    
 except:
    print("An error occured")
    
 finally:
    print("I am always therer 4 u")

x = func()
print(x)
    
