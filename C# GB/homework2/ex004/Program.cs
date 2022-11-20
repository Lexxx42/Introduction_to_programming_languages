// Задача 4: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным
// поскольку из условия не понятно, с чего начинается неделя, то я буду использовать американский стандарт, где неделя начинается с воскресенья

int Prompt(string message) // Input values.
{
    Console.Write(message);
    bool isDigit = int.TryParse(Console.ReadLine(), out int number);
    if (isDigit)
    {
        return number;
    }
    throw new Exception("You didn't enter a number");
}

bool Validation(int dayOfWeekForCheck) // Check day of a week.
{
    return dayOfWeekForCheck < 1 ^ dayOfWeekForCheck > 7;
}

void PrintDayOfWeek(int dayOfWeek) // Print day of a week.
{
    if (Validation(dayOfWeek))
    {
        System.Console.WriteLine("There is no such day of the week! Check your number, please!");
    }
    else
    {
        if ((dayOfWeek == 1) ^ (dayOfWeek == 7))
        {
            System.Console.WriteLine("Today is a day off! Yay!");
        }
        else
        {
            System.Console.WriteLine("Today is a weekday, go to work!");
        }
    }
}


Console.Clear();
System.Console.WriteLine("This program takes a number representing the day of the week as input and checks if that day is a holiday.");
int value = Prompt("Please, enter a number for day of a week from 1 to 7 > ");
PrintDayOfWeek(value);
