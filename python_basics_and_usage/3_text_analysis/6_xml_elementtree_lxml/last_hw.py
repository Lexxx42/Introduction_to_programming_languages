# Вам дано описание пирамиды из кубиков в формате XML.
# Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
# Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

# Пример:

# <cube color="blue">
#   <cube color="red">
#     <cube color="green">
#     </cube>
#   </cube>
#   <cube color="red">
#   </cube>
# </cube>

# Введем понятие ценности для кубиков.
# Самый верхний кубик, соответствующий корню XML документа имеет ценность 1.
# Кубики, расположенные прямо под ним, имеют ценность 2.
# Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.

# Ценность цвета равна сумме ценностей всех кубиков этого цвета.

# Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
# Sample Input:

# <cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
# Sample Output:

# 4 3 1

import xml.etree.ElementTree as ET


def value_count(current_root, current_count_value):
    if current_root:
        for child in current_root:
            value[child.attrib.get("color")] += current_count_value
            value_count(child, current_count_value + 1)
    else:
        return


root = ET.fromstring(input())

value = {"red": 0, "green": 0, "blue": 0}
count_value = 1

value[root.attrib.get("color")] += count_value
count_value += 1

value_count(root, count_value)
print(" ".join(map(str, value.values())))
