// **. Напишите программу, которая на вход принимает значение, а  на выходе показывает обратное значение.
// 1 -> 1 
// 2 -> 0.5
// 0.25 -> 4

double Prompt(string messege)
{
    Console.Write(messege);
    string strValue = Console.ReadLine() ?? "0";
    double value = double.Parse(strValue);
    return value;
}

double value = Prompt("введите число > ");
double result;
result = 1/value;
System.Console.WriteLine($"{value} -> {result}");