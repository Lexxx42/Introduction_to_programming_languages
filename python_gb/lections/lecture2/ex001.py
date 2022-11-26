colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors)  # разделителей не будет
data.close()

