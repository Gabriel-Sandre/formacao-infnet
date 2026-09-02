using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite um número: ");
        int numero = int.Parse(Console.ReadLine());

        for (int i = numero; i >= 0; i--)
        {
            if (i > 0)
            {
                Console.Write(i + ", ");
            }
            else
            {
                Console.WriteLine(i);
            }
        }
    }
}
