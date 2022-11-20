colors = ['red', 'green', 'blue']

for e in colors:  # red green blue
    print(e)

for e in colors:  #redred greengreen blueblue
    print(e*2)

colors.append('gray')  # add gray in the end
print(colors == ['red', 'green', 'blue', 'gray'])  #True
colors.remove('red') # remove element, del colors[0]