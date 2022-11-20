/* Задача 1: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.

0, 7, 8, -2, -2 -> 2

1, -7, 567, 89, 223-> 3 */

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

bool Validation(int quantity) // Check quantity of numbers.
{
    return quantity <= 0;
}

int[] InputArray(int length) // Input values into array.
{
    int[] arr = new int[length];
    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = Prompt($"Please enter {i + 1} number: ");
    }
    return arr;
}

void PrintArray(int[] array) // Print array.
{
    for (int i = 0; i < array.Length; i++)
    {
        System.Console.Write($"{array[i]} ");
    }
    System.Console.WriteLine();
}

int CountNumbers(int[] array) // Counts the same numbers in array.
{
    int count = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] > 0)
        {
            count++;
        }
    }
    return count;
}

void PrintQuantity(int quantity) // Prints quantity of the same numbers in array.
{
    if (Validation(quantity))
    {
        System.Console.WriteLine("Quantity of numbers must be greater than 0!");
    }
    else
    {
        int[] inputArray = InputArray(quantity);
        System.Console.WriteLine();
        PrintArray(inputArray);
        System.Console.WriteLine();
        System.Console.WriteLine($"Quantity of numbers greater than zero = {CountNumbers(inputArray)}");
    }
}


Console.Clear();
System.Console.WriteLine($"This program takes M as quantity of numbers, numbers. And returns quantity of ones which greater than zero");
System.Console.WriteLine();
int quantity = Prompt("Please enter quantity of number, which you want to input: ");
System.Console.WriteLine();
PrintQuantity(quantity);
