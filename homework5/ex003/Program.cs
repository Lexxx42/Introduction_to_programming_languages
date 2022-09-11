// Задача 3: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.
// [3 7 22 2 78] -> 76


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

double InputValuesToArray(string message)
{
    Console.Write(message);
    bool isDigit = double.TryParse(Console.ReadLine(), out double number);
    if (isDigit)
    {
        return number;
    }
    throw new Exception("You didn't entered the number!");
}

void PrintArray(double[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        System.Console.Write(array[i] + "\t");
    }
    System.Console.WriteLine();
}


bool Validation(int length)
{
    if (length < 0) { return false; }
    return true;
}

double FindMin(double[] array)
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

double FindMax(double[] array)
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




System.Console.WriteLine("The user enters an array of real numbers. The program finds the difference between the maximum and minimum elements of an array.");
int length = Prompt("Please enter array's length > ");
if (Validation(length) == true)
{
    if (length == 0) { System.Console.WriteLine("Your array has no elements!"); }
    else
    {
        double[] array = new double[length];
        for (int i = 0; i < length; i++)
        {
            array[i] = InputValuesToArray($"Please enter {i} element of your array > ");
        }
        PrintArray(array);
        System.Console.WriteLine($"{FindMax(array)} - {FindMin(array)} = {FindMax(array) - FindMin(array)}");
    }
}
else
{
    System.Console.WriteLine("Length can't be negative!");
}
