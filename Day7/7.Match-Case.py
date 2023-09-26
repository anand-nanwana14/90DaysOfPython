print("Caste Your Vote")
print("1. BJP")
print("2.Congress")
print("Type no. of your respective party")
x = int(input("Enter Your Value: "))

match x:
    case 1:
        print("You have voted for BJP")
    
    case 2:
        print("You have voted for congress")
    
    case _:
        print("You have voted for others")

