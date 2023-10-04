def meancalc(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def greater(a, b):
    if(a>b):
        print("1st is greater")
    else:
        print("2nd is greater or equal to 1st") 

def percentage(a, b):
    pass            

a = 5
b = 8
c = 10
d = 15
e = 20
f = 4
meancalc(a, b)
meancalc(c, d)
meancalc(d, e)
greater(a, e)
greater(a, f)