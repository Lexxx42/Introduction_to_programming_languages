def f(x):
    return x + 2


n = int(input())
number = int(input())
result = f(number)
d = {number: result}
print(result)
while len(d) < n:
    temp = int(input())
    number = temp
    result = f(temp)
    d[temp] = result
    print(d[temp])
