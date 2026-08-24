import java.util.Scanner;
import java.util.Random;

public class JogoAdivinhacao {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        // Gera um número aleatório entre 1 e 100
        int numeroSecreto = random.nextInt(100) + 1;

        int palpite;

        System.out.println("===== JOGO DE ADIVINHAÇÃO =====");
        System.out.println("Tente adivinhar o número entre 1 e 100!");

        // Laço de repetição
        do {
            System.out.print("Digite seu palpite: ");
            palpite = scanner.nextInt();

            if (palpite < numeroSecreto) {
                System.out.println("O número secreto é MAIOR. Tente novamente!");

            } else if (palpite > numeroSecreto) {
                System.out.println("O número secreto é MENOR. Tente novamente!");

            } else {
                System.out.println("\nParabéns! Você acertou!");
                System.out.println("O número secreto era: " + numeroSecreto);
            }

        } while (palpite != numeroSecreto);

        scanner.close();
    }
}
