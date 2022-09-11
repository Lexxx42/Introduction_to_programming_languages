// Задача 2: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.
// [3, 7, 23, 12] -> 19
// [-4, -6, 89, 6] -> 0

const int MINRANDOM = -100;
const int MAXRANDOM = 100;

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

int SummOfOddPositions(int[] array)
{
    int sum = 0;
    for (int i = 1; i < array.Length; i++)
    {
        if(i%2!=0)
        {
            sum = sum + array[i];
        }
    }
    return sum;
}

bool Validation(int length)
{
    if (length < 0) { return false; }
    return true;
}

System.Console.WriteLine("This program creates an array filled with random numbers. And gives the sum of the elements in odd positions");
int length = Prompt("Please enter array's length > ");
if (Validation(length) == true)
{
    if (length == 0) { System.Console.WriteLine("Your array has no elements!"); }
    else
    {
        int[] array = GenerateArray(length);
        PrintArray(array);
        System.Console.WriteLine($"Sum of elements in odd positions = {SummOfOddPositions(array)}");
    }
}
else
{
    System.Console.WriteLine("Length can't be negative!");
}
