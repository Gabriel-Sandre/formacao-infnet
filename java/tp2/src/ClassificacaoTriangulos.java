import java.util.Scanner;

public class ClassificacaoTriangulos {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Entrada dos lados
        System.out.print("Digite o primeiro lado: ");
        double lado1 = scanner.nextDouble();

        System.out.print("Digite o segundo lado: ");
        double lado2 = scanner.nextDouble();

        System.out.print("Digite o terceiro lado: ");
        double lado3 = scanner.nextDouble();

        // Verificação da validade do triângulo
        if (lado1 <= 0 || lado2 <= 0 || lado3 <= 0) {
            System.out.println("\nAs medidas devem ser maiores que zero.");
        } else if (lado1 + lado2 <= lado3 ||
                   lado1 + lado3 <= lado2 ||
                   lado2 + lado3 <= lado1) {

            System.out.println("\nAs medidas não formam um triângulo válido.");

        } else {

            // Classificação do triângulo
            if (lado1 == lado2 && lado2 == lado3) {
                System.out.println("\nO triângulo é equilátero.");

            } else if (lado1 == lado2 ||
                       lado1 == lado3 ||
                       lado2 == lado3) {

                System.out.println("\nO triângulo é isósceles.");

            } else {
                System.out.println("\nO triângulo é escaleno.");
            }
        }

        scanner.close();
    }
}
