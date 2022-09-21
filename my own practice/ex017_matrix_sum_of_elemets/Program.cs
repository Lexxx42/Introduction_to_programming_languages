// This program generates two cubic matrices and prints result of sum of their elements.
// 123  456 -> 5 7   9 
// 345  345 -> 3 8   10
// 567  123 -> 6 8   10

const int MIN = -20;
const int MAX = 20;


int Prompt(string message) // Input values.
{
    Console.Write(message);
    bool isDigit = int.TryParse(Console.ReadLine(), out int number);
    if (isDigit)
    {
        return number;
    }
    throw new Exception("You didn't entered the number!");
}

int[,] MatrixGeneration(int length)
{
    int[,] matrix = new int[length, length];
    return matrix;
}

int[,] MatrixFill(int[,] matrix)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            matrix[i, j] = new Random().Next(MIN, MAX + 1);
        }
    }
    return matrix;
}

void PrintMatrix(int[,] matrix)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            System.Console.Write($"{matrix[i, j]}\t");
        }
        System.Console.WriteLine();
    }
}

int[,] SumElements(int[,] matrix1, int[,] matrix2)
{
    int[,] matrixSum = MatrixGeneration(matrix1.GetLength(0));
    for (int i = 0; i < matrixSum.GetLength(0); i++)
    {
        for (int j = 0; j < matrixSum.GetLength(1); j++)
        {
            matrixSum[i, j] = matrix1[i, j] + matrix2[i, j];
        }
    }
    return matrixSum;
}




void SumResult(int length)
{
    if (length < 0)
    {
        System.Console.WriteLine("Length can't be negative!");
    }
    else if (length == 0)
    {
        System.Console.WriteLine("Length is null!");
    }
    else
    {
        System.Console.WriteLine("Generating matrix");
        System.Console.WriteLine();
        int[,] firstMatrix = MatrixFill(MatrixGeneration(length));
        int[,] secondMatrix = MatrixFill(MatrixGeneration(length));
        PrintMatrix(firstMatrix);
        System.Console.WriteLine();
        PrintMatrix(secondMatrix);
        System.Console.WriteLine();
        int[,] sumMatrix = SumElements(firstMatrix, secondMatrix);
        PrintMatrix(sumMatrix);

    }
}

Console.Clear();
System.Console.WriteLine("This program generates two cubic matrices and prints result of sum of their elements.");
int matrixLength = Prompt("Please enter cubic matrix length for both matrices > ");
SumResult(matrixLength);
