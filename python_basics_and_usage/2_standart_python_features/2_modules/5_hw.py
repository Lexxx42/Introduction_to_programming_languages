# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
#
# Вычислите и выведите год, месяц и день даты, которая наступит,
# когда с момента исходной даты date пройдет число дней, равное days.
#
# Примечание:
# Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и
# класс datetime.timedelta для прибавления дней к дате.
#
# Sample Input 1:
#
# 2016 4 20
# 14
# Sample Output 1:
#
# 2016 5 4
# Sample Input 2:
#
# 2016 2 20
# 9
# Sample Output 2:
#
# 2016 2 29
# Sample Input 3:
#
# 2015 12 31
# 1
# Sample Output 3:
#
# 2016 1 1


import sys
import datetime

sys.stdin = open("hw5.txt", "r")

date_imp = list(map(lambda x: int(x), input().split()))
days_imp = int(input())
current_day = datetime.date(date_imp[0], date_imp[1], date_imp[2])
delta = datetime.timedelta(days=days_imp)
final_date = current_day + delta
year = final_date.year
month = final_date.month
day = final_date.day
print(year, month, day)
