// Задача 1: Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.

int SearchForSecondNumber(int X)
{
    int p = 0;
    X = X/10;
    if(X > 0)
    {
        p = X%10;
    }
    else
    {
        p = -X%10;
    }
    return p;
}

int Prompt(string message)
{
    System.Console.Write(message);        // Вывод приглашения
    string strValue;                      // Объявление переменной для ввода строки
    strValue = Console.ReadLine() ?? "0"; // Вводим строку с консоли (с консоли можно ввести только строку)
    int value = int.Parse(strValue);      // Преобразование строки в целое число
    return value;
}

System.Console.WriteLine("This program takes a three-digit number as input and outputs the second digit of that number.");
int value = Prompt("Please, enter some three-digit number > ");


if((Math.Abs(value)>99 & Math.Abs(value)<1000))
{
System.Console.WriteLine($"2nd digit is {SearchForSecondNumber(value)}");
}
else
{
    System.Console.WriteLine("Your number have to be a three-digit number!");
}