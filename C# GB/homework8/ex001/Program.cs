/* Задача 54: Задайте двумерный массив. Напишите программу, 
которая упорядочит по убыванию элементы каждой строки двумерного массива.

Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
В итоге получается вот такой массив:
7 4 2 1
9 5 3 2
8 4 4 2 */

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

int[,] SortRowsDescending(int[,] matrix) // Sort rows in matrix in ascending order.
{
    int max = 0;
    int temp = 0;
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            max = matrix[i, j];
            for (int k = j + 1; k < matrix.GetLength(1); k++)
            {
                if (matrix[i, k] > max)
                {
                    temp = matrix[i, k];
                    matrix[i, k] = max;
                    matrix[i, j] = temp;
                    max = temp;
                }
            }
        }
    }
    return matrix;
}

void MainSequence(int matrixRows, int matrixColumns, int minValueGenerated, int maxValueGenerated) // Calls all other methods and prints results.
{
    if (matrixRows <= 0 || matrixColumns <= 0)
    {
        System.Console.WriteLine("Number of columns and rows must be greater than zero!");
    }
    else
    {
        int[,] generatedMatrix = GenerateMatrix(matrixRows, matrixColumns, minValueGenerated, maxValueGenerated);
        System.Console.WriteLine("Generated matrix:");
        PrintMatrix(generatedMatrix);
        System.Console.WriteLine("Sorted matrix:");
        PrintMatrix(SortRowsDescending(generatedMatrix));
    }
}


Console.Clear();
System.Console.WriteLine("This program generates a matrix. Sorts rows in matrix in ascending order.");
System.Console.WriteLine();

int matrixRows = 6;
int matrixColumns = 3;
int minValueGenerated = -5;
int maxValueGenerated = 5;

MainSequence(matrixRows, matrixColumns, minValueGenerated, maxValueGenerated);
