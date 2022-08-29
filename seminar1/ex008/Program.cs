//вычислить факториал числа
int Prompt(string messege)
{
    Console.Write(messege);
    string strValue = Console.ReadLine() ?? "0";
    int value = int.Parse(strValue);
    return value;
}
int value = Prompt("Введите число > ");
if (value < 0)
{
    System.Console.WriteLine("Число должно быть больше нуля");
}
else
{
    System.Console.WriteLine($"Факториал числа {value} равен -> {Factorial(value)}");
}

int Factorial(int value)
{
    int factorial = 1;
    for (int i = 1; i <= value; i++)
    {
        factorial = factorial * i;
    }
    return factorial;
}
