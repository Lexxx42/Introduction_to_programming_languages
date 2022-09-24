/* Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.

Например, задан массив:

1 4 7 2

5 9 2 3

8 4 2 4

5 2 6 7

Программа считает сумму элементов в каждой строке и выдаёт номер строки с наименьшей суммой элементов: 1 строка */

int[,] GenerateMatrix(int rowLength, int columnLength, int minRange, int maxRange) // Matrix generation.
{
    var matrix = new int[rowLength, columnLength];
    var random = new Random();
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            matrix[i, j] = random.Next(minRange, maxRange + 1);

        }
    }
    return matrix;
}

void PrintMatrix(int[,] matrix) // Matrix print.
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            System.Console.Write($"{matrix[i, j]}\t");
        }
        System.Console.WriteLine();
    }
    System.Console.WriteLine();
}

int[] SumOfRow(int[,] matrix) // Finds sum of rows in matrix.
{
    int[] sumArray = new int[matrix.GetLength(0)];
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        sumArray[i] = 0;
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            sumArray[i] += matrix[i, j];
        }
    }
    return sumArray;
}

int FindMinIndexArray(int[] array) // Finds first index of minimum sum of elements in row.
{
    int min = array[0];
    int index = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] < min)
        {
            min = array[i];
            index = i;
        }
    }
    return index;
}

void FirstPositionOfMinSum(int matrixRows, int matrixColumns, int minValueGenerated, int maxValueGenerated)
{
    if (matrixRows <= 0 || matrixColumns <= 0)
    {
        System.Console.WriteLine("Number of columns and rows must be greater than zero!");
    }
    else
    {
        int[,] generatedMatrix = GenerateMatrix(matrixRows, matrixColumns, minValueGenerated, maxValueGenerated);
        PrintMatrix(generatedMatrix);
        int[] sumOfRows = SumOfRow(generatedMatrix);
        System.Console.WriteLine($"The position of first row with minimum sum of elements is {FindMinIndexArray(sumOfRows) + 1}");
    }
}


Console.Clear();
System.Console.WriteLine("This program generates a matrix. Prints the row of matrix with lowest sum of elements.");
System.Console.WriteLine();

int matrixRows = 6;
int matrixColumns = 3;
int minValueGenerated = 0;
int maxValueGenerated = 3;

FirstPositionOfMinSum(matrixRows, matrixColumns, minValueGenerated, maxValueGenerated);
