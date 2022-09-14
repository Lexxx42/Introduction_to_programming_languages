// See https://aka.ms/new-console-template for more information




// f(1) =1
//f(2) = 1
//f(n) = f(n-1)+f(n-2)


double Fibonacci(int n)
{
    if(n==1|| n==2) return 1;
    else return Fibonacci(n-1)+Fibonacci(n-2);
}


for (int i = 1; i < 50; i++)
{
    System.Console.WriteLine($"f({i}) = {Fibonacci(i)} ");
}