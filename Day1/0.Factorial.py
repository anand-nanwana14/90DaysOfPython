def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate the factorial of 5
n = int(input("Enter a no.: "))
result = factorial(n)
print(result)