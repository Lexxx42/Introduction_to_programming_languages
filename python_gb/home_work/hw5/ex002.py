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


def coding(str_1: str or int, str_new_list: list) -> list[str]:
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


def decoding(string_decoding) -> str:
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
    print(list_decoded_repaired)
    print()





# string_for_coding = 'aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa'
string_for_decoding = '5a29v4s3D3d2F4g2O3i2a'
decoding(string_for_decoding)
# string_new_list = []
# coding(string_for_coding, string_new_list)
# print(''.join(string_new_list))
