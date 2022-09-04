// Задача 3
// Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
// 3 -> 1, 8, 27
// 5 -> 1, 8, 27, 64, 125

System.Console.WriteLine("This program takes a number (N - natural) as input and produces a table of cubes of numbers from 1 to N.");

int Prompt(string message)
{
    System.Console.Write(message);
    return Convert.ToInt32(Console.ReadLine());
}

bool Validation(int numberForCheck)
{
    if (numberForCheck > 0)
    {
        return true;
    }
    else
    {
        System.Console.WriteLine("Number has to be natural!");
        return false;
    }
}

int[] MakeCubes(int inputNumber)
{
    int[] results = new int[inputNumber];
    for (int i = 0; i < results.Length; i++)
    {
        results[i] = (i+1)*(i+1)*(i+1); // why MathPow((i+1),3) not working?
    }
    return results;
}

void Print(int[] inputForPrint)
{
    for (int i = 0; i < inputForPrint.Length; i++)
    {
        System.Console.Write($"{inputForPrint[i]} ");
    }
}

int numberInput = Prompt("Please, enter the number > ");
if (Validation(numberInput))
{
    int[] results = MakeCubes(numberInput);
    Print(results);
}
