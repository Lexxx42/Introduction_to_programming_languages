// Задача 2: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
// 452 -> 11
// 82 -> 10
// 9012 -> 12

int Prompt(string message)
{
    System.Console.Write(message);
    return Convert.ToInt32(Console.ReadLine());
}

int SummDigits(int number)
{
    number = Math.Abs(number); // negative numbers have positive digits after all!
    if (0 <= number && number < 10) { return 1; }
    int sum = 0;
    while (number >= 10)
    {
        sum = sum + number % 10;
        number /= 10;
    }
    sum = sum + number;
    return sum;
}


System.Console.WriteLine("This program takes a number as input and returns the sum of the digits in the number");
System.Console.WriteLine();
int number = Prompt("Please, enter the number > ");
System.Console.WriteLine();
System.Console.WriteLine($"Summ of digits = {SummDigits(number)}");
