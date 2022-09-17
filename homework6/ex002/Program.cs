/* Задача 2: Напишите программу, которая найдёт точку пересечения двух прямых, 

заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.

b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; -0,5) */

int Prompt(string message)
{
    Console.Write(message);
    bool isDigit = int.TryParse(Console.ReadLine(), out int number);
    if (isDigit)
    {
        return number;
    }
    throw new Exception("You didn't enter a number");
}


(double, double) CrossCoordinates(int b1, int k1, int b2, int k2)
{
    double x = (double)(b1 - b2) / (k2 - k1);
    double y = (double)(k2 * b1 - k1 * b2) / (k2 - k1);
    return (x, y);
}


void Result(int b1, int k1, int b2, int k2)
{
    if (Check(b1, k1, b2, k2) == false)
    {
        System.Console.WriteLine("Parallel lines!");
    }
    else
    {
        (double, double) answer = CrossCoordinates(b1, k1, b2, k2);
        System.Console.WriteLine($"Intersection point is (x, y) = {answer}");
    }
}


bool Check(int b1, int k1, int b2, int k2)
{
    if (k1 == k2)
    {
        return false;

    }
    return true;
}


System.Console.WriteLine("This program finds the point of intersection of two"
+ " lines given by the equations y = k1 * x + b1, y = k2 * x + b2; b1, k1, b2 and k2 values are user defined");
System.Console.WriteLine();
int b1 = Prompt("Please enter b1 value: ");
int k1 = Prompt("Please enter k1 value: ");
int b2 = Prompt("Please enter b2 value: ");
int k2 = Prompt("Please enter k2 value: ");
System.Console.WriteLine();
Result(b1, k1, b2, k2);