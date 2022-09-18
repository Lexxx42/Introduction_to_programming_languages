/* Задача 3. Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.

Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3. */

const int MIN = -20;
const int MAX = 20; // Max and Min for generation

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

void PrintArray(int[,] matrixForPrint) // Print matrix.
{
    for (int i = 0; i < matrixForPrint.GetLength(0); i++)
    {
        for (int j = 0; j < matrixForPrint.GetLength(1); j++)
        {
            System.Console.Write($"{matrixForPrint[i, j]}\t");
        }
        System.Console.WriteLine();
    }
}

void FillArray(int[,] matrixGenerated) // Matrix generation.
{
    for (int i = 0; i < matrixGenerated.GetLength(0); i++)
    {
        for (int j = 0; j < matrixGenerated.GetLength(1); j++)
        {
            matrixGenerated[i, j] = new Random().Next(MIN, MAX + 1);
        }
    }
}

bool Validation(int numberOfRows, int numberOfColumns) // Check input values.
{
    return (numberOfRows > 0 && numberOfColumns > 0);
}

void ResultOfGeneration(int numberOfRows, int numberOfColumns) // Print result of generation.
{
    if (!Validation(numberOfRows, numberOfColumns))
    {
        System.Console.WriteLine("Length can't be less or equal to zero!");
    }
    else
    {
        int[,] generatedMatrix = GenerateMatrix(numberOfRows, numberOfColumns);
        (int rowPosition, int columnPosition) = InputNumbersCoordinates();
        
    }
}

int[,] GenerateMatrix(int numberOfRows, int numberOfColumns) // Generates and prints matrix.
{
    int[,] matrix = new int[numberOfRows, numberOfColumns];
    FillArray(matrix);
    PrintArray(matrix);
    return matrix;
}


System.Console.WriteLine("This program generates random array filled with real numbers, from MIN to MAX");
System.Console.WriteLine();
int numberOfRows = Prompt("Please enter the number of rows: ");
int numberOfColumns = Prompt("Please enter the number of columns: ");
System.Console.WriteLine();
ResultOfGeneration(numberOfRows, numberOfColumns);

