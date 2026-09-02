using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite seu peso em kg: ");
        double peso = double.Parse(Console.ReadLine());

        Console.Write("Digite sua altura em metros: ");
        double altura = double.Parse(Console.ReadLine());

        double imc = peso / (altura * altura);

        string classificacao;

        if (imc < 18.5)
        {
            classificacao = "Abaixo do peso";
        }
        else if (imc < 25)
        {
            classificacao = "Peso normal";
        }
        else if (imc < 30)
        {
            classificacao = "Sobrepeso";
        }
        else if (imc < 35)
        {
            classificacao = "Obesidade Grau I";
        }
        else if (imc < 40)
        {
            classificacao = "Obesidade Grau II";
        }
        else
        {
            classificacao = "Obesidade Grau III";
        }

        Console.WriteLine();
        Console.WriteLine("========== RESULTADO ==========");
        Console.WriteLine($"Peso:          {peso:F2} kg");
        Console.WriteLine($"Altura:        {altura:F2} m");
        Console.WriteLine($"IMC:           {imc:F2}");
        Console.WriteLine($"Classificação: {classificacao}");
        Console.WriteLine("===============================");
    }
}
