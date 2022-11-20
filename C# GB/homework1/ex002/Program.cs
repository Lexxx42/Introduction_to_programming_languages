//Задача 4: Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.
// Примеры с целыми числами, поэтому мы с ними и работаем.

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

int SearchForMax(int firstNumber, int secondNumber, int thirdNumber) // Compare numbers and search for max.
{
    int max = firstNumber;
    if (max < secondNumber)
    {
        max = secondNumber;
    }
    if (max < thirdNumber)
    {
        max = thirdNumber;
    }
    return max;
}


Console.Clear();
System.Console.WriteLine("This program find maximum of three numbers");
int number1 = Prompt("Please enter 1st number > ");
int number2 = Prompt("Please enter 2nd number > ");
int number3 = Prompt("Please enter 3rd number > ");
System.Console.WriteLine($"Max value = {SearchForMax(number1, number2, number3)}");
