a = int(input("Enter Value b/w 5 & 9: "))
if(a<5 or a>9):
    raise ValueError("Value Should be b/w 5 & 9")
else:
    print("Got it")