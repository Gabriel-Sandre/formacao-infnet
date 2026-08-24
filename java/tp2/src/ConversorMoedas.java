import java.util.Scanner;

public class ConversorMoedas {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Taxas de câmbio pré-definidas
        double taxaDolar = 5.40;
        double taxaEuro = 6.30;
        double taxaLibra = 7.30;

        // Entrada do valor
        System.out.print("Digite o valor em reais (R$): ");
        double valorReais = scanner.nextDouble();
        scanner.nextLine();

        // Entrada da moeda
        System.out.print("Digite a moeda de destino (dolar, euro ou libra): ");
        String moeda = scanner.nextLine().toLowerCase();

        double valorConvertido;

        // Conversão
        switch (moeda) {
            case "dolar":
                valorConvertido = valorReais / taxaDolar;
                System.out.printf("Valor convertido: US$ %.2f%n", valorConvertido);
                break;

            case "euro":
                valorConvertido = valorReais / taxaEuro;
                System.out.printf("Valor convertido: € %.2f%n", valorConvertido);
                break;

            case "libra":
                valorConvertido = valorReais / taxaLibra;
                System.out.printf("Valor convertido: £ %.2f%n", valorConvertido);
                break;

            default:
                System.out.println("Moeda inválida. Escolha dólar, euro ou libra.");
        }

        scanner.close();
    }
}
