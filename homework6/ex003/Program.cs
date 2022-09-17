/* Найдите максимальное значение в матрице по каждой строке, получите сумму этих максимумов. 
Затем найдите минимальное значение по каждой колонке,получите сумму этих минимумов. 
Затем из первой суммы (с максимумами) вычтите вторую сумму(с минимумами)
1 2 3
3 4 5
3+5=8, 1+2+3=6, 8-6=2 */


int Prompt(string message)
{
    Console.Write(message);
    bool isDigit = int.TryParse(Console.ReadLine(), out int number);
    if (isDigit)
    {
        return number;
    }
    throw new Exception("You didn't enter a number");
}

void PrintArray(int[,] matr)
{
    for (int i = 0; i < matr.GetLength(0); i++)
    {
        for (int j = 0; j < matr.GetLength(1); j++)
        {
            System.Console.Write($"{matr[i, j]} ");
        }
        System.Console.WriteLine();
    }
}

void FillArray(int[,] matr)
{
    for (int i = 0; i < matr.GetLength(0); i++)
    {
        for (int j = 0; j < matr.GetLength(1); j++)
        {
            matr[i, j] = new Random().Next(1, 10);
        }
    }
}

int SumMaxRow(int[,] matr)
{
    int sum = 0;
    for (int i = 0; i < matr.GetLength(0); i++)
    {
        int maxRow = matr[i, 0];
        for (int j = 0; j < matr.GetLength(1); j++)
        {
            if (matr[i, j] > maxRow)
            {
                maxRow = matr[i, j];
            }
        }
        sum += maxRow;
    }
    return sum;
}

int SumMinCol(int[,] matr)
{
    int sum = 0;
    for (int i = 0; i < matr.GetLength(0); i++)
    {
        int minCol = matr[0, i];
        for (int j = 0; j < matr.GetLength(1); j++)
        {
            if (matr[j, i] < minCol)
            {
                minCol = matr[j, i];
            }
        }
        sum += minCol;
    }
    return sum;
}

int MaxMinusMin(int max, int min)
{
    return max - min;
}

bool Validation(int length)
{
    if (length <= 0)
    {
        return false;
    }
    return true;
}

void Result(int length, int[,] matrix)
{
    if (Validation(length) == false)
    {
        System.Console.WriteLine("Length can't be less or equal to zero!");
    }
    else
    {
        FillArray(matrix);
        PrintArray(matrix);
        int sumMaxRow = SumMaxRow(matrix);
        int sumMinCol = SumMinCol(matrix);
        System.Console.WriteLine();
        System.Console.WriteLine($"Sum of max for rows = {sumMaxRow}");
        System.Console.WriteLine();
        System.Console.WriteLine($"Sum of min for columns = {sumMinCol}");
        System.Console.WriteLine();
        System.Console.WriteLine($"SumMax - SumMin = {MaxMinusMin(sumMaxRow, sumMinCol)}");
    }
}



System.Console.WriteLine("This program finds the maximum value in the matrix for each row,"
+ " gets the sum of these maximums. Then finds the minimum value for each column,"
+ " gets the sum of these minima. Then from the first sum (with maximums) subtracts the second sum (with minimums)");
System.Console.WriteLine();
int length = Prompt("Please enter length of cubic matrix: ");
int[,] matrix = new int[length, length];
System.Console.WriteLine();
Result(length, matrix);
