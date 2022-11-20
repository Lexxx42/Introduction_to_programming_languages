/* Задача 3: Напишите программу, которая будет принимать на вход число и возвращать сумму его цифр. Использовать рекурсию.
453 -> 12
45 -> 9
*/

int SumDigit(int number)
{
    if (number<=0) return 0;
    return number%10 + SumDigit(number/10);
}

int number = 0;
System.Console.WriteLine($"Sum of digit = {SumDigit(number)}");
