// Задача 2
// Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.
// A (3,6,8); B (2,1,-7), -> 15.84
// A (7,-5, 0); B (1,-1,9) -> 11.53

const int XCOORD = 1;
const int YCOORD = 1;
const int ZCOORD = 1;

System.Console.WriteLine("This program takes as input the coordinates of two points and finds the distance between them in 3D space");

int Prompt(string message)
{
    System.Console.Write(message);
    return Convert.ToInt32(Console.ReadLine());
}

int[] InputCoords()
{
    int numberOfDots = 2;
    int[] xyzCoords = new int[numberOfDots];
    xyzCoords[XCOORD] = Prompt($"Please enter x coordinate > ");
    xyzCoords[YCOORD] = Prompt($"Please enter y coordinate > ");
    xyzCoords[YCOORD] = Prompt($"Please enter z  coordinate > ");
    return xyzCoords;
}


double Length(int[] firstCoord, int[] secondCoord)
{
    return Math.Sqrt(Math.Pow(firstCoord[XCOORD] - secondCoord[XCOORD], 2)
    + Math.Pow(firstCoord[YCOORD] - secondCoord[YCOORD], 2) + Math.Pow(firstCoord[ZCOORD] - secondCoord[ZCOORD], 2));
}

int[] firstPoint = InputCoords();
int[] secondPoint = InputCoords();
System.Console.WriteLine($"Length {Length(firstPoint, secondPoint):f2}");
