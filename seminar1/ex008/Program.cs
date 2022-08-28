//факториал
// :)

int Prompt(string messege)
{
    Console.Write(messege);
    string strValue = Console.ReadLine() ?? "0";
    int value = int.Parse(strValue);
    return value;
}
int value = Prompt("введите число > ");
int factorial = 1;
if (value <0 )
{
    System.Console.WriteLine("должно быть больше нуля");
}
else 
{
    System.Console.WriteLine($"Факториал{value} -> {Factorial(value)}");
}

int Factorial(int value)
{
    int factorial=1;
    for (int i = 1; i <= value; i++)
    {
        factorial = factorial*i
    }
    return factorial;
}