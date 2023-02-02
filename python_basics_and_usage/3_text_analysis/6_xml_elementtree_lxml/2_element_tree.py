from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")
root = tree.getroot()
# use root = ElementTree.fromstring(string_xml_data)  # to parse from str

print(root)
print(root.tag, root.attrib)

for child in root:
    print(child.tag, child.attrib)

print(root[0][0].text)

# Все элементы нашего дерева будут иметь один класс Element, поэтому наш корень класса
# Element.
# Все объекты которые мы перебираем используя цикл for по корню будут класса Element.
# Все дети детей нашего корня также будут иметь класс Element.

# Поэтому все имена методов и атрибутов у данных объектов будут одинаковые.

for element in root.iter("scores"):
    score_sum = 0
    for child in element:
        score_sum += float(child.text)
    print(score_sum)

# Как создавать новые деревья и записывать их в XML формат?
print("+++")

tree = ElementTree.parse("example.xml")
root = tree.getroot()

tree.write("example_copy.xml", encoding="UTF-8")

greg = root[0]
module1 = next(greg.iter("module1"))
print(module1, module1.text)

# Изменение содержимого
module1.text = str(float(module1.text) + 30)

# Добавление атрибута
certificate = greg[2]
certificate.set("type", "with distinction")

# Добавление элемента
# description = ElementTree.Element("description")
# description.text = "Showed excellent skills during the course"
# greg.append(description)

tree = ElementTree.parse("example_modified.xml")
root = tree.getroot()
greg = root[0]

# Удаление элемента
# description = greg.find("description")
# greg.remove(description)

tree.write("example_modified.xml", encoding="UTF-8")

# Создание дерева
root = ElementTree.Element("student")

first_name = ElementTree.SubElement(root, "firstName")
first_name.text = "Greg"

second_name = ElementTree.SubElement(root, "secondName")
second_name.text = "Dean"

scores = ElementTree.SubElement(root, "scores")

module1 = ElementTree.SubElement(scores, "module1")
module1.text = "100"

module2 = ElementTree.SubElement(scores, "module2")
module2.text = "100"

module3 = ElementTree.SubElement(scores, "module2")
module3.text = "100"

tree = ElementTree.ElementTree(root)
tree.write("students.xml", encoding="UTF-8")
