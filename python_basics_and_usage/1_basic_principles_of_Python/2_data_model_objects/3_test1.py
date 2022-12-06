x = [1, 2, 3]
y = x
y.append(4)  # [1,2,3,4]

s = "123"
print(id(s))
t = s
print(id(t))
t = t + "4"  # '1234'
print(id(t))
print(s)
print(t)

print(str(x) + " " + s)  # [1, 2, 3, 4] 123
