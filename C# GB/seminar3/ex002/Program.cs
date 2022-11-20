// Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


int Prompt(string message)
{
    System.Console.Write(message);
    return Convert.ToInt32(Console.ReadLine());
}

bool ValidateQuarter(int x)
{
    if (x>0 && x<5)
    {
        return true;
    }

    System.Console.WriteLine("такой четверти нет");
    return false;
}

void DeterminateQuarter(int x)
{
      if (x==1)
    {
        System.Console.WriteLine("X>0, Y>0");
    }
    if (x==2)
    {
        System.Console.WriteLine("X<0, Y>0");
    }
    if (x==3)
    {
        System.Console.WriteLine("X<0, Y<0");
    }
    if (x==4)
    {
        System.Console.WriteLine("X>0, Y<0");
    }  
}

int quarter = Prompt("Введите номер четверти > ");
if (ValidateQuarter(quarter))
{
    DeterminateQuarter(quarter);
}
