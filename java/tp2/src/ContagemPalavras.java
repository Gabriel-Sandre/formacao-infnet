import java.util.Scanner;

public class ContagemPalavras {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Entrada da frase
        System.out.print("Digite uma frase: ");
        String frase = scanner.nextLine();

        // Remove espaços extras no início e no final
        frase = frase.trim();

        // Verifica se a frase está vazia
        if (frase.isEmpty()) {
            System.out.println("A frase não possui palavras.");
        } else {

            // Divide a frase em palavras
            String[] palavras = frase.split("\s+");

            int quantidadePalavras = 0;

            // Percorre as palavras utilizando um laço de repetição
            for (int i = 0; i < palavras.length; i++) {
                quantidadePalavras++;
            }

            // Exibe o resultado
            System.out.println("\n===== RESULTADO =====");
            System.out.println("Frase: " + frase);
            System.out.println("Quantidade de palavras: " + quantidadePalavras);
        }

        scanner.close();
    }
}
