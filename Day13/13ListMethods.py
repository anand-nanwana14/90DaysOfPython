l = [51,42,32,24,5,5]

l.reverse()
print(l)
l.append(7)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
print(l.index(7))
print(l.count(5))
m = l.copy()
m[0] = 0
print(l)
print(m)
l.insert(1, 24)
print(l)
l.extend(m)
print(m)
print(l)
k = l + m
print(k)
