# Определите, сколько рублей и копеек нужно заплатить за N пирожков, если пирожок в столовой стоит А рублей и В копеек.
# На вход 3 числа: рубли, копейки и количество пирожков. На выходе 2 числа: рубли и копейки.


def validation(rub, cop, cake):
    if rub <= 0 or cop <= 0 or cake < 0:
        return False
    else:
        return True


def cost_forming(rub, cop, cake):
    cop_to_rub = 0
    rub *= cake
    cop *= cake
    while cop >= 100:
        cop_to_rub += 1
        cop -= 100
    rub = rub+cop_to_rub
    return (rub, cop)


print("this program shows how many cakes you can by, and what the cost will be")
print("please enter the rub cost of the cake:")
rub = int(input())
print("please enter cop cost:")
cop = int(input())
print("please enter how many cakes do you whant to buy:")
cake = int(input())
if validation(rub, cop, cake) == False:
    print("Can't be negative! or cakes be free")
else:
    cost = cost_forming(rub, cop, cake)
    print()
    print("cost of", cake, "cakes is", cost[0], "rub", cost[1], "cop")
    print()
