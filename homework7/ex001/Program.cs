/* Задача 1. Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
m = 3, n = 4.
0,5 7 -2 -0,2
1 -3,3 8 -9,9
8 7,8 -7,1 9 */

const double MIN = -20;
const double MAX = 20; // Max and Min for generation

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

void PrintArray(double[,] matrixForPrint) // Print matrix.
{
    for (int i = 0; i < matrixForPrint.GetLength(0); i++)
    {
        for (int j = 0; j < matrixForPrint.GetLength(1); j++)
        {
            System.Console.Write($"{matrixForPrint[i, j]:f2}\t");
        }
        System.Console.WriteLine();
    }
}

void FillArray(double[,] matrixGenerated) // Matrix generation.
{
    for (int i = 0; i < matrixGenerated.GetLength(0); i++)
    {
        for (int j = 0; j < matrixGenerated.GetLength(1); j++)
        {
            matrixGenerated[i, j] = MIN + new Random().NextDouble() * (MAX - MIN); ;
        }
    }
}

bool Validation(int numberOfRows, int numberOfColumns) // Check input values.
{
    return (numberOfRows > 0 && numberOfColumns > 0);
}

void Result(int numberOfRows, int numberOfColumns) // Print result.
{
    if (!Validation(numberOfRows, numberOfColumns))
    {
        System.Console.WriteLine("Length can't be less or equal to zero!");
    }
    else
    {
        double[,] matrix = new double[numberOfRows, numberOfColumns];
        FillArray(matrix);
        PrintArray(matrix);
    }
}



System.Console.WriteLine("This program generates random array filled with real numbers, from MIN to MAX");
System.Console.WriteLine();
int numberOfRows = Prompt("Please enter the number of rows: ");
int numberOfColumns = Prompt("Please enter the number of columns: ");
System.Console.WriteLine();
Result(numberOfRows, numberOfColumns);
