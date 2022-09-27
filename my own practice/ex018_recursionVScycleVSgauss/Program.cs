// sum all numbers from N to M

// recursion
var startRec = DateTime.Now;
int SumRec(int n, int m)
{
    if (n>m)
    {
        return 0;
    }
    return n += SumRec(n+1,m);
}


// cycle
var startC = DateTime.Now;
int SumC(int n, int m)
{
    int sum = 0;
    for (int i = n; i < m+1; i++)
    {
        sum += i;
    }
    return sum;
}

// gauss
var startGauss = DateTime.Now;
long SumGauss(int n, int m)
{
    return (n+m)*(m-n)/2;
}


int n = 1;
int m = 19000;
var finishRec = DateTime.Now - startRec;
var finishC = DateTime.Now - startC;
var finishGauss = DateTime.Now - startGauss;

System.Console.WriteLine($"Time recursion: {finishRec}");
System.Console.WriteLine($"Sum from {n} to {m} = {SumRec(n,m)}");
System.Console.WriteLine();
System.Console.WriteLine($"Time cycle: {finishC}");
System.Console.WriteLine($"Sum from {n} to {m} = {SumC(n,m)}");
System.Console.WriteLine();
System.Console.WriteLine($"Time Gauss: {finishGauss}");
System.Console.WriteLine($"Sum from {n} to {m} = {SumGauss(n,m)}");


