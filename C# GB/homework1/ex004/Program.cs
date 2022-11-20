// Задача 8: Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
// Целые числа.

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

bool Validation(int numberForCheck) // Segment's length check.
{
    return numberForCheck == 1;
}

void PrintSegment(int segmentEnd) // Prints all even numbers in segment.
{
    if (segmentEnd > 0 && !Validation(segmentEnd))
    {
        System.Console.Write($"Even numbers in segment (1, {segmentEnd}]: ");
        System.Console.Write("2");
        for (int i = 4; i <= segmentEnd; i += 2)
        {
            System.Console.Write($", {i}");
        }
    }
    else if (segmentEnd <= 0 && !Validation(segmentEnd))
    {
        System.Console.Write($"Even numbers in segment [{segmentEnd}, 1): ");
        System.Console.Write("0");
        for (int i = 2; i <= Math.Abs(segmentEnd); i += 2)
        {
            System.Console.Write($", {-i}");
        }
    }
    else
    {
        System.Console.Write($"There is nothing between 1 and 1");
    }
}


Console.Clear();
System.Console.WriteLine("This program takes a number (N) and returns all even numbers from (1 to N]");
int number = Prompt("Please enter a number, which will be a segment's end > ");
PrintSegment(number);
