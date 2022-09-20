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

int[,] GenerateMatrix(int numberOfRows, int numberOfColumns) // Generates matrix.
{
    int[,] matrix = new int[numberOfRows, numberOfColumns];
    FillMatrix(matrix);
    return matrix;
}

List<double> SumAverageColumn(int[,] matrix) // Forming list with averages of columns.
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
        System.Console.WriteLine("Average for each column:");
        System.Console.WriteLine();
        var answer = SumAverageColumn(generatedMatrix);
        foreach (double item in answer)
        {
            System.Console.Write($"{item:f2}\t");
        }

    }
}


Console.Clear();
System.Console.WriteLine("This program generates random array filled with whole numbers, from MIN to MAX."
+ "Then finds the arithmetic mean of the elements in each column");
System.Console.WriteLine();
int numberOfRows = Prompt("Please enter the number of rows: ");
int numberOfColumns = Prompt("Please enter the number of columns: ");
System.Console.WriteLine();
ResultOfGeneration(numberOfRows, numberOfColumns);
