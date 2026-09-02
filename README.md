# Formação em Desenvolvimento — Instituto Infnet

Trabalhos práticos e exercícios da minha graduação em Tecnologia da Informação,
organizados por linguagem. O objetivo deste repositório é registrar a evolução:
do primeiro `Hello, World!` até programas com lógica de negócio e validação de
entrada.

Cada trabalho traz o **código-fonte** e o **relatório em PDF** entregue, com
enunciado e evidência de execução.

## Estrutura

```
java/     Fundamentos de Desenvolvimento com Java
  tp1/    Ambiente, primeiro projeto, variáveis, entrada de dados e depuração
  tp2/    Entrada do usuário, controle de fluxo e estruturas de repetição
csharp/   Fundamentos de Desenvolvimento com C#
  exercicios/  Prática de aula que antecedeu a disciplina formal
  TP2-c#/      Datas, entrada de dados, controle de fluxo e repetição
```

## Java — TP2 em detalhe

O TP2 reúne 12 programas, divididos em três frentes:

| # | Programa | O que exercita |
|---|---|---|
| 01 | `CadastroUsuario` | `Scanner`, comparação de `String` |
| 02 | `CalculadoraMedia` | média aritmética, `if / else if` encadeado |
| 03 | `ConversorMoedas` | `switch` sobre `String`, formatação com `printf` |
| 04 | `CalculadoraIdadeDias` | `LocalDate` e `ChronoUnit`, anos bissextos |
| 05 | `CalculadoraDescontos` | faixas de desconto por valor |
| 06 | `VerificadorAnoBissexto` | operadores lógicos e a regra dos séculos |
| 07 | `CalculadoraImpostoRenda` | imposto progressivo por faixa |
| 08 | `ClassificacaoTriangulos` | condicionais aninhadas, desigualdade triangular |
| 09 | `ValidadorSenha` | `do/while`, comparação com `.equals()` |
| 10 | `JogoAdivinhacao` | `Random`, laço com condição de saída |
| 11 | `SequenciaNumerica` | `while` e formatação de saída |
| 12 | `ContagemPalavras` | `split()` com expressão regular, `array` |

O arquivo `java/tp2/build_report.py` é um script que escrevi para montar o PDF
do relatório automaticamente: ele lê os `.java` da pasta `src/`, junta com os
enunciados e os prints de execução e gera o documento final. Assim o relatório
nunca fica dessincronizado do código.

## Como executar

Os programas Java são independentes e usam apenas a biblioteca padrão:

```bash
cd java/tp2/src
javac -encoding UTF-8 CalculadoraMedia.java
java CalculadoraMedia
```

Todos leem dados do teclado via `Scanner`.

## C# — TP2 em detalhe

O TP2 também reúne 12 programas, agora em quatro frentes:

| # | Programa | O que exercita |
|---|---|---|
| 01 | `CalculoIdadePrecisa` | `DateTime`, empréstimo de dias entre meses |
| 02 | `DiasProximoAniversario` | `DateTime`, ano bissexto na comparação de datas |
| 03 | `DiferencaEntreDatas` | `DateTime` e `TimeSpan`, normalização de ordem das datas |
| 04 | `FormularioCadastroSimples` | `Console.ReadLine()`, formatação de saída |
| 05 | `ConversorTemperatura` | fórmulas de conversão, `:F2` |
| 06 | `CalculoIMC` | faixas de classificação com `if / else if` encadeado |
| 07 | `VerificadorParImpar` | operador `%`, números negativos |
| 08 | `ClassificacaoNotaEscolar` | faixas de nota, validação de entrada |
| 09 | `CalculadoraSalarioLiquido` | faixas de imposto sobre o valor total |
| 10 | `ContagemRegressiva` | `for` decrescente, formatação de lista |
| 11 | `TabuadaInterativa` | `for`, interpolação de string |
| 12 | `JogoAdivinhacao` | `while`, `Random`, contagem de tentativas |

O arquivo `csharp/TP2-c#/build_report.py` segue o mesmo modelo do de Java: lê os
`.cs` da pasta `src/`, junta com os enunciados e os prints de execução em
`screenshots/` e gera o PDF final.

## Como executar (C#)

```bash
cd csharp/TP2-c#/src
dotnet new console -o teste
# substitua o Program.cs gerado pelo arquivo que quer rodar
cd teste
dotnet run
```

---

**Gabriel Alves Sandre da Silva** — Instituto Infnet
