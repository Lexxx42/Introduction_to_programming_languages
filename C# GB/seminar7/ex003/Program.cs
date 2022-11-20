//Задайте двумерный массив. Найдите элементы, у которых обе позиции чётные, и замените эти элементы на их квадраты.

int[,] GenerateArray(int rowLength, int colLength, int minRange, int maxRange)
{
    Random rnd = new Random();
    var array = new int[rowLength, colLength];
    for (var i = 0; i < array.GetLength(0); i++)
    {
        for (var j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = rnd.Next(minRange, maxRange);
        }
    }
    return array;
}

int[,] ChangeArray(int[,] arr)
{
    for (var i = 0; i < arr.GetLength(0); i = i + 2)
    {
        for (var j = 0; j < arr.GetLength(1); j += 2)
        {
            arr[i,j] *= arr[i,j];
        }
    }
    return arr;

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

int[,] myArray = GenerateArray(5,5,0,4);
PrintArray(myArray);
myArray = ChangeArray(myArray);
PrintArray(myArray);
