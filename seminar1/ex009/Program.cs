//вычислить числа фибоначи
int Prompt(string messege)
{
    Console.Write(messege);
    string strValue = Console.ReadLine() ?? "0";
    bool isNumber = int.TryParse(strValue, out int value);
    if (isNumber)
    {
        return value;
    } 
    throw new Exception("Данное начение не возможно преобразовать в целое число");
}
int value = Prompt("Введите число > ");
if (value < 0)
{
    System.Console.WriteLine("Число должно быть c нуля");
}
else
{
    System.Console.WriteLine($"Номер числа последовательности Фибонначи {value}. Значние числа-> {Fibbonachi(value)}");
}

int Fibbonachi(int value)
{
    int fibbonachi = 0;
    int tempVar1 = 0;
    int tempVar2 = 1;
    for (int i = 0; i <= value; i++)
    {        
        fibbonachi = tempVar1 + tempVar2;
        tempVar1 = tempVar2;
        tempVar2 = fibbonachi; 
    }
    return tempVar1;
}
