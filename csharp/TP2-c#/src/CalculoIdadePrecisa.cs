using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite sua data de nascimento (dd/MM/yyyy): ");
        DateTime nascimento = DateTime.Parse(Console.ReadLine());

        DateTime hoje = DateTime.Today;

        int anos = hoje.Year - nascimento.Year;
        int meses = hoje.Month - nascimento.Month;
        int dias = hoje.Day - nascimento.Day;

        // Ajusta os dias quando o dia atual é menor que o dia do nascimento
        if (dias < 0)
        {
            meses--;

            DateTime mesAnterior = hoje.AddMonths(-1);
            dias += DateTime.DaysInMonth(mesAnterior.Year, mesAnterior.Month);
        }

        // Ajusta os meses quando necessário
        if (meses < 0)
        {
            anos--;
            meses += 12;
        }

        Console.WriteLine();
        Console.WriteLine($"Sua idade é: {anos} anos, {meses} meses e {dias} dias.");
    }
}
