using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite seu nome: ");
        string nome = Console.ReadLine();

        Console.Write("Digite sua idade: ");
        int idade = int.Parse(Console.ReadLine());

        Console.Write("Digite seu telefone: ");
        string telefone = Console.ReadLine();

        Console.Write("Digite seu e-mail: ");
        string email = Console.ReadLine();

        Console.WriteLine();
        Console.WriteLine("===== DADOS CADASTRADOS =====");
        Console.WriteLine($"Nome:      {nome}");
        Console.WriteLine($"Idade:     {idade} anos");
        Console.WriteLine($"Telefone:  {telefone}");
        Console.WriteLine($"E-mail:    {email}");
        Console.WriteLine("=============================");
    }
}
