using System;

class ContaBancaria
{
    private int numero;
    private string titular;
    private double saldo;

    public ContaBancaria(int numero, string titular)
    {
        this.numero = numero;
        this.titular = titular;
        this.saldo = 0;
    }

    public void Depositar(double valor)
    {
        if (valor > 0)
        {
            saldo = saldo + valor;
        }
    }

    public bool Sacar(double valor)
    {
        if (valor > 0 && valor <= saldo)
        {
            saldo = saldo - valor;
            return true;
        }

        return false;
    }

    public double ConsultarSaldo()
    {
        return saldo;
    }

    public void ApresentarDados()
    {
        Console.WriteLine("Número da conta: " + numero);
        Console.WriteLine("Titular: " + titular);
        Console.WriteLine("Saldo disponível: R$ " + saldo.ToString("F2"));
    }
}

class Program
{
    static void Main()
    {
        Console.Write("Número da conta: ");
        int numero = Convert.ToInt32(Console.ReadLine());

        Console.Write("Nome do titular: ");
        string titular = Console.ReadLine();

        ContaBancaria conta = new ContaBancaria(numero, titular);

        conta.Depositar(500);
        Console.WriteLine("\nDepósito de R$ 500,00 realizado.");

        if (conta.Sacar(200))
        {
            Console.WriteLine("Saque de R$ 200,00 realizado com sucesso.");
        }
        else
        {
            Console.WriteLine("Saque de R$ 200,00 recusado.");
        }

        if (conta.Sacar(1000))
        {
            Console.WriteLine("Saque de R$ 1000,00 realizado com sucesso.");
        }
        else
        {
            Console.WriteLine("Saque de R$ 1000,00 recusado: saldo insuficiente.");
        }

        Console.WriteLine("\n--- Dados finais da conta ---");
        conta.ApresentarDados();
        Console.WriteLine("Saldo final: R$ " + conta.ConsultarSaldo().ToString("F2"));
    }
}