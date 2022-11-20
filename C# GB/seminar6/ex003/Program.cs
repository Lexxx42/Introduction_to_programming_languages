// Задача 2: Напишите программу, которая будет преобразовывать десятичное число в двоичное.
// 45 -> 101101
// 3  -> 11
// 2  -> 10
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

int[] ConvertToBinary(int num)
{
    int[] array = new int[ArraySize(num)];
    int counnt = array.Length - 1;    
    while (num > 0)
    {
        array[counnt] = num % 2;        
        num = num / 2;        
        counnt--;
    }
    return array;
}
int ArraySize(int inputNum)
{
    int count = 0;
    if (inputNum ==0)
    {
        return 1;
    }
    while (inputNum > 0)
    {
        inputNum = inputNum / 2;
        count++;
    }
    return count;
}
void PrintArray(int[] array)
{    
    for (int i = 0; i < array.Length; i++)
    {
        System.Console.Write($"{array[i]}");
    }    
}
int num = Prompt("Введите число > ");
PrintArray(ConvertToBinary(num));
