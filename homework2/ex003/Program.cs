//Задача 3: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.
// из условия не понятно откуда считать порядок цифр поэтому я, для разнообразия, буду считать справа налево

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

bool Validation(int numberForCheck) // Check number for a third digit.
{
    return Math.Abs(numberForCheck) > 99;
}

int SearchForThirdDigit(int numberForSearch) // Search for third digit in number.
{
    numberForSearch = Math.Abs(numberForSearch);
    int thirdDigit = numberForSearch;
    while (thirdDigit > 10)
    {
        thirdDigit /= 100; thirdDigit %= 10;
    }
    return thirdDigit;
}

void PrintThirdDigit(int number) // Print 3-rd digit in number.
{
    if (!Validation(number))
    {
        System.Console.WriteLine("There is no third digit!");
    }
    else
    {
        System.Console.WriteLine($"Third digit is -> {SearchForThirdDigit(number)}");
    }
}


Console.Clear();
System.Console.WriteLine("This program prints the third digit of the given number, or reports that there is no third digit.");
int inputNumber = Prompt("Please, enter some three-digit number > ");
PrintThirdDigit(inputNumber);
