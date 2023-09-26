
print("Choose operation for calculator:")
print("1. ADD")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
print("5. MODULUS")
print("6. FLOOR VALUE")
print("7. EXPONENT")
operation = (int(input("Enter your choice:\n")))
print("Enter your 2 no.")
a=int(input("enter your 1st: "))
b=int(input("enter your 2nd: "))
if operation == "1":
  print(a+b)
elif operation == "2":
  print(a-b)
elif operation == "3":
  print(a*b)
elif operation == "4":
  print(a/b)
elif operation == "5":
  print(a%b)
elif operation == "6":
  print(a//b)
elif operation == "7":
  print(a**b)
else :
 print("Choice invalid")