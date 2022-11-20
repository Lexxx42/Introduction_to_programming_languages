// Задача 6: Напишите программу, которая на вход принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка).
// Примеры к задаче с целыми числами, следовательно с ними и будем работать.

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

void CheckForEven(int numberForCheck) // Checking the number for even.
{
    if (numberForCheck % 2 == 0)
    {
        System.Console.WriteLine($"number {numberForCheck} is even");
    }
    else
    {
        System.Console.WriteLine($"number {numberForCheck} is not even");
    }
}


Console.Clear();
System.Console.WriteLine("This program takes a number and returns whether the number is even or not");
int number = Prompt("Please enter a number > ");
CheckForEven(number);
