# Катя узнала, что ей для сна надо XX минут.
# В отличие от Коли, Катя ложится спать после полуночи в HH часов и MM минут.
# Помогите Кате определить, на какое время ей поставить будильник,
# чтобы он прозвенел ровно через XX минут после того, как она ляжет спать.

# На стандартный ввод, каждое в своей строке, подаются значения XX, HH и MM.
# Гарантируется, что Катя должна проснуться в тот же день, что и заснуть.
# Программа должна выводить время, на которое нужно поставить будильник: в первой строке часы, во второй — минуты.


XX = int(input())
HH = int(input())
MM = int(input())
print((XX+HH*60+MM)//60)
print((XX+HH*60+MM) % 60)
