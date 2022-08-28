//3. Напишите программу вычисления функции:
// x = f(a) найти куб

int Prompt(string messege)
{
    Console.Write(messege);
    string strValue = Console.ReadLine() ?? "0";
    int value = int.Parse(strValue);
    return value;
}
int value = Prompt("введите число > ");
System.Console.WriteLine(value*value*value);