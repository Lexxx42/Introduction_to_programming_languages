/* Задача 2: Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.

M = 1; N = 15 -> 120
M = 4; N = 8. -> 30 */

int SegmentSum(int startNumber, int finishNumber) // Calculates sum of numbers in a segment.
{
    if (startNumber <= finishNumber) return (startNumber + SegmentSum(startNumber + 1, finishNumber));
    else return 0;
}

void MainSequence(int startNumber, int finishNumber) // If data is valid, prints results.
{
    if (startNumber <= 0 || finishNumber <= 0)
    {
        System.Console.WriteLine("Numbers have to be natural!");
    }
    else if (startNumber >= finishNumber)
    {
        System.Console.WriteLine("Segment starts with a lower value!");
    }
    else
    {
        System.Console.WriteLine($"Sum of numbers in a segment [{startNumber}..{finishNumber}]"
        + $" = {SegmentSum(startNumber, finishNumber)}");
    }
}


Console.Clear();

System.Console.WriteLine("This program prints sum of natural numbers"
+ " in a segment from startNumber to finishNumber");
System.Console.WriteLine();

int startNumber = 2;
int finishNumber = 5;

MainSequence(startNumber, finishNumber);
