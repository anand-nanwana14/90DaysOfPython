s1 = {1,3,5,6,7}
s2 = {3,6,7,9,11}

print(s1.symmetric_difference(s2))
print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2)
print(s1,s2)
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)

