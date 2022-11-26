number = 119
summ = 0
while number > 9:
    summ += number % 10
    number = number//10
summ += number
print(summ)
