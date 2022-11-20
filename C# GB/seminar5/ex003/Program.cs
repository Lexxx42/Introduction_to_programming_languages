/*
Задайте массив. Напишите программу, которая определяет, присутствует ли заданное число в массиве.
4; массив [6, 7, 19, 345, 3] -> нет
3; массив [6, 7, 19, 345, 3] -> да
*/

int Prompt(string message)
{
    Console.Write(message);
    bool isDigit = int.TryParse(Console.ReadLine(), out int number);
    if (isDigit)
    {
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
    System.Console.WriteLine("Новый сгенерированный массив: ");
    for (int i = 0; i < array.Length; i++)
    {
        System.Console.Write(array[i] + "\t");
    }
    System.Console.WriteLine();
}
bool SearchResult(int[] array, int searchNum)
{
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] == searchNum)
        {
            return true;
        }
    }
    return false;
}

const int MIN_ELEMENTS = -99;
const int MAX_ELEMENTS = 99;

int ArrayLen = Prompt("Введите длину массива > ");
int[] array = GenerateArray(ArrayLen, MIN_ELEMENTS, MAX_ELEMENTS);
PrintArray(array);

int searchNum = Prompt("Введите искомое число > ");

if (SearchResult(array, searchNum))
{
    System.Console.WriteLine("ok");
}
else
{
 System.Console.WriteLine("not ok ^_^");
}
