import java.util.Scanner;

public class ValidadorSenha {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Cadastro da senha
        System.out.print("Cadastre sua senha: ");
        String senhaCadastrada = scanner.nextLine();

        // Solicita a senha até acertar
        String senhaDigitada;

        do {
            System.out.print("Digite sua senha novamente: ");
            senhaDigitada = scanner.nextLine();

            if (!senhaDigitada.equals(senhaCadastrada)) {
                System.out.println("Senha incorreta! Tente novamente.");
            }

        } while (!senhaDigitada.equals(senhaCadastrada));

        // Mensagem de sucesso
        System.out.println("\nSenha correta!");
        System.out.println("Acesso realizado com sucesso.");

        scanner.close();
    }
}
