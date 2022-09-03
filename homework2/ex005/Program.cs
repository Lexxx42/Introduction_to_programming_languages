// Задача 5 *: Напишите программу, которая генерирует несколько случайных чисел, и в цикле проверяет, кратны ли эти числа предварительно введенному числу, 
//при кратности - цикл прерывается.
// Введенное число 2
// 13 -> нет
// 15 -> нет
// 12 -> да


// int[] RandomGenerator()
// {
//     int number_of_generations = new Random().Next(1,5);
//     int[] results = new int[number_of_generations];
//     for (int i = 0; i < results.Length; i++)
//     {
//         results[i] = new Random().Next(1,100);
//     }
//     return results;
// }

int Prompt(string message)
{
    System.Console.Write(message);        // Вывод приглашения
    string strValue;                      // Объявление переменной для ввода строки
    strValue = Console.ReadLine() ?? "0"; // Вводим строку с консоли (с консоли можно ввести только строку)
    int value = int.Parse(strValue);      // Преобразование строки в целое число
    return value;
}

System.Console.WriteLine("This program generates several random numbers, and in the loop checks if these numbers are multiples of the previously entered number, if the multiplicity is - the loop is interrupted.");
int value = Prompt("Please, enter a number > ");
CheckForMultiolicity(value);


// int[] array = RandomGenerator();
// for (int i = 0; i < array.Length; i++)
// {
//     System.Console.Write($"{array[i]} ");
// }


void CheckForMultiolicity (int received_number)
{
    while (true)
    {
        if(received_number==0){System.Console.WriteLine("Divided by zero!"); break;}
        if(Math.Abs(received_number)>99){System.Console.WriteLine("Sorry, our generated numbers is smaller than 100"); break;}
        int num1 = new Random().Next(1,100);
        int num2 = new Random().Next(1,100);
        int num3 = new Random().Next(1,100);
        System.Console.WriteLine($"Generated numbers > {num1}, {num2}, {num3}");
        if( num1 % received_number != 0 ) {System.Console.WriteLine($"{num1} -> no");}
        else if( num1 % received_number == 0 ) {System.Console.WriteLine($"{num1} -> yes"); break;}
        else if( num2 % received_number != 0 ) {System.Console.WriteLine($"{num2} -> no");}
        else if( num2 % received_number == 0 ) {System.Console.WriteLine($"{num2} -> yes"); break;}
        else if( num3 % received_number != 0 ) {System.Console.WriteLine($"{num3} -> no");}
        else if( num3 % received_number == 0 ) {System.Console.WriteLine($"{num3} -> yes"); break;}
    }
}