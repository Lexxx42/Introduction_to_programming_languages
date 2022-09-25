/* Задача 60. 

Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. 
Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.

Массив размером 2 x 2 x 2

66(0,0,0) 25(0,1,0)
34(1,0,0) 41(1,1,0)
27(0,0,1) 90(0,1,1)
26(1,0,1) 55(1,1,1) 
*/
// я описание не понял.

//Задача 4: * Напишите программу, которая заполнит спирально квадратный массив.

int Prompt(string message) // Input values.
{
    Console.Write(message);
    bool isDigit = int.TryParse(Console.ReadLine(), out int number);
    if (isDigit)
    {
        return number;
    }
    throw new Exception("You didn't enter a number");
}

int[,] SpiralFillMatrix(int length) // Fills spirally the matrix.
{
    int[,] matrix = new int[length, length];

    int directionX = 1;
    int directionY = 0;

    int row = 0;
    int column = 0;

    int directionChanges = 0;
    int steps = length;

    for (int i = 0; i < matrix.Length; i++)
    {
        matrix[row, column] = i + 1;
        if (--steps == 0)
        {
            steps = length * (directionChanges % 2) + length * ((directionChanges + 1) % 2) - (directionChanges / 2 - 1) - 2;
            int temp = directionX;
            directionX = -directionY;
            directionY = temp;
            directionChanges++;
        }
        column += directionX;
        row += directionY;
    }
    return matrix;
}

void PrintMatrix(int[,] matrix) // Matrix print.
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            System.Console.Write($"{matrix[i, j]}\t");
        }
        System.Console.WriteLine();
    }
    System.Console.WriteLine();
}


int cubicMatrixLength = Prompt("Enter cubic matrix length > ");
System.Console.WriteLine();
if (cubicMatrixLength <= 0)
{
    System.Console.WriteLine("Length can't be less or equal to zero!");
}
else
{
    PrintMatrix(SpiralFillMatrix(cubicMatrixLength));
}
