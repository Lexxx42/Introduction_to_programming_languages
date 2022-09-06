// Задача 2: Напишите программу, которая выводит случайное трёхзначное число и удаляет вторую цифру этого числа.

void ThreeDigitNumberWithoutMiddle(int X)
{
    int result = -1;
    if(X==0) {result = new Random().Next(100,1000);}
    if(X==1) {result = new Random().Next(-999,-101);} //ошибка! нельзя включать -1000!

    System.Console.WriteLine($"Our random number is > {result}");
    int last_digit = result;
    int first_digit = result;
    if(result > 0)
    {
        last_digit = result%10;
        while (first_digit > 10) { first_digit /= 10; }
    }
    else
    {
        last_digit = -result%10;
        while (first_digit < -10) { first_digit /= 10; }
    }
    System.Console.WriteLine($"Number without middle digit is {first_digit}{last_digit}");
}
System.Console.WriteLine("This program prints a random three-digit number and removes the second digit of this number");
ThreeDigitNumberWithoutMiddle(new Random().Next(0,2));

