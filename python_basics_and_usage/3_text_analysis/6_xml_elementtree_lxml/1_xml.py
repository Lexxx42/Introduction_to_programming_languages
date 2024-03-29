# Темой данного урока является еще один популярный текстовый формат XML.

# XML - extensible markup language, расширяемый язык разметки.
# Также как HTML он является теговым языком разметки, однако в XML мы придерживаемся
# более строгих правил, но основное отличие от HTML, что мы сами определяем теги.

# Если HTML использую для того, чтобы данные отображать чаще всего в браузере,
# то XML используется для того, чтобы данные хранить.

# Что же такое элементы в XML?

# Элементы объявляются с помощью тегов.

# <tag> </tag> - элемент XML
# Либо с помощью одного тега <tag/>

# Также мы храним внутри элемента атрибуты.
# Атрибуты - это пара ключ=значение, которые разделены равно.
# Значение хранится в кавычках.
# Мы объявляем атрибуты в открывающем нас теге.

# <tag id="1">text</tag>

# Важно понимать, что в XML формате мы сами придумываем себе формат, теги, имена для атрибутов.
# Поэтому если другие люди будут пользоваться нашим XML форматом, нашими данными, которые хранятся
# в XML формате, важно чтобы мы придумывали понятные имена для наших тегов и атрибутов.
# Проще всего использовать понятные слова, которые бы хорошо объясняли сущность тех данных,
# которые вы храните.

# Из-за того, что данные в XML могут содержать в себе другие элементы или текст,
# то нам проще всего изображать данные в XML формате с помощью деревьев.

# Корень нашего дерева будет studentList.
# Такое отображение данных в виде дерева в XML продиктовано самим форматом.
# Более того, формат XML требует от нас наличие выделенного корня.
# Такого элемента, который содержал бы в себе все остальные элементы.

# Поэтому все программы и библиотеки, которые занимаются разбором данных в формате XML
# так или иначе хранят его именно в виде дерева.
