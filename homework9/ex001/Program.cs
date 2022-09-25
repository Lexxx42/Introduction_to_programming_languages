/* Задача 1: 

Задайте значение N. 
Напишите программу, которая выведет все натуральные числа в промежутке от N до 1. 
Выполнить с помощью рекурсии.

N = 5 -> "5, 4, 3, 2, 1"
N = 8 -> "8, 7, 6, 5, 4, 3, 2, 1" */

void ShowNaturalNumbers(int number) // Shows natural numbers from number to 1.
{
    if(number==0) return;
    System.Console.Write($"{number} ");
    ShowNaturalNumbers(number - 1);
}

Console.Clear();
System.Console.WriteLine("This program shows natural numbers from inputNumber to 1.");
System.Console.WriteLine();
int inputNumber = 10;
ShowNaturalNumbers(inputNumber);