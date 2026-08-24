import java.time.LocalDate;

public class Ex07_HelloWorld_Modificado {
    public static void main(String[] args) {
        String meuNome = "Gabriel Sandre";
        LocalDate hoje = LocalDate.now();

        System.out.println("Ola, meu nome e " + meuNome);
        System.out.println("Hoje e " + hoje);
    }
}
