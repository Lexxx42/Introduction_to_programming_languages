// Задача 1
// Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
// 14212 -> нет
// 12821 -> да
// 23432 -> да

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

bool Validation(int numberForCheck) // Check number if it can be a palindrome.
{
    return Math.Abs(numberForCheck) > 9;
}

int ReverseNumber(int numberForReverse) // Reverse number's digits.
{
    int reversedNumber = 0;
    numberForReverse = Math.Abs(numberForReverse);
    while (numberForReverse > 0)
    {
        reversedNumber *= 10;
        reversedNumber += numberForReverse % 10;
        numberForReverse /= 10;
    }
    return reversedNumber;
}

void PrintPalindrome(int numberForCheck) // Prints if it's a palindrome or not.
{
    if (Validation(numberForCheck))
    {
        if (Math.Abs(numberForCheck) == ReverseNumber(numberForCheck))
        {
            System.Console.WriteLine("Number is a palindrome!");
        }
        else
        {
            System.Console.WriteLine("Number isn't a palindrome!");
        }
    }
    else
    {
        System.Console.WriteLine("Number has to be at least 2 digits");
    }

}


Console.Clear();
System.Console.WriteLine("This program takes at least 2 digit number as input and checks if it is a palindrome");
int numberInput = Prompt("Please, enter the number > ");
PrintPalindrome(numberInput);
