// Задача со звездочкой: Сформировать массив четной длины с парами элементов, каждого элемента должно быть в паре,
// 1,1,2,3,3,2,4,5,4,5



// (int, int) SumAll(int[] array)
// {
//     return (SumElements(array), SumElements(array, NEGATIVE_VALUE));
// }
// (int sumPlus, int sumMinus) = SumAll(array);
// System.Console.WriteLine($"{sumPlus}, {sumMinus}");




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


(int, int) InputValuesToArray(string message)
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


void PrintArray((int, int)[] array)
{
    System.Console.WriteLine();
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



System.Console.WriteLine("User enters an array of even length with pairs of elements, each element must be in a pair.");
int length = Prompt("Please enter array's length > ");
if (Validation(length) == true)
{
    if (length == 0) { System.Console.WriteLine("Your array has no elements!"); }
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
else
{
    System.Console.WriteLine("Length can't be negative!");
}
