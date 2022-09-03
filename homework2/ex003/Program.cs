//Задача 3: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.


int ThirdNumber(int X)
{   
    int third_digit = X;
    bool isFound = false;
    if(Math.Abs(X)<100) {System.Console.WriteLine("There is no 3rd number"); isFound=true; third_digit=-1;}
    else if ((X > 99) & (isFound==false))
    {
        while (third_digit > 10) { third_digit /=100; third_digit %= 10;}
        isFound=true;
    }
    else if((X < -99) & (isFound==false))
    {
        while (third_digit < -10) { third_digit /=100; third_digit %= 10;}
        isFound=true;
    }
    else
    {
        System.Console.WriteLine("is it real?");
        isFound=true;
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

//System.Console.WriteLine("This program takes a three-digit number as input and outputs the second digit of that number.");
int value = Prompt("Please, enter some three-digit number > ");
System.Console.WriteLine("This program prints the third digit of the given number, or reports that there is no third digit.");

ThirdNumber(value);
System.Console.WriteLine(ThirdNumber(value));
