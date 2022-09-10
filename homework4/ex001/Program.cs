// Задача 1: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
// 3, 5 -> 243 (3⁵)
// 2, 4 -> 16


int Prompt(string message)
{
    System.Console.Write(message);
    return Convert.ToInt32(Console.ReadLine());
}

bool Validation(int numberForCheck)
{
    if (0 > numberForCheck || numberForCheck == 0) // B must be natural!
    {
        return false;
    }
    else
    {
        return true;
    }
}

double Pow(int A, int B)
{
    return Math.Pow(A, B);
}


System.Console.WriteLine("This program takes two numbers (A and B) as input and raises the number A to the natural power B");
System.Console.WriteLine();
int numberA = Prompt("Please, enter A number > ");
System.Console.WriteLine();
int numberB = Prompt("Please, enter B number > ");
System.Console.WriteLine();
if (Validation(numberB) == false)
{
    System.Console.WriteLine("Number B must be a natural number!");
}
else
{
    System.Console.WriteLine($"{numberA} ^ {numberB} = {Pow(numberA, numberB)}");
}
