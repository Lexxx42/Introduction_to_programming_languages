using System;
using System.Linq;
using System.Text;
using System.Net.Http;
using ListMaster;


namespace ConsoleVS
{
    class Program
    {
        static public void Main(string[] args)
        {
            ArrayMaster am = new();
            for (int i = 0; i < 10; i++)
            {
                am.Add(new Random().Next(1,5));
            }
            for (int i = 0; i < am.GetCount(); i++)
            {
                Console.WriteLine(am.GetValue(i));
            }
        }
    }
}
