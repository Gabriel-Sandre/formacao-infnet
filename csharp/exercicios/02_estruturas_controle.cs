using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite a nota (0 a 10): ");
        double nota = Convert.ToDouble(Console.ReadLine());

        string classificacao;

        if (nota < 6)
        {
            classificacao = "Insuficiente";
        }
        else if (nota < 7)
        {
            classificacao = "Regular";
        }
        else if (nota < 9)
        {
            classificacao = "Bom";
        }
        else
        {
            classificacao = "Excelente";
        }

        Console.WriteLine("Classificação: " + classificacao);
    }
}