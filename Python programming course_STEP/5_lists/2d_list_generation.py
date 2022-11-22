n=3
a=[[0]*n]*n
print(a)
a[0][0]=5  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(a)  # [[5, 0, 0], [5, 0, 0], [5, 0, 0]]
print()
a = [[0]*n for i in range(n)]  # list comprehension
print()
a[0][0]=5
print(a)
a = [[0 for j in range(n)]for i in range(n)]  # list comprehension
print()
a[0][0]=5
print(a)