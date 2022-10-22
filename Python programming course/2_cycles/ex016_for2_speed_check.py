# sum of odds


import time




a, b = input().split()

start_time = time.time()
a = int(a)
b = int(b)
sum = 0
for i in range(a, b+1):
    if i % 2 == 0:
        continue
    else:
        sum += i
finish_time = time.time()
print("sum of odds =", sum, "time=", finish_time-start_time)


a, b = input().split()

start_time = time.time()
a = int(a)
b = int(b)
sum = 0
if a % 2 == 0:
    for i in range(a+1, b+1, 2):
        sum += i
else:
    for j in range(a, b+1, 2):
        sum += j
finish_time = time.time()
print("sum of odds =", sum, "time=", finish_time-start_time)
