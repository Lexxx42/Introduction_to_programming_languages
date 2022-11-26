n = int(input())
temp = None
for i in range(n):
    if i == temp:
        continue
    else:
        temp = int(input())
        print(f'{f(temp)}')
