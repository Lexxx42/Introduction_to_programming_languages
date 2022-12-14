# Пространство имен или namespace-ы
# Пространство имен - это сопоставление наших имен переменных, функций или классов и реальных объектов в оперативной памяти

# Чаще всего, когда мы сталкиваемся с пространством имен, когда мы объявляем переменные и затем пытаемся их использовать.

# Пускай есть список а
a = [2, 3, 1]

# Как мы знаем, когда мы используем оператор присваивания где-то в оперативной памяти появляется объект для списка
# и а ссылается на объект списка

# пускай мы объявили
b = 14

# в оперативной памяти появился бы объект 14 и б ссылается на этот объект

# Мы знаем, что а ссылается на список и б ссылается на 14.
# Именно это множество ссылок от всех имен до объектов мы будем называть пространством имен.

# Т.е. есть 2 имени а и б, есть 2 ссылки - это множество ссылок и будет пространством имен

# Тогда, если мы заходим создать переменную, мы должны будем добавить ее в пространство имен.

# Если объявим переменную с
c = 'abc'

# Мы бы конечно же создали объект в оперативной памяти и с начало бы ссылаться на этот объект.
# эта ссылка бы добавился в пространство имен.

# Но чаще мы используем пространство имен, не когда переменные объявляем, а когда переменные переиспользуем.

# создали бы мы переменную d
d = sorted(a)

# Когда интерпретатор дошел бы до этой строки он сначала исполнил бы правую часть оператора присваивания, чтобы узнать, что нужно присвоить
# И тогда первый вопрос, который задал бы себе интерпретатор: "а что же такое сортед()" и тогда в каком-то из неймспейсов он бы нашел имя
# сортед() и узнал бы, что это функция, которая принимает 1 аргумент. А затем он спросил бы себя: "а что же такое объект а, на что ссылается а, 
# если его нужно передать в качестве аргумента?" 

# В этом есть рутинная работа пространства имен. В процессе работы мы создаем имена и связываем с ними какие-то объекты.
# однако в любой момент времени можно спросить у пространства имен: а связан ли с каким-то конкретным именем какой-нибудь объект
