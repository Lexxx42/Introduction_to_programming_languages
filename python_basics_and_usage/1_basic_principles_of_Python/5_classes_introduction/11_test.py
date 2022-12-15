# Какие числа будут выведены в результате выполнения данного кода?

class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()  # 1
b = A()  # 1

a.bar()  # 2
a.foo()  # 3

c = A()  # 3

print(a.val)  # 2
print(b.val)  # 3
print(c.val)  # 3
