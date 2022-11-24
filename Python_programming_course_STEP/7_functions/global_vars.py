# Global variables

# def print_value():
#     print(a)  # 5
#
#
# a = 5
# print_value()


# global and local variables

def print_value():
    print(a)
    a=10
    print(a)

a= 5
print_value()  # UnboundLocalError: local variable 'a' referenced before assignment


