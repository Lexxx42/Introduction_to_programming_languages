// Задача 3
// Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
// 3 -> 1, 8, 27
// 5 -> 1, 8, 27, 64, 125

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

bool Validation(int numberForCheck) // Check for number is natural or not.
{
    return numberForCheck > 0;
}

double[] MakeCubes(int length) // Produce cubes in a segment.
{
    double[] results = new double[length];
    for (int i = 0; i < results.Length; i++)
    {
        results[i] = Math.Pow((i + 1), 3);
    }
    return results;
}

void Print(double[] inputForPrint) // Prints array.
{
    for (int i = 0; i < inputForPrint.Length; i++)
    {
        System.Console.Write($"{inputForPrint[i]} ");
    }
}

void PrintCubes(int number) // Prints cubes in a segment or exception.
{
    if (Validation(number))
    {
        double[] results = MakeCubes(number);
        Print(results);
    }
    else
    {
        System.Console.WriteLine("Number has to be natural!");
    }
}


Console.Clear();
System.Console.WriteLine("This program takes a number (N - natural) as input and produces a table of cubes of numbers from 1 to N.");
int numberInput = Prompt("Please, enter the number > ");
PrintCubes(numberInput);
