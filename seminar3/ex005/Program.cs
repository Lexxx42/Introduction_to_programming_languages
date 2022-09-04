// Напишите программу, которая генерирует последовательность случайных чисел из 10 элементов в диапазоне от 1 до 10, 
// и подсчитывает, сколько сгенерировалось чисел больше 5.
void Print(double[] numbers)
{
    for (int i = 0; i < numbers.Length; i++)
    {
        System.Console.Write($"{numbers[i]:f2} \t");
    }
    System.Console.WriteLine();
}
double[] GenerateArray(int size)
{
    double[] numbers = new double[size];
    for (int i = 0; i < numbers.Length; i++)
    {
        numbers[i] = new Random().Next(1, 10) + new Random().NextDouble();
    }
    return numbers;
}
int Count(double[] numbers)
{
    int count = 0;
    for (int i = 0; i < numbers.Length; i++)
    {
        if (numbers[i] > 5)
        {
            count++;
        }
    }
    return count;

}
double[] numbers = GenerateArray(10);
Print(numbers);
System.Console.WriteLine(Count(numbers));
