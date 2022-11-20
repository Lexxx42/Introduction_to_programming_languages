// 2. Напишите программу, которая выводит случайное число из отрезка [10, 99] и показывает наибольшую цифру числа.
// 78 -> 8 
// 12-> 2 
// 85 -> 8

void chislo()
{
    int p = new Random().Next(10,100);
    System.Console.WriteLine($"p={p}");
    int a = p/10;
    int b = p%10;
    System.Console.WriteLine($"a={a}, b= {b}");
}
chislo();
// int Prompt(string message)
// {
//     System.Console.Write(message);        // Вывод приглашения
//     string strValue;                      // Объявление переменной для ввода строки
//     strValue = Console.ReadLine() ?? "0"; // Вводим строку с консоли (с консоли можно ввести только строку)
//     int value = int.Parse(strValue);      // Преобразование строки в целое число
//     return value;
// }

// int value = Prompt("Введите число from 10 to 99 > ");

