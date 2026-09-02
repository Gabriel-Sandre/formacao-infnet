using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite a primeira data (dd/MM/yyyy): ");
        DateTime data1 = DateTime.Parse(Console.ReadLine());

        Console.Write("Digite a segunda data (dd/MM/yyyy): ");
        DateTime data2 = DateTime.Parse(Console.ReadLine());

        // Garante que a primeira data seja a mais antiga
        if (data1 > data2)
        {
            DateTime temp = data1;
            data1 = data2;
            data2 = temp;
        }

        // Calcula a diferença em dias utilizando TimeSpan
        TimeSpan diferenca = data2 - data1;

        // Calcula anos, meses e dias
        int anos = data2.Year - data1.Year;
        int meses = data2.Month - data1.Month;
        int dias = data2.Day - data1.Day;

        if (dias < 0)
        {
            meses--;

            DateTime mesAnterior = data2.AddMonths(-1);
            dias += DateTime.DaysInMonth(mesAnterior.Year, mesAnterior.Month);
        }

        if (meses < 0)
        {
            anos--;
            meses += 12;
        }

        Console.WriteLine();
        Console.WriteLine("Diferença entre as datas:");
        Console.WriteLine($"Anos: {anos}");
        Console.WriteLine($"Meses: {meses}");
        Console.WriteLine($"Dias: {dias}");
        Console.WriteLine($"Total de dias: {diferenca.Days}");
    }
}
