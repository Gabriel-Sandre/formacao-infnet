import java.util.Scanner;

public class CalculadoraImpostoRenda {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite seu salário bruto anual: R$ ");
        double salarioBruto = scanner.nextDouble();

        double imposto;

        if (salarioBruto <= 30000) {
            imposto = 0;

        } else if (salarioBruto <= 50000) {
            imposto = (salarioBruto - 30000) * 0.10;

        } else if (salarioBruto <= 80000) {
            imposto = (20000 * 0.10)
                    + (salarioBruto - 50000) * 0.20;

        } else {
            imposto = (20000 * 0.10)
                    + (30000 * 0.20)
                    + (salarioBruto - 80000) * 0.30;
        }

        double salarioLiquido = salarioBruto - imposto;

        System.out.println("\n===== RESULTADO =====");
        System.out.printf("Salário bruto anual: R$ %.2f%n", salarioBruto);
        System.out.printf("Imposto a pagar: R$ %.2f%n", imposto);
        System.out.printf("Salário líquido anual: R$ %.2f%n", salarioLiquido);

        scanner.close();
    }
}
