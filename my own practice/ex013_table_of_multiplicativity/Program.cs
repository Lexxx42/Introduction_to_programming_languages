// table of multiplicativity

System.Console.WriteLine("this program prints table of multiplicativity from 2 to 10");

void multiplicativity()
{
    for (int i = 2; i <= 10; i++)
    {
        for (int j = 2; j <= 10; j++)
        {
            System.Console.WriteLine($"{i} x {j} = {i*j}");
        }
        System.Console.WriteLine();
    }
}

multiplicativity();