// Задача 2: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
// 452 -> 11
// 82 -> 10
// 9012 -> 12

int Prompt(string message) // Input values.
{
    Console.Write(message);
    bool isDigit = int.TryParse(Console.ReadLine(), out int number);
    if (isDigit)
    {
        return number;
    }
    throw new Exception("You didn't enter a number");
}

int SumDigits(int number) // Finds the sum of digits.
{
    number = Math.Abs(number);
    if (0 <= number && number < 10)
    {
        return 1;
    }
    int sum = 0;
    while (number >= 10)
    {
        sum = sum + number % 10;
        number /= 10;
    }
    sum = sum + number;
    return sum;
}


Console.Clear();
System.Console.WriteLine("This program takes a number as input and returns the sum of the digits in the number");
System.Console.WriteLine();
int number = Prompt("Please, enter the number > ");
System.Console.WriteLine();
System.Console.WriteLine($"Sum of digits = {SumDigits(number)}");
