import java.util.Scanner;

public class SequenciaNumerica {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o valor inicial: ");
        int valorInicial = scanner.nextInt();

        System.out.print("Digite o incremento: ");
        int incremento = scanner.nextInt();

        System.out.println("\n===== SEQUÊNCIA NUMÉRICA =====");

        int numero = valorInicial;

        while (numero <= 100) {
            System.out.print(numero);

            // Verifica se o próximo número ainda estará dentro do limite
            if (numero + incremento <= 100) {
                System.out.print(", ");
            }

            numero += incremento;
        }

        System.out.println();

        scanner.close();
    }
}
