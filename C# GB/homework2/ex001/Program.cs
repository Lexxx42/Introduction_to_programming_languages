// Задача 1: Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.

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

bool Validation(int numberForCheck) // Check if number is 3-digit.
{
    return Math.Abs(numberForCheck) > 99 & Math.Abs(numberForCheck) < 1000;
}

int SearchForSecondNumber(int number) // Finds a second digit in number.
{
    number = Math.Abs(number);
    int secondDigit = 0;
    number = number / 10;
    secondDigit = number % 10;
    return secondDigit;
}

void PrintResult(int threeDigitNumber) // Prints second digit or exception.
{
    if (Validation(threeDigitNumber))
    {
        System.Console.WriteLine($"2nd digit is {SearchForSecondNumber(threeDigitNumber)}");
    }
    else
    {
        System.Console.WriteLine("Your number have to be a three-digit number!");
    }
}


Console.Clear();
System.Console.WriteLine("This program takes a three-digit number as input and outputs the second digit of that number.");
int inputNumber = Prompt("Please, enter some three-digit number > ");
PrintResult(inputNumber);
