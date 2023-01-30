# int A in power int B

print("This progarm takes two int numbers A and B and show the result of A ^ B")
print("Please anter number A:")
number_a = int(input())
print("Please enter number B:")
number_b = int(input())


def validation(number_for_check):
    if number_for_check < 1:
        return False
    else:
        return True


if validation(number_b) == False:
    print("Power must be natural!")
else:
    print("A ^ B =", pow(number_a, number_b))
