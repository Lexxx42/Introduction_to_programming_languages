# Какие числа будут выведены в результате выполнения данного кода?


class A:
    def __init__(self, val=0):
        self.val = val

    def add(self, x):
        self.val += x

    def print_val(self):
        print(self.val)


a = A()  # a=0
b = A(2)  # b=2
c = A(4)  # c=4
a.add(2)#a=2
b.add(2)#b=4

a.print_val()
b.print_val()
c.print_val()

# answer: 2,4,4