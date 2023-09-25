a = int(input("Enter a Number: "))
if (a>0):
    if (a<=10):
        print("No. is b/w 1-10")
    elif (a>10 and a<20):
        print("NO. is b/w 10-20")
    else:
        print("No. is greter than 20")    
elif (a==0):
    print("NO. is zero")
else:
    print("No. is negative")
print("Done Analysing")
