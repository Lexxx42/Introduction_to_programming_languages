// Задача 2. Напишите программу, которая на вход принимает позиции элемента в двумерном массиве,
// и возвращает значение этого элемента или же указание, что такого элемента нет.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// 1, 7 -> такого числа в массиве нет

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

void PrintMatrix(int[,] matrixForPrint) // Print matrix.
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

void FillMatrix(int[,] matrixGenerated) // Fills matrix with random numbers.
{
    for (int i = 0; i < matrixGenerated.GetLength(0); i++)
    {
        for (int j = 0; j < matrixGenerated.GetLength(1); j++)
        {
            matrixGenerated[i, j] = new Random().Next(MIN, MAX + 1);
        }
    }
}

int[,] GenerateMatrix(int numberOfRows, int numberOfColumns) // Generates matrix.
{
    int[,] matrix = new int[numberOfRows, numberOfColumns];
    FillMatrix(matrix);
    return matrix;
}

(int, int) InputNumbersCoordinates() // User search input.
{
    int rowPosition = Prompt("Please enter number's row position: ");
    int columnPosition = Prompt("Please enter number's column position: ");
    return (rowPosition, columnPosition);
}

int SearchNumbersValue(int[,] matrix, int rowPosition, int columnPosition) // Search for value in position.
{
    return matrix[rowPosition - 1, columnPosition - 1];
}

void ResultOfGeneration(int numberOfRows, int numberOfColumns) // Print result of generation.
{
    if (!(numberOfRows > 0 && numberOfColumns > 0))
    {
        System.Console.WriteLine("Length can't be less or equal to zero!");
    }
    else
    {
        int[,] generatedMatrix = GenerateMatrix(numberOfRows, numberOfColumns);
        PrintMatrix(generatedMatrix);
        (int rowPosition, int columnPosition) = InputNumbersCoordinates();
        if (generatedMatrix.GetLength(0) < rowPosition || generatedMatrix.GetLength(1) < columnPosition || rowPosition < 1 || columnPosition < 1)
        {
            System.Console.WriteLine("There is no such element within the matrix!");
        }
        else
        {
            int foundValue = SearchNumbersValue(generatedMatrix, rowPosition, columnPosition);
            System.Console.WriteLine($"Found value = {foundValue}");
        }
    }
}

Console.Clear();
System.Console.WriteLine("This program generates random array filled with whole numbers, from MIN to MAX."
+ " User inputs row position and column position for search withing the matrix. Program returns the value from matrix");
System.Console.WriteLine();
int numberOfRows = Prompt("Please enter the number of rows: ");
int numberOfColumns = Prompt("Please enter the number of columns: ");
System.Console.WriteLine();
ResultOfGeneration(numberOfRows, numberOfColumns);
