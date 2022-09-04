int Prompt(string message)
{
    System.Console.Write(message);
    return Convert.ToInt32(Console.ReadLine());
}

int factorial = Prompt("Введите число для подсчета его факториала:");

int FactorialCalc(int number)
{
    int fact = 1;
    for (int i = 1; i <= number; i++) 
    {
        fact = fact * i;       
    }
    return fact;
}

System.Console.WriteLine(FactorialCalc(factorial));
