
Animal Barsik;
Barsik = new Animal();
Barsik.kindOfAnimal = "Cat";
Barsik.name = "Кот Барсик";
Barsik.numberOfLegs = 4;
Barsik.height = 50;
Barsik.length = 110;
Barsik.color = "Black";
Barsik.hasTail = true;
Barsik.isMammal = true;


void SayHello()
{
    Console.WriteLine($"hello {Barsik.name}");
}

int numberOfLegs(string animalName)
{
    if (animalName == "slon")
    {
        return 4;
    }
    else if(animalName == "indeyka")
    {
        return 2;
    }
    else if(animalName=="Ustricha")
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
void JustWriteSomething(string someThing)
{
Console.WriteLine(someThing);
}



SayHello();

int i; // save number of legs
i = numberOfLegs("slon");
System.Console.WriteLine($"slon has {i} legs");
i = numberOfLegs("Alex");
System.Console.WriteLine($"Alex has {i} legs");
i = numberOfLegs("Кот Барсик");
System.Console.WriteLine($"Barsik has {Barsik.numberOfLegs} legs");
JustWriteSomething("you are a big guy");
JustWriteSomething("For You");














class Animal
{
    public string kindOfAnimal;
    public string name;
    public int numberOfLegs;
    public int height;
    public int length;
    public string color;
    public bool hasTail;  //private if nothing typed
    public bool isMammal;
    public bool spellingCorrect;
}


