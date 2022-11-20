// Задайте двумерный массив размером m×n, заполненный случайными целыми числами.

int[,] GenerateArray(int rowLength, int colLength, int minRange, int maxRange)
{
    var array = new int[rowLength, colLength];
    var random = new Random();
    for (var i = 0; i < array.GetLength(0); i++)
    {
        for (var j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = random.Next(minRange, maxRange + 1);

        }
    }
    return array;
}

void PrintArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            System.Console.Write($"{array[i, j]}\t");
        }
        System.Console.WriteLine();
    }
    System.Console.WriteLine();
}

void PrintArrayForeach(int[,] array)
{
    foreach (var item in array)
    {
        System.Console.Write($"{item}\t");
    }
    System.Console.WriteLine();
    System.Console.WriteLine();
}

int[,] array = GenerateArray(5, 4, 0, 10);
PrintArray(array);
PrintArrayForeach(array);
