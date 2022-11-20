// Задача 1: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
// 3, 5 -> 243 (3⁵)
// 2, 4 -> 16

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

bool Validation(int powerForCheck) // Check for natural power.
{
    return 0 > powerForCheck || powerForCheck == 0;
}

double Pow(int number, int power) // Returns firstNumber ^ secondNumber.
{
    return Math.Pow(number, power);
}

void PrintPower() // Inputs numbers and prints results of power.
{
    while (true)
    {
        int number = Prompt("Please, enter A number > ");
        System.Console.WriteLine();
        int power = Prompt("Please, enter B number > ");
        System.Console.WriteLine();
        if (Validation(power))
        {
            System.Console.WriteLine("Number B must be a natural number!");
        }
        else
        {
            System.Console.WriteLine($"{number} ^ {power} = {Pow(number, power)}");
        }
    }
}


Console.Clear();
System.Console.WriteLine("This program takes two numbers (A and B) as input and raises the number A to the natural power B");
System.Console.WriteLine();
PrintPower();
