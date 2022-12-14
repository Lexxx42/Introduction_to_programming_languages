# Какие числа будут выведены в результате выполнения данного кода?

class Base:
    def __init__(self):
        self.val = 0

    def add_one(self):
        self.val += 1

    def add_many(self, x):
        for i in range(x):
            self.add_one()


class Derived(Base):
    def add_one(self):
        self.val += 10


a = Derived()  # a.val = 0
a.add_one()  # 10

b = Derived()
b.add_many(3) # b.val =30

print(a.val)
print(b.val)
