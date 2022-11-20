// See https://aka.ms/new-console-template for more information

/* string Numbers(int a, int b)
{
    string result = String.Empty;
    for (int i = 1; i < b; i++)
    {
        result += $"{i} ";
    }
    return result;
} */


/* string Numbers(int a, int b)
{
    if (a<b) return $"{a} " + Numbers(a+1, b);
    else return String.Empty;
}

int b = 10;
System.Console.WriteLine(Numbers(1, b)); */

void ShowNumbers(int number)
{
    if(number==0) return;
    ShowNumbers(number - 1);
    System.Console.Write($"{number} ");
}
int number = 10;
ShowNumbers(number);




