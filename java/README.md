# Java — Fundamentos de Desenvolvimento

## TP1 — Ambiente e primeiros programas

Instalação do JDK e da IntelliJ IDEA, criação do primeiro projeto, uso de
variáveis e tipos, leitura de entrada com `Scanner` e um exercício de
depuração: três erros introduzidos de propósito, identificados e corrigidos a
partir das mensagens do compilador.

Os arquivos em `tp1/src/` seguem a numeração dos exercícios do roteiro.

## TP2 — Entrada, controle de fluxo e repetição

Doze programas organizados nas três partes do enunciado:

- **Parte 1 (ex. 1–4)** — entrada de dados com `Scanner`
- **Parte 2 (ex. 5–8)** — estruturas condicionais
- **Parte 3 (ex. 9–12)** — estruturas de repetição

Cada classe fica em seu próprio arquivo, com o nome exigido pelo compilador, e
tem um método `main` independente.

### Alguns pontos que valeram estudo

**Ano bissexto** (`VerificadorAnoBissexto`) — a regra completa tem três
camadas, não uma. Divisível por 4 é bissexto, exceto se for divisível por 100,
a menos que também seja por 400. Testar só com 2024 esconde o erro; 1900 e 2000
são os casos que revelam.

**Imposto progressivo** (`CalculadoraImpostoRenda`) — cada faixa tributa apenas
a parcela da renda que cai dentro dela, somada ao que já foi cobrado nas faixas
anteriores. Aplicar a alíquota sobre o salário inteiro criaria a distorção de
alguém ganhar mais e receber menos ao cruzar a fronteira de uma faixa.

**Comparação de String** (`ValidadorSenha`) — `==` compara referências, não
conteúdo. Com texto vindo do `Scanner`, o `==` falha mesmo quando a senha está
correta. A comparação precisa ser feita com `.equals()`.

**Validade antes da classificação** (`ClassificacaoTriangulos`) — a verificação
da desigualdade triangular precisa das três combinações de lados, e o caso
equilátero tem que ser testado antes do isósceles, já que um triângulo
equilátero também satisfaz a condição de ter dois lados iguais.

## Executando

```bash
cd tp2/src
javac -encoding UTF-8 VerificadorAnoBissexto.java
java VerificadorAnoBissexto
```

A flag `-encoding UTF-8` evita que os acentos das mensagens saiam corrompidos
no console do Windows.
