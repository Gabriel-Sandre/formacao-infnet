# C#

Exercícios de aula. A disciplina formal de C# entra no próximo bloco do curso,
então aqui ainda não há trabalhos práticos entregues — o que está registrado é
a prática que antecede isso.

## Exercícios

| Arquivo | Conteúdo |
|---|---|
| `01_operacoes_basicas.cs` | variáveis, tipos numéricos e operações aritméticas |
| `02_estruturas_controle.cs` | condicionais |
| `03_repeticao.cs` | laços |
| `04_classes_pessoa.cs` | primeira classe e instanciação de objeto |
| `05_conta_bancaria.cs` | encapsulamento com campos privados e métodos |
| `06_aluno.cs` | classe com matrícula, nome e notas |
| `07_livro.cs` | classe com propriedades e comportamento |

A progressão acompanha a do bloco de Java: primeiro variáveis e operadores,
depois controle de fluxo, e então a passagem para orientação a objetos — que é
onde o C# começa a se diferenciar do que eu vinha escrevendo em Java.

## Executando

```bash
dotnet run
```

Os arquivos foram extraídos de projetos de console separados. Para rodar um
deles isoladamente, crie um projeto novo e substitua o `Program.cs`:

```bash
dotnet new console -o teste
```
