a = []
print(a,id(a))
a += [1]
print(a,id(a))
a += [2]
print(a,id(a))
a = []
print(a,id(a))
a = a + [1]
print(a,id(a))