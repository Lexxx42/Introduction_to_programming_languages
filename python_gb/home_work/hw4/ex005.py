# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def main():
    print(
        "Given two files, each of which contains a record of the polynomial. "
        "The task is to generate a file containing the sum of polynomials")
    with open('ex004.txt', 'r', encoding='utf-8') as file1, open('ex005.txt', 'r', encoding='utf-8') as file2:
        content_file1 = []
        content_file2 = []
        for line in file1:
            line = line.strip()
            content_file1.append(line)
        for line in file2:
            line = line.strip()
            content_file2.append(line)

    with open('ex005_save.txt', 'w', encoding='utf-8') as file3:
        for i in range(len(content_file1)):
            file3.write(content_file1[i] + ' + ' + content_file2[i] + '\n')
