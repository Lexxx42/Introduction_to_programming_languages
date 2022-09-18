// Задача 4: Задайте двумерный массив. Введите элемент, и найдите первое его вхождение,
// выведите позиции по горизонтали и вертикали, или напишите, что такого элемента нет.
// Например, такой массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4

// Введенный элемент 2, результат: [1, 4]

// Введенный элемент 6, результат: такого элемента нет.

// + посчитали количество найденных элементов
// эти элементы отправлили в конец массива
int Prompt(string messege)
{
    Console.Write(messege);
    string strValue = Console.ReadLine() ?? "0";
    bool isNumber = int.TryParse(strValue, out int value);
    if (isNumber)
    {
        return value;
    }
    throw new Exception("Данное значение не возможно преобразовать в число");
}

int[,] GenerateArray(int length, int minRange, int maxRange)
{
    var array = new int[length, length];
    var random = new Random();
    for (var i = 0; i < array.GetLength(0); i++)
    {
        for (var j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = random.Next(minRange, maxRange + 1);

        }
    }
    return array;
}

int[] FindElement(int[,] inputMatrix, int searchElement, int numberEntry)
{
    int[] answer = new int[2];
    int count = 0;
    for (int i = 0; i < inputMatrix.GetLength(0); i++)
    {
        for (int j = 0; j < inputMatrix.GetLength(1); j++)
        {
            if (inputMatrix[i, j] == searchElement)
            {
                answer[0] = i;
                answer[1] = j;
                count++;
                if (numberEntry == count)
                {
                    return answer;
                }
            }
        }

    }
    return answer;
}
int CountElements(int[,] inputMatrix, int searchElement)
{
    int count = 0;
    for (int i = 0; i < inputMatrix.GetLength(0); i++)
    {
        for (int j = 0; j < inputMatrix.GetLength(1); j++)
        {
            if (inputMatrix[i, j] == searchElement)
            {
                count++;
            }
        }

    }
    return count;
}

bool IsFound(int[] inputArray)
{
    return !(inputArray[0] == 0 && inputArray[1] == 0);
}

void SwapElemens(int[,] inputMatrix, int[] index, int[] ccords)
{
    int tempItem = inputMatrix[ccords[0], ccords[1]];
    inputMatrix[ccords[0], ccords[1]] = inputMatrix[index[0], index[1]];
    inputMatrix[index[0], index[1]] = tempItem;
}

void SortArray(int[,] inputMatrix, int elemen)
{
    int count = CountElements(inputMatrix, elemen);
    int[] coords = new int[2];
    int[] lastCoords = new int[2] { inputMatrix.GetLength(0) - 1, inputMatrix.GetLength(1) - 1 };
    while (count > 0)
    {
        coords = FindElement(inputMatrix, elemen, count);
        SwapElemens(inputMatrix, lastCoords, coords);
        lastCoords[1]--;
        if (lastCoords[1] < 0)
        {
            lastCoords[1] = inputMatrix.GetLength(1) - 1;
            lastCoords[0]--;
        }
        count--;
    }
}

void PrintArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            System.Console.Write($"{array[i, j]}\t");
        }
        System.Console.WriteLine();
    }
    System.Console.WriteLine();
}
int[,] numbers = GenerateArray(4, 0, 10);
PrintArray(numbers);
int searchNum = Prompt("Введите искомое число > ");
int[] answer = FindElement(numbers, searchNum, 2);
if (!IsFound(answer))
{
    System.Console.WriteLine("такого элемента нет.");
}
else
{
    System.Console.WriteLine($"{answer[0]},{answer[1]}");
    System.Console.WriteLine(CountElements(numbers, searchNum));
    SortArray(numbers, searchNum);
    PrintArray(numbers);
}