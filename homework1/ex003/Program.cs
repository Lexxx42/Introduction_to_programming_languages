// Задача 6: Напишите программу, которая на вход принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка).
// примеры к задаче с целыми числами, следовательно с ними и будем работать

int Prompt(string message)
{
    System.Console.Write(message);        // Вывод приглашения
    string strValue;                      // Объявление переменной для ввода строки
    strValue = Console.ReadLine() ?? "0"; // Вводим строку с консоли (с консоли можно ввести только строку), если ничего не ввели, то = 0 
    int value = int.Parse(strValue);      // Преобразование строки в целое число
    return value;
}
Console.Clear();
System.Console.WriteLine("This program takes a number and returns whether the number is even or not");

int number = Prompt("please enter a number > ");
if(number%2 == 0)
{
    System.Console.WriteLine($"number {number} is even");
}
else
{
    System.Console.WriteLine($"number {number} is not even");
}