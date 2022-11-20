/* Найдите максимальное значение в матрице по каждой строке, получите сумму этих максимумов. 
Затем найдите минимальное значение по каждой колонке,получите сумму этих минимумов. 
Затем из первой суммы (с максимумами) вычтите вторую сумму(с минимумами)
1 2 3
3 4 5
3+5=8, 1+2+3=6, 8-6=2 */

const int MIN = 0;
const int MAX = 10;

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

void PrintArray(int[,] matrix) // Prints matrix.
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            System.Console.Write($"{matrix[i, j]} ");
        }
        System.Console.WriteLine();
    }
}

void FillArray(int[,] matrix) // Fills the matrix with random values.
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            matrix[i, j] = new Random().Next(MIN, MAX);
        }
    }
}

int SumMaxRow(int[,] matrix) // Finds sum of row's maximums.
{
    int sumMaxRow = 0;
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        int maxRow = matrix[i, 0];
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            if (matrix[i, j] > maxRow)
            {
                maxRow = matrix[i, j];
            }
        }
        sumMaxRow += maxRow;
    }
    return sumMaxRow;
}

int SumMinColumn(int[,] matrix) // Finds sum of column minimums.
{
    int sumMinColumn = 0;
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        int minColumn = matrix[0, i];
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            if (matrix[j, i] < minColumn)
            {
                minColumn = matrix[j, i];
            }
        }
        sumMinColumn += minColumn;
    }
    return sumMinColumn;
}

int MaxMinusMin(int max, int min) // Finds the difference between max and min.
{
    return max - min;
}

bool Validation(int length) // Check the length of cubic matrix.
{
    return length <= 0;
}

void DiffSumMaxRowSumMinColumn(int length, int[,] matrix) // Finds the difference between sum maximums of rows and sum minimums of columns.
{
    if (Validation(length))
    {
        System.Console.WriteLine("Length can't be less or equal to zero!");
    }
    else
    {
        FillArray(matrix);
        PrintArray(matrix);
        int sumMaxRow = SumMaxRow(matrix);
        int sumMinColumn = SumMinColumn(matrix);
        System.Console.WriteLine();
        System.Console.WriteLine($"Sum of max for rows = {sumMaxRow}");
        System.Console.WriteLine();
        System.Console.WriteLine($"Sum of min for columns = {sumMinColumn}");
        System.Console.WriteLine();
        System.Console.WriteLine($"SumMaxRows - SumMinColumns = {MaxMinusMin(sumMaxRow, sumMinColumn)}");
    }
}


Console.Clear();
System.Console.WriteLine("This program finds the maximum value in the matrix for each row,"
+ " gets the sum of these maximums. Then finds the minimum value for each column,"
+ " gets the sum of these minima. Then from the first sum (with maximums) subtracts the second sum (with minimums)");
System.Console.WriteLine();
int length = Prompt("Please enter length of cubic matrix: ");
int[,] matrix = new int[length, length];
System.Console.WriteLine();
DiffSumMaxRowSumMinColumn(length, matrix);
