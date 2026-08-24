import java.util.Scanner;

public class VerificadorAnoBissexto {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Entrada do ano
        System.out.print("Digite um ano: ");
        int ano = scanner.nextInt();

        // Verificação do ano bissexto
        if ((ano % 400 == 0) || (ano % 4 == 0 && ano % 100 != 0)) {
            System.out.println("O ano " + ano + " é bissexto.");
        } else {
            System.out.println("O ano " + ano + " não é bissexto.");
        }

        scanner.close();
    }
}
