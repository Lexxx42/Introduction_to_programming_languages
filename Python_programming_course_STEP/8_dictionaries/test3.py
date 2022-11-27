n = int(input())
count = 1
x = input()
result = f(int(x))
print(result)
results = {x: result}
while count < n:
    x = input()
    count += 1
    if x not in results.keys():
        result = f(int(x))
        print(result)
        results[x] = result
    else:
        print(results[x])
