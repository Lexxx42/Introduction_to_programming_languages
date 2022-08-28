// 2. Напишите программу, которая будет выдавать название дня недели по заданному номеру.
// 	3 -> Среда 
// 5 -> Пятница

int Prompt(string messege)
{
    Console.Write(messege);
    string strValue = Console.ReadLine() ?? "0";
    int value = int.Parse(strValue);
    return value;
}

string[] days = { "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресение" };

int value = Prompt("Введите день недели > ");
if (value < 0 || value > 7)
{
    System.Console.WriteLine(" Нет такого дня недели ");
}
else
{
    int daysValue = value - 1;
    System.Console.WriteLine($"{value} -> {days[daysValue]}");
}
