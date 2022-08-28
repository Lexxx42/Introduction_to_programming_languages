// Напишите программу, которая на вход принимает число и выдаёт его квадрат 
// (число умноженное на само себя).

// Ввод числа из консоли по приглашению
int Prompt(string message)
{
    System.Console.Write(message);        // Вывод приглашения
    string strValue;                      // Объявление переменной для ввода строки
    strValue = Console.ReadLine() ?? "0"; // Вводим строку с консоли (с консоли можно ввести только строку)
    int value = int.Parse(strValue);      // Преобразование строки в целое число
    return value;
}

int value = Prompt("Введите число > ");
int result = value * value;                 // Вычисление квадрата (заносим в переменную result)
System.Console.WriteLine($"Квадрат числа {value} равен {result}");  // Вывод результата
