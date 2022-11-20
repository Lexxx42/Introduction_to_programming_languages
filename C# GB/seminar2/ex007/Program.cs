// 3.1. Напишите программу, которая будет принимать на вход пять чисел и выводить сумму и среднее арифметическое этих чисел.
// 2, 5, 6, 8, 1 -> сумма 22, среднее 4,4

int Prompt(string message)
{
    System.Console.Write(message);       
    string strValue;                      
    strValue = Console.ReadLine() ?? "0"; 
    int value = int.Parse(strValue);      
    return value;
}


// int num1 = Prompt("Введите число from 100 to 999 > ");
// int num2 = Prompt("Введите число from 100 to 999 > ");
// int num3 = Prompt("Введите число from 100 to 999 > ");
// int num4 = Prompt("Введите число from 100 to 999 > ");
// int num5 = Prompt("Введите число from 100 to 999 > ");

// System.Console.WriteLine($"summ={num1+num2+num3+num4+num5}, average={(num1+num2+num3+num4+num5)/5}");
double[] SumAvr(int[]num)
{
    int sum = 0;
    double average;
    for(int i=0; i<num.Length; i++)
    {
        sum += num[i];
    }
    average = sum/num.Length;
    double[] result = new double[2];
    result[0] = sum;
    result[1] = average;
    return result;
}


int[] numbers = new int[5];
for(int i=0; i<numbers.Length; i++)
{
    numbers[i] = Prompt($"Введите число from 100 to 999{i+1} > ");
}
// int sum = 0;
// double average;
// for(int i=0; i<numbers.Length; i++)
// {
//     sum += numbers[i];
// }
// average = sum/numbers.Length;
// System.Console.WriteLine($"summ={sum}, average={average}");
double[] result = SumAvr(numbers);
System.Console.WriteLine($"summ={result[0]}, average={result[1]}");

// :)

// у массива есть эти функции из "коробки" )
// От Владимир Морозов всем 03:59 PM
// int[] result = new int[2];
// От меня всем 03:59 PM
// спасибо, я понял
// От Владимир Морозов всем 04:00 PM
// result[0] = sum;
// result[1] = avg
// return result
