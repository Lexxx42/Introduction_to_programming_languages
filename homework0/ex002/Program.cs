//Задача 4: Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.
//примеры снова с целыми числами, поэтому мы с ними и работаем

int Prompt(string message)
{
    System.Console.Write(message);        // Вывод приглашения
    string strValue;                      // Объявление переменной для ввода строки
    strValue = Console.ReadLine() ?? "0"; // Вводим строку с консоли (с консоли можно ввести только строку), если ничего не ввели, то = 0 
    int value = int.Parse(strValue);      // Преобразование строки в целое число
    return value;
}
Console.Clear();
System.Console.WriteLine("This program find maximum of three numbers");

int number1 = Prompt("please enter 1st number > ");
int number2 = Prompt("please enter 2nd number > ");
int number3 = Prompt("please enter 3rd number > ");

//for (int i = 0; i < 3; i++)
//{
//    int number[i] = Prompt($"please enter {i+1} number > ");
//}
//not working 

int max = number1;
if (max<number2)
{
    max = number2;
}
if (max<number3)
{
    max = number3;
}
System.Console.WriteLine($"max value = {max}");