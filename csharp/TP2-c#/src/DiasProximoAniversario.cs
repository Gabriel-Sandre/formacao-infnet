using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite sua data de nascimento (dd/MM/yyyy): ");
        DateTime nascimento = DateTime.Parse(Console.ReadLine());

        DateTime hoje = DateTime.Today;
        DateTime aniversario;

        // Verifica se a pessoa nasceu em 29 de fevereiro
        if (nascimento.Month == 2 && nascimento.Day == 29)
        {
            // Se o ano atual não for bissexto, usa 28 de fevereiro
            if (DateTime.IsLeapYear(hoje.Year))
            {
                aniversario = new DateTime(hoje.Year, 2, 29);
            }
            else
            {
                aniversario = new DateTime(hoje.Year, 2, 28);
            }
        }
        else
        {
            // Para as demais datas, usa o mesmo mês e dia normalmente
            aniversario = new DateTime(
                hoje.Year,
                nascimento.Month,
                nascimento.Day
            );
        }

        // Se o aniversário deste ano já passou,
        // calcula a data do próximo ano
        if (aniversario < hoje)
        {
            if (nascimento.Month == 2 && nascimento.Day == 29)
            {
                if (DateTime.IsLeapYear(hoje.Year + 1))
                {
                    aniversario = new DateTime(hoje.Year + 1, 2, 29);
                }
                else
                {
                    aniversario = new DateTime(hoje.Year + 1, 2, 28);
                }
            }
            else
            {
                aniversario = new DateTime(
                    hoje.Year + 1,
                    nascimento.Month,
                    nascimento.Day
                );
            }
        }

        int diasFaltam = (aniversario - hoje).Days;

        Console.WriteLine();
        Console.WriteLine($"Faltam {diasFaltam} dias para o próximo aniversário.");
    }
}
