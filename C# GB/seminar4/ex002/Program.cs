// Напишите программу, которая принимает на вход число и выдаёт количество цифр в числе.

int Prompt(string message)
{
    System.Console.Write(message);
    return Convert.ToInt32(Console.ReadLine());
}


int CountDigit(int number)
{
    int count = 1;
    while (number > 10)
    {
        number /= 10;
        count++;
    }
    return count;
}

bool Validation(int number)
{
    if (number >= 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int number = Prompt("enter the number>=0 > ");
if (Validation(number) == true)
{
    System.Console.WriteLine($"count = {CountDigit(number)}");
}
else
{
    System.Console.WriteLine("Number is invalid");
}

