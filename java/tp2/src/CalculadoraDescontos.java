import java.util.Scanner;

public class CalculadoraDescontos {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Entrada do valor da compra
        System.out.print("Digite o valor da compra: R$ ");
        double valorCompra = scanner.nextDouble();

        double percentualDesconto;
        double valorDesconto;
        double valorFinal;

        // Verificação do desconto
        if (valorCompra > 1000) {
            percentualDesconto = 0.10;
        } else if (valorCompra >= 500) {
            percentualDesconto = 0.05;
        } else {
            percentualDesconto = 0.0;
        }

        // Cálculo do desconto e do valor final
        valorDesconto = valorCompra * percentualDesconto;
        valorFinal = valorCompra - valorDesconto;

        // Exibição dos resultados
        System.out.println("\n===== RESUMO DA COMPRA =====");
        System.out.printf("Valor original: R$ %.2f%n", valorCompra);
        System.out.printf("Desconto aplicado: R$ %.2f%n", valorDesconto);
        System.out.printf("Percentual de desconto: %.0f%%%n", percentualDesconto * 100);
        System.out.printf("Valor final: R$ %.2f%n", valorFinal);

        scanner.close();
    }
}
