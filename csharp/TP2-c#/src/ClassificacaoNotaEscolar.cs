using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite uma nota de 0 a 10: ");
        double nota = double.Parse(Console.ReadLine());

        if (nota < 0 || nota > 10)
        {
            Console.WriteLine("Nota inválida. Digite uma nota entre 0 e 10.");
        }
        else if (nota < 6)
        {
            Console.WriteLine("Classificação: Insuficiente");
        }
        else if (nota < 7)
        {
            Console.WriteLine("Classificação: Regular");
        }
        else if (nota < 9)
        {
            Console.WriteLine("Classificação: Bom");
        }
        else
        {
            Console.WriteLine("Classificação: Excelente");
        }
    }
}
