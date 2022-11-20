// Задача 5 *: Напишите программу, которая генерирует несколько случайных чисел, и в цикле проверяет, кратны ли эти числа предварительно введенному числу, 
//при кратности - цикл прерывается.
// Введенное число 2
// 13 -> нет
// 15 -> нет
// 12 -> да

const int MIN = 1;
const int MAX = 100;

int Prompt(string message) // Input values.
{
    Console.Write(message);
    bool isDigit = int.TryParse(Console.ReadLine(), out int number);
    if (isDigit)
    {
        return number;
    }
    throw new Exception("You didn't enter a number");
}

int Validation(int numberForCheck) // Check input number for 0 and the number in range of generation.
{
    numberForCheck = Math.Abs(numberForCheck);
    if (numberForCheck == 0)
    {
        return 0;
    }
    else if (numberForCheck > MAX)
    {
        return 1;
    }
    else
    {
        return 2;
    }
}

int NumberGeneration() // Generates random number.
{
    return new Random().Next(MIN, MAX);
}

void CheckForMultiplicity(int number) // Prints results of multiplicity: "yes" if multiplicity is, else "no".
{
    while (true)
    {
        if (Validation(number) == 0)
        {
            System.Console.WriteLine("Divided by zero!");
            break;
        }
        if (Math.Abs(number) > 99)
        {
            System.Console.WriteLine("Sorry, your number is out of generation maximum.");
            break;
        }
        int generatedNumber = NumberGeneration();
        System.Console.WriteLine($"Generated number > {generatedNumber}");
        if (generatedNumber % number != 0)
        {
            System.Console.WriteLine($"{generatedNumber} -> no");
        }
        else if (generatedNumber % number == 0)
        {
            System.Console.WriteLine($"{generatedNumber} -> yes");
            break;
        }
    }
}


Console.Clear();
System.Console.WriteLine("This program generates several random numbers,"
+ "and in the loop checks if these numbers are multiples of the previously entered number,"
+ " if the multiplicity is - the loop is interrupted.");
int inputNumber = Prompt("Please, enter a number > ");
CheckForMultiplicity(inputNumber);
