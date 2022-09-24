/* Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
Например, даны 2 матрицы:
2 4 | 3 4
3 2 | 3 3
Результирующая матрица будет:
18 20
15 18 */

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

int[,] MatrixMultiplication(int[,] firstMatrix, int[,] secondMatrix) // Multiplies first matrix with second one.
{
    int[,] matrix = new int[firstMatrix.GetLength(0), secondMatrix.GetLength(1)];
    for (int i = 0; i < firstMatrix.GetLength(0); i++)
    {
        for (int j = 0; j < secondMatrix.GetLength(1); j++)
        {
            for (int k = 0; k < firstMatrix.GetLength(1); k++)
            {
                matrix[i, j] += firstMatrix[i, k] * secondMatrix[k, j];
            }
        }
    }
    return matrix;
}

// Prints the result of multiplication of matrices.
void PrintMultiplication(int firstMatrixRows, int firstMatrixColumns, int secondMatrixRows, int secondMatrixColumns, int minValueGenerated, int maxValueGenerated)
{
    if ((firstMatrixRows > 0 || firstMatrixColumns > 0) && (secondMatrixRows > 0 || secondMatrixColumns > 0) && firstMatrixColumns == secondMatrixRows)
    {
        int[,] firstMatrix = GenerateMatrix(firstMatrixRows, firstMatrixColumns, minValueGenerated, maxValueGenerated);
        System.Console.WriteLine("First matrix:");
        PrintMatrix(firstMatrix);
        int[,] secondMatrix = GenerateMatrix(secondMatrixRows, secondMatrixColumns, minValueGenerated, maxValueGenerated);
        System.Console.WriteLine("Second matrix:");
        PrintMatrix(secondMatrix);
        int[,] multiplication = MatrixMultiplication(firstMatrix, secondMatrix);
        System.Console.WriteLine("First matrix x Second matrix:");
        PrintMatrix(multiplication);

    }
    else if ((firstMatrixRows <= 0 || firstMatrixColumns <= 0) && (secondMatrixRows <= 0 || secondMatrixColumns <= 0))
    {
        System.Console.WriteLine("Number of columns and rows must be greater than zero!");
    }
    else
    {
        System.Console.WriteLine("Number of first matrix columns have to be equal to second's matrix number of rows.");
    }
}


Console.Clear();
System.Console.WriteLine("This program generates a matrix. Prints the row of matrix with lowest sum of elements.");
System.Console.WriteLine();

int firstMatrixRows = 3;
int firstMatrixColumns = 2;

int secondMatrixRows = 2;
int secondMatrixColumns = 2;

int minValueGenerated = 0;
int maxValueGenerated = 3;

PrintMultiplication(firstMatrixRows, firstMatrixColumns, secondMatrixRows, secondMatrixColumns, minValueGenerated, maxValueGenerated);
