# Привет, слушатель.

# В степах 3 и 7 данного урока есть ошибки и неточности формулировки.

# Для каждой области видимости у нас есть соответствующее ей пространство имен, 
# и мы ищем переменные в этих пространствах имен. Порядок областей видимости: local, non-local, global, built-in.

# Что было неправильно:  порядок поиска имени переменной не связан со стеком вызовов. 
# Порядок поиска имени переменной связан лишь с порядком вложенности друг в друга областей видимости.

# За полной информацией, лучше почитать документацию на https://docs.python.org/3.7/tutorial/classes.html#python-scopes-and-namespaces