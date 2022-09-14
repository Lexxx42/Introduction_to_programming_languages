// summ of even elements in array


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

int Validation(int len)
{
    if (len < 0)
    {
        return -1;
    }
    else if (len == 0)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}

int[] GenerationArray(int len)
{
    int[] array = new int[len];
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(-9, 10);
    }
    return array;
}

void PrintArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        System.Console.Write($"{array[i]} ");
    }
    System.Console.WriteLine();
}

int SumOfEven(int[] array)
{
    int sum = 0;
    for (int i = 0; i < array.Length; i += 2)
    {
        sum += array[i];
    }
    return sum;
}


int length = Prompt("Please enter array's length> ");
if (Validation(length) == 0)
{
    System.Console.WriteLine("Legth is 0!");
}
else if (Validation(length) == -1)
{
    System.Console.WriteLine("Length can't be negative!");
}
else
{
    int[] arr = GenerationArray(length);
    PrintArray(arr);
    System.Console.WriteLine($"summ of even elements = {SumOfEven(arr)}");
}