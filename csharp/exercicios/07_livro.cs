internal class Livro
{
    /*            Crie uma classe Livro que represente os dados básicos de um livro, 
     *            além destes, criar um atributo do tipo boolean chamado emprestado.
    Crie métodos emprestar e devolver que altera o atributo emprestado
    Crie um método construtor que receba todos os valores por parâmetros, exceto o atributo
    emprestado que obrigatoriamente deve ser inicializado como false
    Faça a leitura pelo teclado dos atributos para instanciar dois livros*/
    public string titulo;
    public string autor;
    public string isbn;
    public string editora;
    public bool emprestado;

    public Livro(string titulo, string autor, string isbn, string editora)
    {
        this.titulo = titulo;
        this.autor = autor;
        this.isbn = isbn;
        this.editora = editora;
        emprestado = false;
    }

    public void Emprestar()
    {
        if (emprestado)
        {
            Console.WriteLine("Livro já emprestado!");
        }
        else
        {
            emprestado = true;
            Console.WriteLine("Empréstimo realizado com sucesso do livro " + titulo);
        }

    }

    public void Devolver()
    {
        if (!emprestado)//if(emprestado == false)
        {
            Console.WriteLine("O livro já foi devolvido!");
        }
        else
        {
            emprestado = false;
            Console.WriteLine("Devolução realizada com sucesso do livro " + titulo);
        }

    }
    public void ExibirDados()
    {
        Console.WriteLine("Dados do livro: ");
        Console.WriteLine("Título: " + titulo);
        Console.WriteLine("Autor: " + autor);
        Console.WriteLine("ISBN: " + isbn);
        Console.WriteLine("Editora: " + editora);
        if (emprestado)
        {
            Console.WriteLine("Livro em empréstimo");
        }
        else
        {
            Console.WriteLine("Livro disponível para empréstimo");
        }
    }
}