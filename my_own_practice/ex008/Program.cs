// Random rnd = new Random();
void ArrayFill(int[] collection)
{
    int length = collection.Length;
    int index = 0;
    while(index<length)
    {
        collection[index]=new Random().Next(0,10);
        index++;
    }
}

void PrintArray(int[] col)
{
    int count = col.Length;
    int position = 0;
    while(position<count)
    {
        System.Console.Write($"{col[position]} ");
        position++;
    }
    System.Console.WriteLine();
}

void Find(int[] arr, int looking_number)
{
    int leng = arr.Length;
    int pos = 0;
    bool isFound = false;
    while(pos<leng)
    {
        if (looking_number == arr[pos])
        {
            System.Console.WriteLine($"Looking number is {looking_number}, found in position {pos}!");
            isFound = true;
            break;
        }
        pos++;
    }
    if (isFound==false)
    {
        System.Console.WriteLine($"Number {looking_number} is not found!");
    }
}

int[] Max(int[]mass) //2 transform type into array!
{
     System.Console.WriteLine("Let's find a maximum and it's position!");
    int pos = 0;
    int max = mass[0];
    int pos_max = 0; // 1 hoch posiciyu nayti kak vivesti 2 results?
    while (pos<mass.Length)
    {
        if(mass[pos]>max)
        {
            max = mass[pos];
            pos_max = pos;
        }
        pos++;
    }
    int[]max_results={0,0};
    max_results[0]=max;
    max_results[1]=pos_max;
    return max_results;
}

void PrintEven(int[] array)
{  
    System.Console.WriteLine("Search for uniq even numbers in array");
    bool isFound = false;
    System.Collections.ArrayList unique = new System.Collections.ArrayList();
    for (int index = 0; index < array.Length; index++)
    {
        if(array[index]%2==0)
        {
        if (unique.IndexOf(array[index]) == -1)
        {
            unique.Add(array[index]);
        }
        }
    }
    Console.WriteLine();
    for (int i = 0; i < unique.Count; i++)
    {
        Console.Write(unique[i] + " ");
    }
    //Console.ReadKey(true); //wait for key event
    isFound=true;
    if(isFound==true)
    {
        System.Console.WriteLine("< Results");
    }
    else {System.Console.WriteLine("Not found even numbers!");}
}

void Lucky_number()
{
    int X = new Random().Next(-100,100);
    System.Console.WriteLine($"Lucky number is {X}!");
}








int[] array = new int[new Random().Next(1,10)];
int number_for_search = new Random().Next(0,10);
System.Console.WriteLine($"Number for search = {number_for_search}, let's find it!");
ArrayFill(array);
PrintArray(array);
Find(array, number_for_search);
//System.Console.WriteLine($"{Max(array)} - maximum value");
int[] p = Max(array); //неужели нельзя без этого?
System.Console.WriteLine($"max is {p[0]} , max positon is {p[1]}");
PrintEven(array);
Lucky_number(); // merge success



