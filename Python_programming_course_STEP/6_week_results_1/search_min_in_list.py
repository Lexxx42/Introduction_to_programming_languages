# search for min in the list

a = [5, 8, 4, 3, 5, 7]

min_a = a[0]
for i, item in enumerate(a):
    if item < min_a:
        min_a = item
print(min_a)