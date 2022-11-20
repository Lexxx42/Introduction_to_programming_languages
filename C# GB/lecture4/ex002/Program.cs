// See https://aka.ms/new-console-template for more information


int Factorial (int n)
{
    if(n == 1) return 1;
    else return n*Factorial(n-1);
}

for (int i = 1; i < 40; i++)
{
    System.Console.WriteLine($"{i}! = {Factorial(i)}");
}