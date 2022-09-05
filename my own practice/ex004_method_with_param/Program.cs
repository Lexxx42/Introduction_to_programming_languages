void WriteHello(string X)
{
Console.WriteLine($"Hello {X}");
}
void WriteHello1(string X, string Y)
{
Console.WriteLine($"Hello {X} {Y}");
}
void JustWriteSomething(string someThing)
{
Console.WriteLine(someThing);
}

// Person Alex;
// Alex = new Person();
// Console.Write("Введите имя > ");
// string Name = Console.ReadLine();
// Alex.firstName = Name;
// Console.Write("Введите second name > ");
// string secondName = Console.ReadLine();
// Alex.lastName = secondName;
// Alex.ShowFullName();


//как символ 5 перевести в цифру?




Person User;
User = new Person();
Console.Write("Введите имя > ");
User.firstName = Console.ReadLine();
Console.Write("Введите second name > ");
User.lastName = Console.ReadLine();
int num = User.LuckyNumber(14, 3);
Console.Write("how old are you? > ");
User.age = int.Parse(Console.ReadLine());
JustWriteSomething($"{User.firstName} is {User.age} years old");
User.ShowFullName();
JustWriteSomething($"{User.firstName}'s lucky number is {num}");

Person Anna;
Anna = new Person();
Anna.firstName = "Anna";
Anna.lastName = "asd";
num = Anna.LuckyNumber(24, 23);
JustWriteSomething($"Ann's lucky number is {num}");


//woking
// Console.Write("Введите имя >");
// string Name = Console.ReadLine();
// Console.Write("Введите second name >");
// string secondName = Console.ReadLine();
// WriteHello1(Name,secondName);





// пол часа разбирался почему код не работает, 
//оказывается определение класса надо писать после его использования.
// как-то контр-интуитивно

class Person
{
    //fields
    public string firstName;
    public string lastName;
    public int age;
    //method
    public void ShowFullName()
    {
        System.Console.WriteLine($"Name is {firstName} {lastName}");
    }
    public int LuckyNumber(int numberOfTeeth, int age)
    {
        return numberOfTeeth*age;
    }
}




