number_of_iterations = int(input())
count = 1
x = input()
result = f(int(x))
print(result)
results = {x: result}

while count < number_of_iterations:

    x = input()
    count += 1

    if x not in results.keys():
        result = f(int(x))
        print(result)
        results[x] = result
    else:
        print(results[x])
