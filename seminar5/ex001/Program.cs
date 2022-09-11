// Задайте массив из 12 элементов, заполненный случайными числами из промежутка [-9, 9].
// Найдите сумму отрицательных и положительных элементов массива.
// Например, в массиве [3,9,-8,1,0,-7,2,-1,8,-3,-1,6] 
// сумма положительных чисел равна 29, сумма отрицательных равна -20.

const int NEGATIVE_VALUE = -1;
const int POSITIVE_VALUE = 1;

int Prompt(string message)
{
    Console.Write(message);
    bool isDigit = int.TryParse(Console.ReadLine(), out int number);
    if (isDigit){
        return number;
    }
    throw new Exception("Вы ввели не число");
}

int[] GenerateArray(int length, int minRandom, int maxRandom)
{
    Random rnd = new Random();
    int[] answer = new int[length];
    for (int i = 0; i < answer.Length; i++)
    {
        answer[i] = rnd.Next(minRandom, maxRandom + 1);
    }
    return answer;
}
void PrintArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        System.Console.Write(array[i]+ "\t");
    }
    System.Console.WriteLine();
}

int SumElements(int[] array, int sign = POSITIVE_VALUE)
{
    int sum = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if ((array[i] * sign) > 0)
        {
            sum += array[i];
        }
    }

    return sum;
}

const int MIN_ELEMENTS = -9;
const int MAX_ELEMENTS = 9;

int length = Prompt("Введите длину массива >");
int[] array = GenerateArray(length, MIN_ELEMENTS, MAX_ELEMENTS);
PrintArray(array);
System.Console.WriteLine($"Сумма положительных значений равна {SumElements(array)}");
System.Console.WriteLine($"Сумма отрицательных значений равна {SumElements(array, NEGATIVE_VALUE)}");
