// 3. Напишите программу, которая будет принимать на вход два числа и выводить,
// является ли второе число кратным первому. Если число 2 не кратно числу 1, то программа выводит остаток от деление.
// 34, 5 -> не кратно, остаток 4 
// 16, 4 -> кратно

int first = new Random().Next(1,10);
int second = new Random().Next(1,10);

if(first%second==0)
{
    int result = first%second;
    System.Console.WriteLine("cool!");
    System.Console.WriteLine($"first number={first}, second number={second}, {first}%{second}={result}"); // just for looking
}
else
{
    double result = first%second;
    System.Console.WriteLine($"first number={first}, second number={second}, {first}%{second}={result}");
}
