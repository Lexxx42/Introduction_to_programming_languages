def count_input(input_2, x):
    input_2 = input_2.lower()
    for c in input_2.split(' '):
        if c not in x:
            x[c] = 1
        else:
            x[c] += 1


d = {}
input_1 = 'a aa abC aa ac abc bcd a'
count_input(input_1, d)

for key, value in d.items():
    print(f'{key} {value}')
