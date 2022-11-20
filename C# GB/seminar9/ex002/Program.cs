/* Задача 2: Задайте значения M и N. Напишите программу, которая рекурсивно выведет все натуральные числа в промежутке от M до N.
M = 1; N = 5 -> "1, 2, 3, 4, 5"
M = 4; N = 8 -> "4, 5, 6, 7, 8"
 */

void Numbers(int a, int b)
{
    if (a == b)
    {
        System.Console.WriteLine(a);
        return;
    }
    System.Console.Write($"{a} ");
    Numbers(a+1, b);
}
Numbers(4, 8);
