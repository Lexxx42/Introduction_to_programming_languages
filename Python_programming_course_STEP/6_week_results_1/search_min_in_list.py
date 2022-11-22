# search for min in the list

#a = list(int(i) for i in input().split())
a = [int(i) for i in input().split()]
min_a = a[0]
for i, item in enumerate(a):
    if item < min_a:
        min_a = item
print(min_a)
print()
# simpler
min_a = a[0]
for c in a:
    if c < min_a:
        min_a = c
print(min_a)
print()
# simpler
a.sort()
print(a[0])
print()
# simpler
print(min(a))
print()
