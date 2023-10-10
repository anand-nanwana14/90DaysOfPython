a = input("Enter any no. : ")
print(f"Multiplication table of {a} is :")
try:
 for i in range(1 ,11):
    print(f"{int(a)} X {i} = {int(a)*(i)} ")
except:
  print(f"Eroor!! There is no multiplication table of {a}")  