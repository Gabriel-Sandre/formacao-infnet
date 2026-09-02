# C#

## Exercícios de aula

Prática que antecedeu a disciplina formal: primeiro variáveis e operadores, depois
controle de fluxo, e então a passagem para orientação a objetos.

| Arquivo | Conteúdo |
|---|---|
| `exercicios/01_operacoes_basicas.cs` | variáveis, tipos numéricos e operações aritméticas |
| `exercicios/02_estruturas_controle.cs` | condicionais |
| `exercicios/03_repeticao.cs` | laços |
| `exercicios/04_classes_pessoa.cs` | primeira classe e instanciação de objeto |
| `exercicios/05_conta_bancaria.cs` | encapsulamento com campos privados e métodos |
| `exercicios/06_aluno.cs` | classe com matrícula, nome e notas |
| `exercicios/07_livro.cs` | classe com propriedades e comportamento |

## TP2 — Fundamentos de Desenvolvimento com C#

Doze programas organizados em quatro partes do enunciado, entregue em 02/09/2026:

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

O arquivo `TP2-c#/build_report.py` segue o mesmo modelo do `java/tp2/build_report.py`:
lê os `.cs` da pasta `src/`, junta com os enunciados e os prints de execução em
`screenshots/` e gera o PDF final. O enunciado original também está arquivado em
`TP2-c#/TP2_Fundamentos_de_Desenvolvimento_com_C#.pdf`.

### Alguns pontos que valeram estudo

**Aniversário em 29 de fevereiro** (`DiasProximoAniversario`) — criar
`new DateTime(ano, 2, 29)` direto quebra com `ArgumentOutOfRangeException` em
qualquer ano que não seja bissexto. A correção usa `DateTime.IsLeapYear(ano)`
para decidir entre o dia 29 e o dia 28 antes de montar a data.

**Alíquota sobre o salário inteiro** (`CalculadoraSalarioLiquido`) — aplicar a
taxa da faixa sobre o valor total, em vez de só sobre a fatia que cai nela, cria
um "penhasco": um salário de R$ 3000,00 rende R$ 2700,00 líquidos, mas
R$ 3000,01 rende só R$ 2550,01 — um centavo a mais de bruto derruba o líquido em
R$ 150. É o mesmo problema já visto na `CalculadoraImpostoRenda` em Java;
mantido assim aqui porque o enunciado não pede explicitamente uma faixa
progressiva.

**Separador decimal e cultura do Windows** (`ConversorTemperatura`) —
`double.Parse` sem configuração de cultura usa o padrão pt-BR, que trata `.`
como separador de milhar. Digitar `36.5` não dá erro, mas é lido como `365`,
silenciosamente. Mantido assim por decisão, já que o enunciado só pede vírgula
como separador decimal (padrão brasileiro).

**Empréstimo de dias entre meses de tamanhos diferentes** (`CalculoIdadePrecisa`,
`DiferencaEntreDatas`) — o algoritmo de pegar emprestado dias do mês anterior
funciona corretamente no caso geral (inclusive atravessando anos e anos
bissextos), mas tem um caso extremo conhecido: nascimento no dia 31 caindo num
mês vizinho com menos de 31 dias. Não é exigido pelo enunciado, só uma
curiosidade de quem também usa esse algoritmo em bibliotecas profissionais.

## Executando

```bash
dotnet run
```

Os arquivos de `exercicios/` e `TP2-c#/src/` foram extraídos de projetos de
console separados. Para rodar um deles isoladamente, crie um projeto novo e
substitua o `Program.cs`:

```bash
dotnet new console -o teste
```
