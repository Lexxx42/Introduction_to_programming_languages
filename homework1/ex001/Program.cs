// Задача 2: Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.
// поскольку примеры с целыми числами, то с ними будем и работать

int Prompt(string message)
{
    System.Console.Write(message);        // Вывод приглашения
    string strValue;                      // Объявление переменной для ввода строки
    strValue = Console.ReadLine() ?? "0"; // Вводим строку с консоли (с консоли можно ввести только строку), если ничего не ввели, то = 0 
    int value = int.Parse(strValue);      // Преобразование строки в целое число
    return value;
}
Console.Clear();
System.Console.WriteLine("This program compares two integer numbers and returns which is the largest and which is the smallest");
int number1 = Prompt("please enter 1st number > ");
int number2 = Prompt("please enter 2nd number > ");

if(number1 == number2)
{
    System.Console.WriteLine($"numbers are equal, max value = min value = {number1}");
}
else
{
    if(number1>number2)
    {
        System.Console.WriteLine($"number {number1} is a max value, number {number2} is a minimum value");
    }
    else
    {
        System.Console.WriteLine($"number {number2} is a max value, number {number1} is a minimum value");
    }
}