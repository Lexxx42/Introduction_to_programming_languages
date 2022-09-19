// Задача 2: Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.
// Поскольку примеры с целыми числами, то с ними будем и работать.

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

void Compare(int firstNumber, int secondNumber) // Compare values.
{
    if (firstNumber == secondNumber)
    {
        System.Console.WriteLine($"Numbers are equal, max value = min value = {firstNumber}");
    }
    else
    {
        if (firstNumber > secondNumber)
        {
            System.Console.WriteLine($"Number {firstNumber} is a max value, number {secondNumber} is a minimum value");
        }
        else
        {
            System.Console.WriteLine($"Number {firstNumber} is a max value, number {secondNumber} is a minimum value");
        }
    }
}


Console.Clear();
System.Console.WriteLine("This program compares two integer numbers and returns which is the largest and which is the smallest");
int number1 = Prompt("Please enter 1st number > ");
int number2 = Prompt("Please enter 2nd number > ");
Compare(number1, number2);
