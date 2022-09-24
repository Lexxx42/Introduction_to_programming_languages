// Составить частотный словарь элементов двумерного массива. 
// Частотный словарь содержит информацию о том, сколько раз встречается элемент входных данных. 
// Значения элементов массива 0..9

int[,] GenerateArray(int rowLength, int colLength, int minRange, int maxRange)
{
    var array = new int[rowLength, colLength];
    var random = new Random();
    for (var i = 0; i < array.GetLength(0); i++)
    {
        for (var j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = random.Next(minRange, maxRange);

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

void PrintDict(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        System.Console.Write($"{i} = {array[i]}; ");
    }
    System.Console.WriteLine();
}

int[] FreqDictionary(int[,] arr)
{
    int[] count = new int[10];
    foreach (var item in arr)
    {
        count[item] += 1;
    }
    return count;
}
int[,] myArray = GenerateArray(5,5,0,10);
PrintArray(myArray);
int[] dict = FreqDictionary(myArray);
PrintDict(dict);



