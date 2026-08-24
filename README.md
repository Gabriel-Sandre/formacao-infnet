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
csharp/   Exercícios de aula (a disciplina formal começa no próximo bloco)
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

---

**Gabriel Alves Sandre da Silva** — Instituto Infnet
