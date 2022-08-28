// Задача 2: Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.

int Prompt(string message)
{
    System.Console.Write(message);        // Вывод приглашения
    string strValue;                      // Объявление переменной для ввода строки
    strValue = Console.ReadLine() ?? "0"; // Вводим строку с консоли (с консоли можно ввести только строку), если ничего не ввели, то = 0
    int value = int.Parse(strValue);      // Преобразование строки в целое число
    return number1;
}

int value = Prompt("Введите число > ");
