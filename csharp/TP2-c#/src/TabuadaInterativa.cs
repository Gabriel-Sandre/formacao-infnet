using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite um número: ");
        int numero = int.Parse(Console.ReadLine());

        Console.WriteLine();
        Console.WriteLine($"===== TABUADA DO {numero} =====");

        for (int i = 1; i <= 10; i++)
        {
            int resultado = numero * i;
            Console.WriteLine($"{numero} x {i} = {resultado}");
        }

        Console.WriteLine("==============================");
    }
}
