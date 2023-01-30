//iskluchenie povtorov in even
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




void PrintEven(int[] array)
{  
    System.Console.WriteLine("Search for even numbers in array");
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
    //Console.ReadKey(true);
    isFound=true;
    if(isFound==true)
    {
        System.Console.WriteLine("< Results");
    }
    else {System.Console.WriteLine("Not found even numbers!");}
}




// namespace ConsoleApplication10
// {
//     class Program
//     {
//         static void Main(string[] args)
//         {
//             int[] array = new int[20];
//             Random rand = new Random();
//             for (int i = 0; i < array.Length; i++)
//             {
//                 array[i] = rand.Next(0, 20);
//                 Console.Write(array[i] + " ");
//             }
//             System.Collections.ArrayList unique = new System.Collections.ArrayList();
            
//             for (int i = 0; i < array.Length; i++)
//                 if (unique.IndexOf(array[i]) == -1)
//                     unique.Add(array[i]);
 
//             Console.WriteLine();
//             for (int i = 0; i < unique.Count; i++)
//                 Console.Write(unique[i] + " ");
 
//             Console.ReadKey(true);
//         }
//     }
// }




int[] array = new int[new Random().Next(1,10)];
System.Console.WriteLine();
ArrayFill(array);
PrintArray(array);
PrintEven(array);