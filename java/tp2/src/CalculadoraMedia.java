import java.util.Scanner;

public class CalculadoraMedia {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Entrada das quatro notas
        System.out.print("Digite a primeira nota: ");
        double nota1 = scanner.nextDouble();

        System.out.print("Digite a segunda nota: ");
        double nota2 = scanner.nextDouble();

        System.out.print("Digite a terceira nota: ");
        double nota3 = scanner.nextDouble();

        System.out.print("Digite a quarta nota: ");
        double nota4 = scanner.nextDouble();

        // Cálculo da média
        double media = (nota1 + nota2 + nota3 + nota4) / 4;

        // Exibição da média
        System.out.println("\n===== RESULTADO =====");
        System.out.printf("Média final: %.2f%n", media);

        // Verificação da situação
        if (media >= 7) {
            System.out.println("Parabéns! Você foi aprovado.");
        } else if (media >= 5) {
            System.out.println("Você está em recuperação.");
        } else {
            System.out.println("Você foi reprovado.");
        }

        scanner.close();
    }
}
