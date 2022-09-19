// Задача 2: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.
// [3, 7, 23, 12] -> 19
// [-4, -6, 89, 6] -> 0

const int MINRANDOM = -3;
const int MAXRANDOM = 3;

int Prompt(string message) // Input values.
{
    Console.Write(message);
    bool isDigit = int.TryParse(Console.ReadLine(), out int number);
    if (isDigit)
    {
        return number;
    }
    throw new Exception("You didn't entered the number!");
}

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

void PrintArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        System.Console.Write(array[i] + "\t");
    }
    System.Console.WriteLine();
}

int SumOfOddPositions(int[] array)
{
    int sum = 0;
    for (int i = 1; i < array.Length; i += 2)
    {
        sum = sum + array[i];
    }
    return sum;
}

int Validation(int length) // Validation of array's length.
{
    if (length < 0)
    {
        return -1;
    }
    else if (length == 0)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}

void PrintSumOfOddPositions(int length) // Print sum of numbers in odd positions of the array.
{
    if (Validation(length) == 0)
    {
        System.Console.WriteLine("Your array has no elements!");
    }
    else if (Validation(length) == -1)
    {
        System.Console.WriteLine("Length can't be negative!");
    }
    else
    {
        System.Console.WriteLine();
        int[] array = GenerateArray(length);
        PrintArray(array);
        System.Console.WriteLine();
        System.Console.WriteLine($"Sum of elements in odd positions = {SumOfOddPositions(array)}");
    }
}


Console.Clear();
System.Console.WriteLine("This program creates an array filled with random numbers. And gives the sum of the elements in odd positions");
int length = Prompt("Please enter array's length > ");
PrintSumOfOddPositions(length);
