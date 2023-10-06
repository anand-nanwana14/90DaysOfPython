tup = (1,3,5,7,9,"hello",3,1)

print(tup)
tup2 = tup[1:4]
print(tup2)

print(tup[0])
if "hello" in tup:
    print("hello sir")
else:
    print("hii")

print(tup.count(1))

tup3 = tup+tup2
print(tup3)

tup4 = list(tup)
print(tup4)

tup4.append("hello123")
tup = tuple(tup4)
print(tup)


