with open('stepic2.txt') as inf:  # закрывается самостоятельно
    text = inf.readline()
    text = text.strip()
    if "We" in text:
        print(text)
        for line in inf:
            line = line.strip()
            print(line)
