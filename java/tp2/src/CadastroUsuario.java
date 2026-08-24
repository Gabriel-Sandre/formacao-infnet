import java.util.Scanner;

public class CadastroUsuario {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Entrada de dados
        System.out.print("Digite seu nome completo: ");
        String nome = scanner.nextLine();

        System.out.print("Digite sua idade: ");
        int idade = scanner.nextInt();
        scanner.nextLine(); // Limpa o buffer

        System.out.print("Digite o nome da sua mãe: ");
        String nomeMae = scanner.nextLine();

        System.out.print("Digite o nome do seu pai: ");
        String nomePai = scanner.nextLine();

        // Exibição das informações
        System.out.println("\n===== CADASTRO DO USUÁRIO =====");
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("Nome da mãe: " + nomeMae);
        System.out.println("Nome do pai: " + nomePai);

        // Comparação dos tamanhos
        System.out.println("\n===== COMPARAÇÃO DOS NOMES =====");

        if (nome.length() > nomeMae.length()) {
            System.out.println("Seu nome tem mais letras que o nome da sua mãe.");
        } else if (nome.length() < nomeMae.length()) {
            System.out.println("O nome da sua mãe tem mais letras que o seu.");
        } else {
            System.out.println("Seu nome e o nome da sua mãe possuem o mesmo tamanho.");
        }

        if (nome.length() > nomePai.length()) {
            System.out.println("Seu nome tem mais letras que o nome do seu pai.");
        } else if (nome.length() < nomePai.length()) {
            System.out.println("O nome do seu pai tem mais letras que o seu.");
        } else {
            System.out.println("Seu nome e o nome do seu pai possuem o mesmo tamanho.");
        }

        scanner.close();
    }
}
