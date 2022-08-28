//1. Напишите программу, которая на вход принимает два числа и проверяет, является ли первое число квадратом второго.
//a = 5; b = 25 -> да 
//a = 2 b = 10 -> нет 
//a = 9; b = -3 -> нет 
//a = -3 b = 9 -> да

// Ввод числа из консоли по приглашению
int Prompt(string message)
{
    System.Console.Write(message);        // Вывод приглашения
    string strValue;                      // Объявление переменной для ввода строки
    strValue = Console.ReadLine() ?? "0"; // Вводим строку с консоли (с консоли можно ввести только строку)
    int value = int.Parse(strValue);      // Преобразование строки в целое число
    return value;
}

int first_value = Prompt("Введите число > ");
int second_value = Prompt("Введите число > ");
int result = first_value * second_value;                 // Вычисление квадрата (заносим в переменную result)
System.Console.WriteLine($"Квадрат числа равен {result}");  // Вывод результата
if(result == value*value)
{
    System.Console.WriteLine($"квадрат {value} равен  {result}");
}
else
{
    System.Console.WriteLine($"квадрат не является");
}