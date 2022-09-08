// mirror array

void PrintArray(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        System.Console.Write($"{arr[i]} ");
    }
}

int[] ArrayFill(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = new Random().Next(0, 10);
    }
    return arr;
}

int[] MirrorArray(int[] arr)
{
    for (int i = 0; i < arr.Length / 2; i++)
    {
        int temp = arr[i];
        arr[i] = arr[arr.Length - (i + 1)];
        arr[arr.Length - (i + 1)] = temp;
    }
    return arr;
}

int[] array = new int[new Random().Next(5, 10)];
ArrayFill(array);
System.Console.Write("array filled: ");
PrintArray(array);
System.Console.WriteLine();
System.Console.Write("array mirrored: ");
int[] mirrorArray = MirrorArray(array);
PrintArray(mirrorArray);