# Выведите таблицу размером n×n, заполненную числами от 1 до n^2
#   по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
# Sample Input:

# 5
# Sample Output:

# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

n = int(input())
a = [[0 for i in range(n)] for j in range(n)]

i = 0
j = 0
x = 1
k = 0
while x <= n * n:
    a[i][j] = x
    if i != j:
        a[j][i] = (a[k][k] + (n - k * 2) * 2) * 2 - 4 - x
    if j != n - k - 1:
        j += 1
    elif i != n - k - 1:
        i += 1
    elif x != n * n:
        k += 1
        i = j = k
        x = a[k][k - 1]
    x += 1
for i in a: print(*i)
