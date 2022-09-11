// Напишите программу замены элементов массива: положительные элементы замените на соответствующие отрицательные, и наоборот.
// [-4, -8, 8, 2] -> [4, 8, -8, -2]


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
    for (int i = 0; i < array.Length; i++)
    {
        System.Console.Write(array[i] + "\t");
    }
    System.Console.WriteLine();
}

int[] ArrayFillPositive(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        if ((array[i]) < 0)
        {
            array[i] = array[i] * -1;
        }
    }
    return array;
}

const int MIN_ELEMENTS = -9;
const int MAX_ELEMENTS = 9;

int length = Prompt("Введите длину массива >");
System.Console.WriteLine();
int[] array = GenerateArray(length, MIN_ELEMENTS, MAX_ELEMENTS);
System.Console.Write("Generated array: ");
PrintArray(array);
ArrayFillPositive(array);
System.Console.WriteLine();
System.Console.Write("Changed signs to positives array: ");
PrintArray(array);