// Задача со звездочкой: Сформировать массив четной длины с парами элементов, каждого элемента должно быть в паре,
// 1,1,2,3,3,2,4,5,4,5
// I did it with user input.

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

(int, int) InputValuesToArray(string message) // Input pair.
{
    Console.Write(message);
    System.Console.WriteLine();
    bool isDigit1 = int.TryParse(Console.ReadLine(), out int number1);
    bool isDigit2 = int.TryParse(Console.ReadLine(), out int number2);
    if (isDigit1 && isDigit2)
    {
        return (number1, number2);
    }
    throw new Exception("You didn't entered the number OR number isn't integer!");
}

void PrintArray((int, int)[] array) // Print array.
{
    System.Console.WriteLine();
    for (int i = 0; i < array.Length; i++)
    {
        System.Console.Write(array[i] + "\t");
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

void PrintSequence(int length) // Prints coupled pairs of user input.
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
        (int, int)[] array = new (int, int)[length];

        for (int i = 0; i < array.Length; i++)
        {
            array[i] = InputValuesToArray($"Please enter {i + 1} pair of values > ");
        }
        PrintArray(array);
    }
}


Console.Clear();
System.Console.WriteLine("User enters an array of even length with pairs of elements, each element must be in a pair.");
int length = Prompt("Please enter array's length > ");
PrintSequence(length);
