using System;

class Program
{
    static void Main()
    {
        Random random = new Random();

        int numeroSecreto = random.Next(1, 101);
        int palpite = 0;
        int tentativas = 0;

        Console.WriteLine("===== JOGO DE ADIVINHAÇÃO =====");
        Console.WriteLine("Tente adivinhar um número entre 1 e 100!");

        while (palpite != numeroSecreto)
        {
            Console.Write("Digite seu palpite: ");
            palpite = int.Parse(Console.ReadLine());

            tentativas++;

            if (palpite < numeroSecreto)
            {
                Console.WriteLine("O número secreto é maior!");
            }
            else if (palpite > numeroSecreto)
            {
                Console.WriteLine("O número secreto é menor!");
            }
            else
            {
                Console.WriteLine();
                Console.WriteLine("Parabéns! Você acertou!");
                Console.WriteLine($"Número de tentativas: {tentativas}");
            }
        }
    }
}
