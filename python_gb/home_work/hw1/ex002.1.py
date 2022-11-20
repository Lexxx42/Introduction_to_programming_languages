# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W)

def check_for_falsity(x, y, z, w):
    print('X', 'Y', 'Z', 'W', 'S', sep='\t')
    for i in range(len(x)):
        s = (w[i] and z[i]) or not y[i] or (not x[i] is not w[i])
        print(f'{(x[i])}', f'{(y[i])}', f'{(z[i])}', f'{(w[i])}', int(s), sep='\t')


def value_input():
    x = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    y = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
    z = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
    w = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    check_for_falsity(x, y, z, w)


print("This program checks if the (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) assertion is false for all values of the predicate")
print('S: (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W)', '\n')
value_input()
