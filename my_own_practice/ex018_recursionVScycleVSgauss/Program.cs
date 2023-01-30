// sum all numbers from N to M

int n = 1;
int m = 19003;

Console.Clear();
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
System.Console.WriteLine($"Sum from {n} to {m} = {SumRec(n,m)}");
var finishRec = DateTime.Now - startRec;
System.Console.WriteLine($"Time recursion: {finishRec}");

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
System.Console.WriteLine($"Sum from {n} to {m} = {SumC(n,m)}");
var finishC = DateTime.Now - startC;
System.Console.WriteLine($"Time cycle: {finishC}");

// gauss
var startGauss = DateTime.Now;
int SumGauss(int n, int m)
{
    return (n+m)*(m-n+1)/2;
}
System.Console.WriteLine($"Sum from {n} to {m} = {SumGauss(n,m)}");
var finishGauss = DateTime.Now - startGauss;
System.Console.WriteLine($"Time Gauss: {finishGauss}");
