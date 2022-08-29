// *. Напишите программу вычисления модуля числа.
// 	2 -> 2
// 	-3 -> 3
// 	-7 -> 7
int Prompt(string messege)
{
    Console.Write(messege);
    string strValue = Console.ReadLine() ?? "0";
    int value = int.Parse(strValue);
    return value;
}
int value = Prompt("введите число > ");
int result;
if (value<0)
{
    result = -value;
}
else
{
    result = value;
}
System.Console.WriteLine($"{value} -> {result}");