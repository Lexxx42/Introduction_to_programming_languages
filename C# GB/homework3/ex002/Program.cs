// Задача 2
// Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.
// A (3,6,8); B (2,1,-7), -> 15.84
// A (7,-5, 0); B (1,-1,9) -> 11.53

const int XCOORDINATE = 1;
const int YCOORDINATE = 1;
const int ZCOORDINATE = 1;

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

int[] InputCoordinates() // Input Coordinates.
{
    int numberOfDots = 2;
    int[] xyzCoords = new int[numberOfDots];
    xyzCoords[XCOORDINATE] = Prompt($"Please enter x coordinate > ");
    xyzCoords[YCOORDINATE] = Prompt($"Please enter y coordinate > ");
    xyzCoords[ZCOORDINATE] = Prompt($"Please enter z  coordinate > ");
    return xyzCoords;
}

double Length(int[] firstCoord, int[] secondCoord) // Length calculation.
{
    return Math.Sqrt(Math.Pow(firstCoord[XCOORDINATE] - secondCoord[XCOORDINATE], 2)
    + Math.Pow(firstCoord[YCOORDINATE] - secondCoord[YCOORDINATE], 2) + Math.Pow(firstCoord[ZCOORDINATE] - secondCoord[ZCOORDINATE], 2));
}


Console.Clear();
System.Console.WriteLine("This program takes as input the coordinates of two points and finds the distance between them in 3D space");
int[] firstPoint = InputCoordinates();
int[] secondPoint = InputCoordinates();
System.Console.WriteLine($"Length {Length(firstPoint, secondPoint):f2}");
