Person p = new Person("Petr", "Ivanov");


System.Console.WriteLine();




class Person
{
// Поля
string firstName;
string lastName;
// Первый метод-конструктор
// public Person()
// {
// firstName = "Johnny";
// lastName = "Rocket";

// }
// Второй метод-конструктор
public Person(string f, string l)
{
this.firstName = f;
this.lastName = l;
}
}
