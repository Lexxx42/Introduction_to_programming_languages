// Задача 8: Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
// Целые числа

int Prompt(string message)
{
    System.Console.Write(message);        // Вывод приглашения
    string strValue;                      // Объявление переменной для ввода строки
    strValue = Console.ReadLine() ?? "0"; // Вводим строку с консоли (с консоли можно ввести только строку), если ничего не ввели, то = 0 
    int value = int.Parse(strValue);      // Преобразование строки в целое число
    return value;
}
Console.Clear();
System.Console.WriteLine("This program takes a number (N) and returns all even numbers from 1 to N");
int number = Prompt("please enter a number > ");
if(number == 1) 
{
    System.Console.Write($"there is nothing between 1 and 1");
}

if(number>0)
{
    for (int i = 1; i <= number; i++)
    {
        if(i%2 == 0)
        {
                if(i==number-1) 
                {
                    System.Console.Write($"{i}");
                }
                else
                { 
                if(i==number) 
                {
                    System.Console.Write($"{i}");
                } 
                else 
                {
                    System.Console.Write($"{i}, ");
                }
                }
            
            //System.Console.Write($"{i}, ");
        }
        
    }
}
else
{
    if(number == 0) 
    {
        System.Console.Write($"0");
    }
    else 
    {
        System.Console.Write($"0, ");
        for ( int i = 1; i <= -number; i++)
        {
            if(i%2 == 0)
            {
                 if(i==-number-1) 
                {
                    System.Console.Write($"{-i}");
                }
                else
                { 
                if(i==-number) 
                {
                    System.Console.Write($"{-i}");
                } 
                else 
                {
                    System.Console.Write($"{-i}, ");
                }
                }
                
                //System.Console.Write($"-{i}, ");
            }
            
        }
    }
}

//чет не работает с отрицательными, при вводе 0 и 1 выдает 2, что за пределами!
// но цикл круче, согласен. Нужно адаптировать!
// System.Console.Write("2");
//     for (int i = 4; i <= number; i+=2){
//         System.Console.Write($", {i}");
//     }