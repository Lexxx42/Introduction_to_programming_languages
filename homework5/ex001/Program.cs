// Задача 1: Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.
// [345, 897, 568, 234] -> 2
const int MINRANDOM = 100;
const int MAXRANDOM = 999; // only positive 3 digit numbers allowed!

int[] GenerateArray(int length)
{
    Random rnd = new Random();
    int[] array = new int[length];
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = rnd.Next(MINRANDOM, MAXRANDOM + 1);
    }
    return array;
}

int Prompt(string message)
{
    Console.Write(message);
    bool isDigit = int.TryParse(Console.ReadLine(), out int number);
    if (isDigit)
    {
        return number;
    }
    throw new Exception("You didn't entered the number!");
}

void PrintArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        System.Console.Write(array[i] + "\t");
    }
    System.Console.WriteLine();
}

int CountEven(int[] array)
{
    int count = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] % 2 == 0)
        {
            count++;
        }
    }
    return count;
}

bool Validation(int length)
{
    if (length < 0) { return false; }
    return true;
}

System.Console.WriteLine("This program fills an array filled with random positive three-digit numbers. And will show the number of even numbers in the array");
int length = Prompt("Please enter array's length > ");
if (Validation(length) == true)
{
    if (length == 0) { System.Console.WriteLine("Your array has no elements!"); }
    else
    {
        int[] array = GenerateArray(length);
        PrintArray(array);
        System.Console.WriteLine($"There are {CountEven(array)} even numbers in the array");
    }
}
else
{
    System.Console.WriteLine("Length can't be negative!");
}
