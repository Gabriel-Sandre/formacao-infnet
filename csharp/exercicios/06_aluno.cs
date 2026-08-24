using System;

class Aluno
{
    private int matricula;
    private string nome;
    private string curso;
    private int idade;
    private double nota1;
    private double nota2;

    public Aluno()
    {
    }

    public Aluno(int matricula, string nome, string curso, int idade, double nota1, double nota2)
    {
        this.matricula = matricula;
        this.nome = nome;
        this.curso = curso;
        this.idade = idade;
        this.nota1 = nota1;
        this.nota2 = nota2;
    }

    public void LerDados()
    {
        Console.Write("Matrícula: ");
        matricula = Convert.ToInt32(Console.ReadLine());

        Console.Write("Nome: ");
        nome = Console.ReadLine();

        Console.Write("Curso: ");
        curso = Console.ReadLine();

        Console.Write("Idade: ");
        idade = Convert.ToInt32(Console.ReadLine());

        Console.Write("Nota 1: ");
        nota1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Nota 2: ");
        nota2 = Convert.ToDouble(Console.ReadLine());
    }

    public double CalcularMedia()
    {
        return (nota1 + nota2) / 2;
    }

    public void ApresentarDados()
    {
        Console.WriteLine("Matrícula: " + matricula);
        Console.WriteLine("Nome: " + nome);
        Console.WriteLine("Curso: " + curso);
        Console.WriteLine("Idade: " + idade);
        Console.WriteLine("Nota 1: " + nota1.ToString("F1"));
        Console.WriteLine("Nota 2: " + nota2.ToString("F1"));
        Console.WriteLine("Média: " + CalcularMedia().ToString("F1"));
    }
}