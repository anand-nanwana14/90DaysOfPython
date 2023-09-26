import time
timestamp = int(time.strftime('%H'))
timestamp = int(input("Enter Hours: "))
print(timestamp)

if (timestamp>=4 and timestamp<12):
    print("Good Morning")
elif (timestamp>=12 and timestamp<18):
    print("Good Afternon") 
if (timestamp>=18 and timestamp<24):
    print("Good Evening")
elif (timestamp>=24 or timestamp<4):
    print("Good  night")





