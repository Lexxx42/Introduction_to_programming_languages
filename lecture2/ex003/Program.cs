


int[] array = {11, 241, 21, 66, 22, 7, 23, 77, 90, 22};


int n = array.Length;
int find = 22;

int index = 0;

while (index < n)
{
    if(array[index]== find)
    {
        System.Console.WriteLine(index);
        break;
    }
    index++;

}