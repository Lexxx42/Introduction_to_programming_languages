//fibonachi

int Prompt(string messege)
{
    Console.Write(messege);
    string strValue = Console.ReadLine() ?? "0";
    int value = int.Parse(strValue);
    bool isNumber = int.TryParse(strValue,out int value);
    if (isNumber)
    {
        return value;
    }
    throw new Exception("данное значение нельзя преобразовать в целое число");
}
int value = Prompt("введите число > ");

if (value <0 )
{
    System.Console.WriteLine("должно быть больше нуля");
}
else 
{
    System.Console.WriteLine($"номер числа фибонначи {value} -> {Fib(value)}");
}

int Fib (int value)
{
    int fib1 = 0;
    int temp1 = 0;
    int temp2 = 1;
    for (int i == 0; i <= value; i++=)
    {
        fib1 = temp1+temp2;
        temp1 = temp2;
        temp2=fib1;
    }
    return temp1;
}