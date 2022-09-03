//Задача 3: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.
// из условия не понятно откуда считать порядок цифр поэтому я, для разнообразия, буду считать справа налево


int ThirdDigit(int X)
{   
    int third_digit = X;
    if(Math.Abs(X)<100) {System.Console.WriteLine("There is no 3rd number"); third_digit=-1;}
    else if (X > 99)
    {
        while (third_digit > 10) { third_digit /=100; third_digit %= 10;}
        return third_digit;
    }
    else
    {
        while (third_digit < -10) { third_digit /=100; third_digit %= 10;}
        return -third_digit;
    }
    return third_digit;
}

int Prompt(string message)
{
    System.Console.Write(message);        // Вывод приглашения
    string strValue;                      // Объявление переменной для ввода строки
    strValue = Console.ReadLine() ?? "0"; // Вводим строку с консоли (с консоли можно ввести только строку)
    int value = int.Parse(strValue);      // Преобразование строки в целое число
    return value;
}

System.Console.WriteLine("This program prints the third digit of the given number, or reports that there is no third digit.");
int value = Prompt("Please, enter some three-digit number > ");


System.Console.WriteLine($"Third digit is -> {ThirdDigit(value)} <- if output = -1, then there is no third digit!");
