// Задача 1: Напишите программу, которая принимает на 
//вход три числа и проверяет, может ли существовать треугольник с сторонами такой длины.
//Теорема о неравенстве треугольника: каждая сторона треугольника меньше суммы двух других сторон.
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

bool TriangleExist(int[] sides)
{
    if (sides[0] < sides[1] + sides[2] && sides[1] < sides[0] + sides[2] && sides[2] < sides[1] + sides[0])
    {
        return true;
    }
    return false;
}
void Answer(bool answer)
{
    if (answer)
    {
        System.Console.WriteLine("Треуголиник существует");
    }
    else
    {
        System.Console.WriteLine("Треуголиник не существует");
    }
}

int[] side = new int[3];
for (int i = 0; i < side.Length; i++)
{
    side[i] = Prompt($"Введите сторону {i + 1} > ");
}
Answer(TriangleExist(side));
