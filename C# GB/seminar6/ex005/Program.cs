//Напишите программу, которая будет создавать копию заданного массива с помощью поэлементного копирования.

int[] GenerateArray(int length)
{
    int[] answer = new int[length];
    for (int i = 0; i < answer.Length; i++)
    {
        answer[i] = new Random().Next(0, 10);
    }
    return answer;
}

int[] ArrayCopyByElement(int[] arr)
{
    int[] resArray = new int[arr.Length];
    for (int i = 0; i < resArray.Length; i++)
    {
        resArray[i] = arr[i];
    }
    return resArray;
}
void PrintArray(int[] array)
{
    foreach (int item in array)
    {
        System.Console.Write($"{item}\t");
    }
    System.Console.WriteLine();
}
int[] array = GenerateArray(10);
array[7] = -100;
int[] myArray = ArrayCopyByElement(array);
int[] anotherArray = array; //Это ссылка на array!
PrintArray(array);
PrintArray(myArray);
PrintArray(anotherArray);
array[6] = 256;
System.Console.WriteLine();
PrintArray(array);
PrintArray(myArray);
PrintArray(anotherArray);
anotherArray[2] = 100500;
System.Console.WriteLine();
PrintArray(array);
PrintArray(myArray);
PrintArray(anotherArray);
