
print("This program prints the table of multiplicativity from 2 to 10")

def mult():
    for i in range(2,10):
        for j in range(2,10):
            print(i,'x',j,'=',i*j)
        print()
mult()
