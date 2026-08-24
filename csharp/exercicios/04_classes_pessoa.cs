static void Main(string[] args)
{
    Pessoa pessoa1 = new Pessoa();
    pessoa1.nome = "Ricardo";
    pessoa1.idade = 40;
    Console.WriteLine("Pessoa instanciada!");
    Console.WriteLine($"Nome: {pessoa1.nome}");
    Console.WriteLine($"Idade: {pessoa1.idade}");

    Pessoa pessoa2 = new Pessoa();
    Console.WriteLine("Digite o nome da pessoa: ");
    pessoa2.nome = Console.ReadLine();
    Console.WriteLine("Digite a idade da pessoa: ");
    pessoa2.idade = int.Parse(Console.ReadLine());

    Console.WriteLine("Pessoa 2 instanciada: " + pessoa2);
    Console.WriteLine($"Nome: {pessoa2.nome}");
    Console.WriteLine($"Idade: {pessoa2.idade}");
}