# Задача 1
# Идея: совместная разработка
# Система собирает информацию с датчиков, в ней есть модуль логирования,
# который заносит в журнал все обращения к датчикам.
# В системе есть модуль, выполняющий обращения для получения данных
# с датчиков и модуль генерации html-представления.
# Запуск системы осуществляется из головного модуля.

# Модуль 1: сбор информации с датчиков
# Модуль 2: логирование
# Модуль 3: UI
# Модуль 4: HTML-генератор
# Модуль 5: главный модуль

# Модуль 1: data_provider
# Модуль 2: logger
# Модуль 3: user_interface
# Модуль 4: html_creator
# Модуль 5: main

# В рамках этих модулей напишем некоторый набор методов

# data_provider: get_temperature, get_pressure, get_wind_speed
# logger: temperature_logger, pressure_logger, wind_speed_logger
# user_interface: temperature_view, pressure_view, wind_speed_view
# html_creator: create
# main: запуск системы
