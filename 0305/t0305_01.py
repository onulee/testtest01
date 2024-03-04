a=[1,2,3]
b = a
b[0]=5
print(a[0]) 

c = [*a]
c[1] = 10
print(a[1])