// Задача 4: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным
// поскольку из условия не понятно, с чего начинается неделя, то я буду использовать американский стандарт, где неделя начинается с воскресенья

void CheckForDayOff(int day_of_a_week)
{   
    if((day_of_a_week<1) ^ (day_of_a_week>7))
    {
        System.Console.WriteLine("There is no such day of the week! Check your number, please!");
    }
    else if((day_of_a_week==1)^(day_of_a_week==7))
    {
        System.Console.WriteLine("Today is a day off! Yay!");
    }
    else
    {
        System.Console.WriteLine("Today is a weekday, go to work!");
    }
}

int Prompt(string message)
{
    System.Console.Write(message);        // Вывод приглашения
    string strValue;                      // Объявление переменной для ввода строки
    strValue = Console.ReadLine() ?? "0"; // Вводим строку с консоли (с консоли можно ввести только строку)
    int value = int.Parse(strValue);      // Преобразование строки в целое число
    return value;
}

System.Console.WriteLine("This program takes a number representing the day of the week as input and checks if that day is a holiday.");
int value = Prompt("Please, enter a number for day of a week from 1 to 7 > ");
CheckForDayOff(value);