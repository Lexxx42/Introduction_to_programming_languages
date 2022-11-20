x1, x2, x3 = False, True, False
print(not x1 or x2 and x3)

# 1 - not: true or x2 and x3
# 2 - and: true and false = false
# 3 - or: true or false = true
print()

x1, x2, x3 = False, True, False
print(((not x1) or x2) and x3)

