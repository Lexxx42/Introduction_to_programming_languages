// 1. Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает последнюю цифру этого числа.
// 456 -> 6
// 782 -> 2
// 918 -> 8

int chislo(int X)
{
    
    int p = 0;
    p = X%10;
    return p;
    if(p < 0)
    {
        p = -p;
    }
}

int Prompt(string message)
{
    System.Console.Write(message);        // Вывод приглашения
    string strValue;                      // Объявление переменной для ввода строки
    strValue = Console.ReadLine() ?? "0"; // Вводим строку с консоли (с консоли можно ввести только строку)
    int value = int.Parse(strValue);      // Преобразование строки в целое число
    return value;
}

int value = Prompt("Введите число from 100 to 999 > ");
if(value=>0)
{
if(value>99 & value<1000)
{
System.Console.WriteLine($"last number is {chislo(value)}");
}
else
{
    System.Console.WriteLine("number is not correct!");
}
}
else
{
    if(value>99 & value<1000)
{
System.Console.WriteLine($"last number is {chislo(value)}");
}
    else
{
    System.Console.WriteLine("number is not correct!");
}
}
//error!