# 2. Напишите программу для проверки ложности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def check_for_falsity(x, y, z):
    print('X', 'Y', 'Z', 'L', 'R', 'S', sep='\t')
    for i in range(len(x)):
        left = x[i] or y[i] or z[i]
        right = not x[i] and not y[i] and not z[i]
        s = left != right
        print(f'{(x[i])}', f'{(y[i])}', f'{(z[i])}', left, int(right), int(s), sep='\t')


def value_input():
    x = [0, 0, 0, 0, 1, 1, 1, 1]
    y = [0, 0, 1, 1, 0, 0, 1, 1]
    z = [0, 1, 0, 1, 0, 1, 0, 1]
    check_for_falsity(x, y, z)


print("This program checks if the ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z assertion is false for all values of the predicate")
print('L: (¬X ⋀ ¬Y ⋀ ¬Z)', 'R: (¬X ⋀ ¬Y ⋀ ¬Z)', 'S: (X ⋁ Y ⋁ Z) != (¬X ⋀ ¬Y ⋀ ¬Z)', '\n')
value_input()
