// Задача 3: Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран.
// 1, 2, 5, 7, 19 -> [1, 2, 5, 7, 19]
// 6, 1, 33 -> [6, 1, 33]
// do we enter these numbers?


//random generation
int[] CreationArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(0, 100);
    }
    return array;
}

void PrintArray(int[] array)
{
    System.Console.Write("[");
    for (int i = 0; i < array.Length - 1; i++)
    {
        System.Console.Write($"{array[i]}, ");
    }
    System.Console.Write($"{array[array.Length - 1]}");
    System.Console.Write("]");
    System.Console.WriteLine();
}


//input 8 elements -> array
int Prompt(string message)
{
    System.Console.Write(message);
    return Convert.ToInt32(Console.ReadLine());
}

int[] ArrayFill(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = Prompt("Please, enter the number > ");
    }
    return array;
}

System.Console.WriteLine("This program defines an array of 8 elements and displays them on the screen: random generation");
System.Console.WriteLine();
int[] array = new int[new Random().Next(3, 9)];
PrintArray(CreationArray(array));

System.Console.WriteLine("This program defines an array of 8 elements and displays them on the screen: input numbers from user");
System.Console.WriteLine();
int length = 8;
int[] array1 = new int[length];
PrintArray(ArrayFill(array1));
