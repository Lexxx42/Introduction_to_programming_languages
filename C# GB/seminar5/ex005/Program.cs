/*
Найдите произведение пар чисел в одномерном массиве. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
Результат запишите в новом массиве.
[1 2 3 4 5] -> 5 8 3
[6 7 3 6] -> 36 21 
*/

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

int[] array = GenerateArray(11, 0, 5);
int[] PairMultiply(int[] array)
{
    int[] result = new int[array.Length / 2 + array.Length % 2];
    for (int i = 0; i < result.Length; i++)
    {
        result[i] = array[i] * array[array.Length - 1 - i];
    }
    return result;
}
PrintArray(array);
System.Console.WriteLine();
PrintArray(PairMultiply(array));


/*
(int, int) SumAll(int[] array)
{
    return (SumElements(array), SumElements(array, NEGATIVE_VALUE));
}
(int sumPlus, int sumMinus) = SumAll(array);
System.Console.WriteLine($"{sumPlus}, {sumMinus}");
*/