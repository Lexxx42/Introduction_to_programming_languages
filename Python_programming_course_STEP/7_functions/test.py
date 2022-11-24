def modify_list(l):
    for j in range(len(l) - 1, 0, -1):
        if l[j] % 2 != 0:
            l.remove(l[j])
    for i, x in enumerate(l):
        if x % 2 == 0:
            l[i] = x // 2


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]
