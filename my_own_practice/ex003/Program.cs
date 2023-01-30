Person Alex;
Alex = new Person();
Alex.firstName = "Alexander";
Alex.lastName = "Konuchov";
Alex.ShowFullName();






// пол часа разбирался почему код не работает, 
//оказывается определение класса надо писать после его использования.
// как-то контр-интуитивно

class Person
{
    //fields
    public string firstName;
    public string lastName;
    //method
    public void ShowFullName()
    {
        System.Console.WriteLine($"Name is {firstName} {lastName}");
    }
}

