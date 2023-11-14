import os
if (not os.path.exists("Data")): 
 os.mkdir("Data")

for i in range(1,90):
 os.mkdir(f"Data/Day{i}")

# if (os.path.exists("Data")):
#  for i in range(1,11):
#   os.rmdir(f"Data/day{i}")
#   if i == 5:
#    break
# print(os.getcwd())
# folders = os.listdir("Data")
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"Data/{folder}"))
