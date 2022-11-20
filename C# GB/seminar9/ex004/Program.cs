/* Задача 4: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
 */


int Pow(int num, int pow)
{
    if(pow<=0) return 1;
    return num * Pow(num, pow-1);
}

int number = 2;
int pow = 1;
System.Console.WriteLine($"{number}pow({pow}) = {Pow(number, pow)}");