// Задача 3: Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран.
// 1, 2, 5, 7, 19 -> [1, 2, 5, 7, 19]
// 6, 1, 33 -> [6, 1, 33]
// do we enter these numbers?

const int MIN = 0;
const int MAX = 100;
const int lengthArray = 8;

int[] CreationArray(int[] array) // Generates array, filled with random numbers.
{
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(MIN, MAX);
    }
    return array;
}

void PrintArray(int[] array) // Prints the array.
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

int[] ArrayFill(int[] array) // Filling the array with user's numbers.
{
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = Prompt("Please, enter the number > ");
    }
    System.Console.WriteLine();
    return array;
}


// Random generation of array.
Console.Clear();
System.Console.WriteLine("This program defines an array of 8 elements and displays them on the screen: random generation");
System.Console.WriteLine();
int[] array = new int[lengthArray];
PrintArray(CreationArray(array));
System.Console.WriteLine();

// User generation of array.
System.Console.WriteLine("This program defines an array of 8 elements and displays them on the screen: input numbers from user");
System.Console.WriteLine();
int length = 8;
int[] array1 = new int[length];
PrintArray(ArrayFill(array1));
