/* Задача 3. Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.

Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3. */

const int MIN = 0;
const int MAX = 3; // Max and Min for generation

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
        System.Console.WriteLine("Average for each column:");
        System.Console.WriteLine();
        var answer = SumAverageColumn(generatedMatrix);
        PrintList(answer);
    }
}

void PrintList(List<double> list) // Print elements from list.
{
    foreach (double item in list)
    {
        System.Console.Write($"{item}\t");
    }
}

int[,] GenerateMatrix(int numberOfRows, int numberOfColumns) // Generates and prints matrix.
{
    int[,] matrix = new int[numberOfRows, numberOfColumns];
    FillArray(matrix);
    PrintArray(matrix);
    return matrix;
}

List<double> SumAverageColumn(int[,] matrix) // List with averages.
{
    var answer = new List<double>();
    for (int i = 0; i < matrix.GetLength(1); i++)
    {
        double sumColumn = 0;
        for (int j = 0; j < matrix.GetLength(0); j++)
        {
            sumColumn += matrix[j, i];
        }
        double avrCol = sumColumn / matrix.GetLength(1);
        answer.Add(avrCol);
    }
    return answer;
}




System.Console.WriteLine("This program generates random array filled with whole numbers, from MIN to MAX."
+ "Then finds the arithmetic mean of the elements in each column");
System.Console.WriteLine();
int numberOfRows = Prompt("Please enter the number of rows: ");
int numberOfColumns = Prompt("Please enter the number of columns: ");
System.Console.WriteLine();
ResultOfGeneration(numberOfRows, numberOfColumns);


