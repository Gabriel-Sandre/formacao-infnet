using System;

class Program
{
    static void Main()
    {
        Console.Write("Título do livro 1: ");
        string t1 = Console.ReadLine();
        Console.Write("Autor do livro 1: ");
        string a1 = Console.ReadLine();
        Console.Write("Ano do livro 1: ");
        int y1 = Convert.ToInt32(Console.ReadLine());

        Console.Write("Título do livro 2: ");
        string t2 = Console.ReadLine();
        Console.Write("Autor do livro 2: ");
        string a2 = Console.ReadLine();
        Console.Write("Ano do livro 2: ");
        int y2 = Convert.ToInt32(Console.ReadLine());

        Livro livro1 = new Livro(t1, a1, y1);
        Livro livro2 = new Livro(t2, a2, y2);

        livro1.Emprestar();

        livro1.ApresentarDados();
        Console.WriteLine();
        livro2.ApresentarDados();
    }
}