// Задача 1
// Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
// 14212 -> нет
// 12821 -> да
// 23432 -> да

System.Console.WriteLine("This program takes at least 2 digit number as input and checks if it is a palindrome");

int Prompt(string message)
{
    System.Console.Write(message);
    return Convert.ToInt32(Console.ReadLine());
}

bool Validation(int numberForCheck)
{
    if (Math.Abs(numberForCheck) > 9 )
    {
        return true;
    }
    else
    {
        System.Console.WriteLine("Number has to be at least 2 digits");
        return false;
    }
}

void CheckForPalindrome(int numberForCheck)
{
    int reversedNumber = 0;
    int numberForCheckSaved = Math.Abs(numberForCheck);
    numberForCheck = Math.Abs(numberForCheck);
    while(numberForCheck>0)
    {
        reversedNumber *= 10;
        reversedNumber += numberForCheck % 10;
        numberForCheck /= 10;
    }
    System.Console.WriteLine($"reversedNumber = {reversedNumber}"); // just for me to check
    if(reversedNumber==numberForCheckSaved)
    {
        System.Console.WriteLine("Number is a palindrome!");
    }
    else
    {
        System.Console.WriteLine("Number isn't a palindrome!");
    }
    
}

int numberInput = Prompt("Please, enter the number > ");
if(Validation(numberInput))
{
    CheckForPalindrome(numberInput);
}
