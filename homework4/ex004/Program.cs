// Задачи 4: (*) Напишите программу, которая задаёт массив из 8 элементов случайными числами и выводит их на экран. 
// Также ищет второй максимум (число меньше максимального элемента, но больше всех остальных)
// 8 1 2 4 4 5 3 1 -> 5
// 1 2 6 9 8 1 1 1 -> 8
// 2 1 2 1 1 1 1 1 -> 1
// 1 2 1 2 1 1 1 1 -> 1
// 1 2 3 4 5 6 7 8 -> 7
// 1 2 3 4 5 6 8 7 -> 7
const int MIN = -10;
const int MAX = 10;

int[] CreationArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(MIN, MAX);
    }
    return array;
}

void PrintArray(int[] array)
{
    for (int i = 0; i < array.Length - 1; i++)
    {
        System.Console.Write($"{array[i]}\t");
    }
}

void SearchForMax(int[] array)
{
    int max1 = MIN-1;
    int max2 = MIN-1;
    int temp = MIN-1;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] > max1)
        {
            temp = max1;
            max1 = array[i];
            max2 = temp;

        }
        if (array[i] > max2 && array[i] < max1)
        {
            max2 = array[i];
        }
    }
    System.Console.WriteLine($"max = {max1}, second max = {max2}");
}


System.Console.WriteLine("This program sets an array of 8 elements with random"
+ "numbers and displays them on the screen. Also looks for the second maximum"
+ "(the number is less than the maximum element, but greater than all the others)");
System.Console.WriteLine();
int length = 8;
int[] array = new int[length];
PrintArray(CreationArray(array));
System.Console.WriteLine();
SearchForMax(array);
