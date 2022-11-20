/* Задача 3: Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.
m = 2, n = 3 -> A(m,n) = 9
m = 3, n = 2 -> A(m,n) = 29 */

// Ackermann's function.
int Ackermann(int m, int n)
{
    if (m == 0) return n + 1;
    if (m != 0 && n == 0) return Ackermann(m - 1, 1);
    if (m > 0 && n > 0) return Ackermann(m - 1, Ackermann(m, n - 1));
    return Ackermann(m, n);
}

// Main sequence checks the numbers and call's other methods.
void MainSequence(int firstNumber, int secondNumber)
{
    if (firstNumber < 0 || secondNumber < 0)
    {
        System.Console.WriteLine("Numbers have to be greater than zero!");
    }
    else
    {
        System.Console.WriteLine($"Ackermann({firstNumber},{secondNumber}) = {Ackermann(firstNumber, secondNumber)}");
    }
}


int m = 2;
int n = 0;
MainSequence(m, n);
