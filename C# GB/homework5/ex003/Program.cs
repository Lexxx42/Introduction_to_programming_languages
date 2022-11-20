// Задача 3: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.
// [3 7 22 2 78] -> 76

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

double InputValuesToArray(string message) // Input values to the array.
{
    Console.Write(message);
    double number = 0;
    bool isDigit = double.TryParse(Console.ReadLine(), out number);
    if (isDigit)
    {
        return number;
    }
    throw new Exception("You didn't entered the number!");
}

void PrintArray(double[] array) // Print array.
{
    for (int i = 0; i < array.Length; i++)
    {
        System.Console.Write($"{array[i]}" + "\t");
    }
    System.Console.WriteLine();
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

double FindMin(double[] array) // Finds the minimum value in the array.
{
    double min = array[0];
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] < min)
        {
            min = array[i];
        }
    }
    return min;
}

double FindMax(double[] array) // Finds the maximum value in the array.
{
    double max = array[0];
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] > max)
        {
            max = array[i];
        }
    }
    return max;
}

void PrintDiffMaxMin(int length) // Prints difference between maximum and minimum array's values.
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
        double[] array = new double[length];
        for (int i = 0; i < length; i++)
        {
            array[i] = InputValuesToArray($"Please enter {i} element of your array > ");
        }
        PrintArray(array);
        System.Console.WriteLine($"{FindMax(array)} - {FindMin(array)} = {FindMax(array) - FindMin(array):f2}");
    }
}


Console.Clear();
System.Console.WriteLine("The user enters an array of real numbers. "
+ "The program finds the difference between the maximum and minimum elements of an array.");
int length = Prompt("Please enter array's length > ");
PrintDiffMaxMin(length);
