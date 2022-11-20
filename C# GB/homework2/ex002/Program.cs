// Задача 2: Напишите программу, которая выводит случайное трёхзначное число и удаляет вторую цифру этого числа.

const int MIN = -200;
const int MAX = -100;

int NumberGeneration() // Generates random number.
{
    return new Random().Next(MIN, MAX);
}

(int, int) SearchForFirstSecondDigit(int numberForSearch) // Searches for first and second digit in number.
{
    numberForSearch = Math.Abs(numberForSearch);
    int lastDigit = numberForSearch;
    int firstDigit = numberForSearch;
    lastDigit = numberForSearch % 10;
    while (firstDigit >= 10)
    {
        firstDigit /= 10;
    }
    return (firstDigit, lastDigit);
}

void PrintNumberWithoutSecondDigit(int number) // Prints the number without 2-nd digit.
{
    (int firstDigit, int thirdDigit) = SearchForFirstSecondDigit(number);
    if (number > 0)
    {
        System.Console.WriteLine($"Number without second digit is > {firstDigit}{thirdDigit}");
    }
    else
    {
        System.Console.WriteLine($"Number without second digit is > {-firstDigit}{thirdDigit}");
    }
}


Console.Clear();
System.Console.WriteLine("This program prints a random three-digit number and removes the second digit of this number");
int numberGenerated = NumberGeneration();
System.Console.WriteLine($"Generated number is > {numberGenerated}");
PrintNumberWithoutSecondDigit(numberGenerated);
