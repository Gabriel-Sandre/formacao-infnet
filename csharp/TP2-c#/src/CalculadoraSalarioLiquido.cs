using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite o salário bruto: R$ ");
        double salarioBruto = double.Parse(Console.ReadLine());

        double imposto;

        if (salarioBruto <= 2000)
        {
            imposto = 0;
        }
        else if (salarioBruto <= 3000)
        {
            imposto = salarioBruto * 0.10;
        }
        else if (salarioBruto <= 5000)
        {
            imposto = salarioBruto * 0.15;
        }
        else
        {
            imposto = salarioBruto * 0.20;
        }

        double salarioLiquido = salarioBruto - imposto;

        Console.WriteLine();
        Console.WriteLine("===== CÁLCULO DO SALÁRIO =====");
        Console.WriteLine($"Salário bruto:  R$ {salarioBruto:F2}");
        Console.WriteLine($"Desconto:       R$ {imposto:F2}");
        Console.WriteLine($"Salário líquido: R$ {salarioLiquido:F2}");
        Console.WriteLine("==============================");
    }
}
