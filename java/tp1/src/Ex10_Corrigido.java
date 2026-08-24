public class Ex10_Corrigido {
    public static void main(String[] args) {
        int idade = 25;
        double salario = 3500.50;
        String nome = "SEU NOME AQUI";

        int idadeEmMeses = calcularIdadeEmMeses(idade);
        double salarioComBonus = calcularBonus(salario);

        System.out.println("Nome: " + nome);
        System.out.println("Idade em meses: " + idadeEmMeses);
        System.out.println("Salario com bonus: " + salarioComBonus);
    }

    static int calcularIdadeEmMeses(int idade) {
        return idade * 12;
    }

    static double calcularBonus(double salario) {
        return salario * 1.1;
    }
}
