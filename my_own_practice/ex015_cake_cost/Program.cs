// Определите, сколько рублей и копеек нужно заплатить за N пирожков, если пирожок в столовой стоит А рублей и В копеек. 
// На вход 3 числа: рубли, копейки и количество пирожков. На выходе 2 числа: рубли и копейки.



int Prompt(string message)
{
    Console.Write(message);
    bool isDigit = int.TryParse(Console.ReadLine(), out int number);
    if (isDigit)
    {
        return number;
    }
    throw new Exception("You didn't entered the number!");
}

(int, int) CountCakes(int a, int b, int c)
{
    int rub = a;
    int cop = b;
    rub = rub * c;
    cop = cop * c;
    int temp = 0;
    while (cop >= 100)
    {
        cop -= 100;
        temp++;
    }
    rub=rub+temp;
    System.Console.WriteLine($"rub={rub}, cop={cop}");
    return (rub, cop);
}






System.Console.WriteLine("This program count quantity (N) of cakes you can buy for A rub and B copeeck");
int a = Prompt("enter cake cost rub: ");
int b = Prompt("enter cake cost cop: ");
int cake = Prompt("how much cakes do you want? ");
CountCakes(a, b, cake);