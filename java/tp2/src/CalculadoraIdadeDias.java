import java.util.Scanner;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class CalculadoraIdadeDias {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Entrada da data de nascimento
        System.out.print("Digite o dia de nascimento: ");
        int dia = scanner.nextInt();

        System.out.print("Digite o mês de nascimento: ");
        int mes = scanner.nextInt();

        System.out.print("Digite o ano de nascimento: ");
        int ano = scanner.nextInt();

        // Criação da data de nascimento
        LocalDate dataNascimento = LocalDate.of(ano, mes, dia);

        // Data atual
        LocalDate dataAtual = LocalDate.now();

        // Cálculo da idade em dias
        long idadeEmDias = ChronoUnit.DAYS.between(dataNascimento, dataAtual);

        // Exibição do resultado
        System.out.println("\n===== RESULTADO =====");
        System.out.println("Data de nascimento: " + dataNascimento);
        System.out.println("Data atual: " + dataAtual);
        System.out.println("Sua idade em dias é: " + idadeEmDias + " dias.");

        scanner.close();
    }
}
