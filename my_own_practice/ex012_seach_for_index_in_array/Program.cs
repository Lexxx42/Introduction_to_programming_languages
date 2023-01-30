

System.Console.WriteLine("this program seaches for number in the random-generated array in returns it's index");


int[] RandomGenerationArray()
{
    int[] arr = new int[new Random().Next(5, 15)];
    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = new Random().Next(1, 10);
    }
    return arr;
}

void PrintArray(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        System.Console.Write($"{arr[i]} ");
    }
}

int SearchForIndex(int[] arr, int numberForSearch)
{
    int index = 0;
    while (index < arr.Length)
    {
        if (arr[index] == numberForSearch)
        {
            return index;
            break;
        }
        index++;
    }
    return -1;
}


bool Validation(int number)
{
    if ((number < 10) && (number > 0))
    {
        return true;
    }
    else
    {
        return false;
    }
}


int Input(string message)
{
    System.Console.Write(message);
    return Convert.ToInt32(Console.ReadLine());
}



int number = Input("Please enter a number for search from 1 to 9 > ");

if (Validation(number) == true)
{
    int[] arr = RandomGenerationArray();
    System.Console.Write("Generated arry: ");
    PrintArray(arr);
    System.Console.WriteLine();
    int index = 0;
    index = SearchForIndex(arr, number);
    if (index == -1)
    {
        System.Console.WriteLine("Number is not found!");
    }
    else
    {
        System.Console.WriteLine($"Your number {number} is found! index = {index}");
    }
}
else
{
    System.Console.WriteLine("your number isn't correct!");
}
