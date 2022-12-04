# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE
#
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
#
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
#
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
#
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q


def coding(str_1: str, str_new_list: list) -> list:
    count = 0
    temp = str_1[0]
    x = 0
    for i in range(len(str_1)):
        if str_1[i] == temp:
            count += 1
            temp = str_1[i]
        elif str_1[i] != temp:
            temp_index = i
            x = str_1[temp_index:]
            if x == str_1:
                return str_new_list
            break
    str_new_list.append(str(count) + temp)
    if not x:
        return str_new_list
    coding(x, str_new_list)


def decoding(string_decoding: str) -> str:
    list_decoded_repaired = []
    decoded_list = list(string_decoding)
    temp = ''
    for i in decoded_list:
        if i.isalpha():
            list_decoded_repaired.append(int(temp))
            temp = ''
            list_decoded_repaired.append(i)
        else:
            temp += i
    out_string = ''
    for i in range(1, len(list_decoded_repaired), 2):
        out_string += list_decoded_repaired[i] * list_decoded_repaired[i - 1]
    return out_string


def open_file_read(filename: str) -> list[str]:
    with open(filename) as data:
        read_info = []
        for line in data:
            line = line.strip()
            read_info.append(line)
            print(line)
    return read_info


def open_file_write(filename: str, values: str):
    is_empty = False
    with open(filename) as data:
        line = data.readline().strip()
        if line == '':
            is_empty = True
    if is_empty:
        with open(filename, 'w') as ouf:
            ouf.write(values + '\n')
    else:
        with open(filename, 'a') as ouf:
            ouf.write(values + '\n')


def main() -> None:
    # text_name_for_read = input('Enter the name of the file with the text: ')
    # text_name_for_write = input('Enter the file name to record: ')
    # text_name_for_decode = input('Enter the name of the file to decode: ')
    text_name_for_read = 'text_words.txt'
    text_name_for_write = 'text_code_words.txt'
    text_name_for_decode = 'text_code_words.txt'

    list_for_code = open_file_read(text_name_for_read)
    for i in list_for_code:
        empy_list_for_coding = []
        coding(i, empy_list_for_coding)
        coded_string = ''.join(empy_list_for_coding)
        open_file_write(text_name_for_write, coded_string)

    list_for_decode = open_file_read(text_name_for_write)
    for j in list_for_decode:
        decoded_string = decoding(j)
        open_file_write(text_name_for_decode, decoded_string)


if __name__ == '__main__':
    main()
