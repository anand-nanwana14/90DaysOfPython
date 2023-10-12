def func1():
 try:
    l = [1,3,5,7]
    i = int(input("Enter the index: "))
    print(l[i])
    
 except:
    print("An error occured")
    
 finally:
    print("I am always therer 4 u")

x = func1()
print(x)
    