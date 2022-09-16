/* table of multiplicative but in 2d array */
/* Shift+alt+A */

void PrintArray(int[,] matr)
{
    for (int i = 1; i < matr.GetLength(0); i++)
    {
        for (int j = 1; j < matr.GetLength(1); j++)
        {
            System.Console.Write($"{matr[i, j]} ");
        }
        System.Console.WriteLine();
    }
}

void FillArray(int[,] matr)
{
    
    for (int i = 0; i < matr.GetLength(0); i++)
    {
        for (int j = 0; j < matr.GetLength(1); j++)
        {
            matr[i, j] = i * j;
        }
    }
}

int length = 10;
int[,] matrix = new int[length, length];

System.Console.WriteLine();
FillArray(matrix);
PrintArray(matrix);

