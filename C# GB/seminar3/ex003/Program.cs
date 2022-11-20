// Напишите программу, которая принимает на вход координаты 
//двух точек и находит расстояние между ними в 2D пространстве.
// A (3,6); B (2,1) -> 5,09 
// A (7,-5); B (1,-1) -> 7,21
const int XCOORD = 0;
const int YCOORD = 1;

int Prompt(string message)
{
    System.Console.Write(message);
    return Convert.ToInt32(Console.ReadLine());
}

int[] InsertCoords()
{
    int[] temp = new int[2];
    temp[XCOORD] = Prompt("Введите x > ");
    temp[YCOORD] = Prompt("Введите y > ");
    return temp;
}

double Length(int[] firstCoord, int[] secondCoord)
{
    return Math.Sqrt(Math.Pow(firstCoord[XCOORD] - secondCoord[XCOORD], 2)
    + Math.Pow(firstCoord[YCOORD] - secondCoord[YCOORD], 2));
}

int[] firstPoint = InsertCoords();
int[] secondPoint = InsertCoords();
System.Console.WriteLine($"Длина {Length(firstPoint,secondPoint):f2}");
