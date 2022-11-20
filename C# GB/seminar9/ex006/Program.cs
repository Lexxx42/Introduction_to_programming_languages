// 1 2 2 3 3 3 4 4 4 4 5 5
void Numbers(int n, int a = 1)
{
    if (n == 0)
    {
        return;
    }
    for (int i = 0; i < a; i++)
    {
        System.Console.Write(a + " ");
        n--;
        if (n == 0)
        {
            break;
        }
    }
    Numbers(n, a + 1);
}
Numbers(12);
