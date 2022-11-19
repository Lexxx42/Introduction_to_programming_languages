from _ast import Not

print('hello world')

a = 123
b = 1.23
c = True
d = [1, 2, 3]
print(a, b, c, d)
value = None
print(value)
print(type(value))
print(type(a), type(b), type(c))

s = 'hello world'
print(s)

#  comment

s = "hello' 'world"
print(s)
#s = 'hello" "\nworld'
#print(s)

print(a, b, s)
print('{} - {} - {}'.format(a, b, s))  # format string
print(f'{a} - {b} - {s}')  # interpolate string
print('{1} - {2} - {0}'.format(a, b, s))  # format string 0,1,2 - index

f = True
print(f)

list_1 = [1, 2, '2', 2.2, True]
col = ['hg']
print(list_1)
print(col)

print('enter the values')
#a = input()
#b = input()
#print(a, b, a+b)

#a = float(input())
#b = float(input())
#print(a, b, a+b)

a = 1.3123123
b = 3
c = round(a*b, 5)
print(c)

a = 3
a+=5
print(a)

a = 1>4
print(a)

a = 1 ==2
print(a)

a = 'hello'
b = 'hello'
print(a==b)

a = 1<3<5<10
print(a)

func = 1
T = 4
x = 2
print(func<T>(x))

f = 1>2 or 4<6
print(f)

f = [1,2,3,4]
print(2 in f)

is_odd = not f[0] %2
print(is_odd)


a = int(input('enter number a '))
b = int(input('enter number b '))
if a>b:
    print(a)
else:
    print(b)

original =23
inverted = 0
while original != 0:
    inverted = inverted*10+(original%10)
    original//= 10
print(inverted)

original =23
inverted = 0
while original != 0:
    inverted = inverted*10+(original%10)
    original//= 10
else:
    print("That's")
    print('enough')
print(inverted)

for i in 1,2,3,4:
    print(i**2)

list_1 = [1,2,3,123,4,5]
for i in list_1:
    print(i)

for i in range(5):
    print(i)

for i in range(1,5):
    print(i)

for i in range(1,10, 2):
    print(i)

for i in 'qwerty':
    print(i)

ran = range(1, 10)
print(type(ran))
numbers= list(ran)
print(type(numbers))
numbers[0]=19
print(f'{len(numbers)} len')
for i in numbers:
    i*=2
    print(i)
print(numbers)




