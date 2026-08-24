# -*- coding: utf-8 -*-
"""Gera o PDF do TP2 de Java a partir dos fontes em ../src e dos prints em ./screenshots."""
import io
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Preformatted
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader, PdfWriter

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "..", "src")
SCREENSHOTS = os.path.join(BASE, "screenshots")

ALUNO = "Gabriel Alves Sandre da Silva"
DISCIPLINA = "Fundamentos de Desenvolvimento com Java"
TRABALHO = "TP-2"
DATA_ENTREGA = "24/08/2026"
LOGO = os.path.join(BASE, "capa_logo.png")
SAIDA = "Gabriel_Sandre_DR1_TP2.PDF"

# Fontes TrueType embutidas: garantem acentuacao correta no PDF (as fontes
# padrao do PDF usam uma tabela de caracteres limitada).
FONTS = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont("Corpo", os.path.join(FONTS, "arial.ttf")))
pdfmetrics.registerFont(TTFont("Corpo-Bold", os.path.join(FONTS, "arialbd.ttf")))
pdfmetrics.registerFont(TTFont("Mono", os.path.join(FONTS, "consola.ttf")))
pdfmetrics.registerFontFamily("Corpo", normal="Corpo", bold="Corpo-Bold",
                              italic="Corpo", boldItalic="Corpo-Bold")

# ---------------------------------------------------------------- estilos
styles = getSampleStyleSheet()
title_style = ParagraphStyle("TitleCustom", parent=styles["Heading1"], fontSize=18,
                             textColor=HexColor("#112639"), spaceAfter=14,
                             alignment=TA_CENTER, fontName="Corpo-Bold")
h2 = ParagraphStyle("H2Custom", parent=styles["Heading2"], fontSize=14,
                    textColor=HexColor("#112639"), spaceBefore=16, spaceAfter=8,
                    fontName="Corpo-Bold")
h3 = ParagraphStyle("H3Custom", parent=styles["Heading3"], fontSize=11.5,
                    textColor=HexColor("#1B4F72"), spaceBefore=10, spaceAfter=4,
                    fontName="Corpo-Bold")
body = ParagraphStyle("BodyCustom", parent=styles["Normal"], fontSize=10.5,
                      leading=15, alignment=TA_JUSTIFY, spaceAfter=8,
                      fontName="Corpo")
bullet = ParagraphStyle("BulletCustom", parent=body, leftIndent=14, bulletIndent=4,
                        spaceAfter=3)
caption = ParagraphStyle("Caption", parent=styles["Normal"], fontSize=9,
                         textColor=HexColor("#555555"), spaceBefore=4, spaceAfter=12,
                         fontName="Corpo")
code_style = ParagraphStyle("Code", parent=styles["Code"], fontSize=8.3, leading=10.5,
                            backColor=HexColor("#F4F4F4"), borderPadding=6,
                            fontName="Mono")
pendente = ParagraphStyle("Pendente", parent=styles["Normal"], fontSize=9.5,
                          textColor=HexColor("#B03A2E"), alignment=TA_CENTER,
                          backColor=HexColor("#FDEDEC"), borderPadding=10,
                          spaceBefore=6, spaceAfter=12, fontName="Corpo")
capa_nome = ParagraphStyle("CapaNome", parent=styles["Normal"], fontSize=13,
                           alignment=TA_CENTER, spaceAfter=6, fontName="Corpo")
capa_sub = ParagraphStyle("CapaSub", parent=styles["Normal"], fontSize=11,
                          alignment=TA_CENTER, textColor=HexColor("#555555"),
                          spaceAfter=4, fontName="Corpo")
parte_style = ParagraphStyle("Parte", parent=styles["Normal"], fontSize=10,
                             textColor=HexColor("#FFFFFF"), alignment=TA_CENTER,
                             backColor=HexColor("#1B4F72"), borderPadding=7,
                             spaceBefore=0, spaceAfter=14, fontName="Corpo-Bold")

PAGE_W, PAGE_H = A4
MAX_IMG_W = PAGE_W - 4 * cm


# ---------------------------------------------------------------- helpers
def ler_codigo(arquivo):
    caminho = os.path.join(SRC, arquivo)
    with io.open(caminho, encoding="utf-8") as fh:
        return fh.read().rstrip()


def bloco_codigo(arquivo):
    return Preformatted(ler_codigo(arquivo), code_style)


def imagem_ajustada(nome, max_w=MAX_IMG_W, max_h=17 * cm):
    caminho = os.path.join(SCREENSHOTS, nome)
    ir = ImageReader(caminho)
    iw, ih = ir.getSize()
    escala = min(max_w / iw, max_h / ih, 1.0)
    return Image(caminho, width=iw * escala, height=ih * escala)


# Prints reprovados na conferencia: nao entram no PDF ate serem refeitos.
BLOQUEADOS = {}


def evidencia(num):
    """Print da execucao, se existir; senao um aviso visivel de pendencia."""
    if num in BLOQUEADOS:
        return [Paragraph("[ PENDENTE: %s ]" % BLOQUEADOS[num], pendente)], False
    for base in ("ex%d" % num, "ex%02d" % num):
        for ext in (".png", ".jpg", ".jpeg"):
            nome = base + ext
            if os.path.exists(os.path.join(SCREENSHOTS, nome)):
                return [imagem_ajustada(nome),
                        Paragraph("Execu\u00e7\u00e3o do Exerc\u00edcio %d." % num, caption)], True
    return [Paragraph("[ PENDENTE: inserir o print da execu\u00e7\u00e3o como "
                      "<b>screenshots/ex%d.png</b> ]" % num, pendente)], False


def gerar_capa(caminho):
    """Redesenha a capa institucional com os dados deste trabalho.

    A capa do TP1 nao serve como base: naquele arquivo o "TP-1", o nome e a
    data estao convertidos em curvas (nao sao texto), entao nao ha o que
    substituir. Aqui tudo e texto de verdade.
    """
    from reportlab.pdfgen import canvas as _canvas

    AZUL_FUNDO = HexColor("#EAF2FB")
    BRANCO = HexColor("#FFFFFF")
    TINTA = HexColor("#1A1A1A")

    c = _canvas.Canvas(caminho, pagesize=A4)
    larg, alt = A4

    c.setFillColor(AZUL_FUNDO)
    c.rect(0, 0, larg, alt, stroke=0, fill=1)

    # faixa branca horizontal atras do bloco de identificacao
    c.setFillColor(BRANCO)
    c.rect(0, alt - 400, larg, 165, stroke=0, fill=1)

    def caixa_texto(texto, y, fonte, tamanho, altura=34, largura=None,
                    centralizado=True):
        c.setFont(fonte, tamanho)
        largura = largura or (c.stringWidth(texto, fonte, tamanho) + 60)
        x = (larg - largura) / 2.0
        c.setFillColor(BRANCO)
        c.rect(x, y, largura, altura, stroke=0, fill=1)
        c.setFillColor(TINTA)
        if centralizado:
            c.drawCentredString(larg / 2.0, y + altura / 2.0 - tamanho * 0.35, texto)
        else:
            c.drawString(x + 22, y + altura / 2.0 - tamanho * 0.35, texto)

    caixa_texto(DISCIPLINA, alt - 118, "Corpo-Bold", 12)

    c.setFillColor(TINTA)
    c.setFont("Corpo-Bold", 12)
    c.drawCentredString(larg / 2.0, alt - 330, "Aluno: %s" % ALUNO)
    c.setFont("Corpo", 10)
    c.drawCentredString(larg / 2.0, alt - 360, DATA_ENTREGA)

    caixa_texto(TRABALHO, alt - 470, "Corpo", 20, altura=44,
                largura=larg * 0.62, centralizado=False)

    if os.path.exists(LOGO):
        ir = ImageReader(LOGO)
        iw, ih = ir.getSize()
        destino_w = larg * 0.42
        destino_h = ih * (destino_w / iw)
        c.drawImage(ir, (larg - destino_w) / 2.0, alt - 470 - destino_h - 30,
                    width=destino_w, height=destino_h, mask="auto")

    c.showPage()
    c.save()
    return caminho


# ---------------------------------------------------------------- conteudo
PARTES = {
    1: "Parte 1 \u2014 Programas que utilizam entrada do usu\u00e1rio",
    5: "Parte 2 \u2014 C\u00f3digos usando elementos de controle de fluxo",
    9: "Parte 3 \u2014 C\u00f3digos usando instru\u00e7\u00f5es de repeti\u00e7\u00e3o",
}

EXERCICIOS = [
    dict(n=1, titulo="Cadastro de Usu\u00e1rio Completo", arquivo="CadastroUsuario.java",
         enunciado="Crie um programa em Java que solicite ao usu\u00e1rio seu nome completo, idade, "
                   "nome da m\u00e3e e nome do pai. O programa deve exibir as informa\u00e7\u00f5es de forma "
                   "organizada e verificar se o nome do usu\u00e1rio tem mais letras que o nome da "
                   "m\u00e3e ou do pai.",
         obs=["Utilize a classe Scanner para capturar todas as entradas do usu\u00e1rio.",
              "Compare os tamanhos das strings para determinar o nome mais longo."]),

    dict(n=2, titulo="Calculadora de M\u00e9dia de Notas", arquivo="CalculadoraMedia.java",
         enunciado="Desenvolva um programa que solicite ao usu\u00e1rio quatro notas bimestrais. O "
                   "programa deve calcular a m\u00e9dia e informar se o usu\u00e1rio foi aprovado "
                   "(m\u00e9dia &gt;= 7), est\u00e1 em recupera\u00e7\u00e3o (m\u00e9dia entre 5 e 6.9) ou foi reprovado "
                   "(m\u00e9dia &lt; 5).",
         obs=["Utilize a classe Scanner para entrada de dados.",
              "Realize o c\u00e1lculo da m\u00e9dia aritm\u00e9tica.",
              "Exiba uma mensagem personalizada com o resultado."]),

    dict(n=3, titulo="Conversor de Moedas", arquivo="ConversorMoedas.java",
         enunciado="Crie um programa que pe\u00e7a ao usu\u00e1rio um valor em reais e uma moeda de destino "
                   "(d\u00f3lar, euro ou libra). O programa deve converter o valor informado na moeda "
                   "escolhida com base em taxas de c\u00e2mbio pr\u00e9-definidas no c\u00f3digo.",
         obs=["Utilize a classe Scanner para capturar o valor e a moeda de destino.",
              "Defina as taxas de c\u00e2mbio diretamente no c\u00f3digo.",
              "Exiba o valor convertido com duas casas decimais."]),

    dict(n=4, titulo="Calculadora de Idade em Dias", arquivo="CalculadoraIdadeDias.java",
         enunciado="Escreva um programa que solicite a data de nascimento do usu\u00e1rio (dia, m\u00eas e "
                   "ano) e calcule sua idade em dias.",
         obs=["Utilize a classe Scanner para capturar a data de nascimento.",
              "Considere anos bissextos no c\u00e1lculo.",
              "Exiba a idade total em dias."]),

    dict(n=5, titulo="Calculadora de Descontos Progressivos", arquivo="CalculadoraDescontos.java",
         enunciado="Crie um programa que solicite o valor de uma compra e calcule o desconto "
                   "aplic\u00e1vel com base no valor total. Se o valor for maior que R$ 1000, aplique "
                   "um desconto de 10%; entre R$ 500 e R$ 1000, aplique 5%; abaixo de R$ 500, n\u00e3o "
                   "h\u00e1 desconto.",
         obs=["Utilize estruturas condicionais para verificar o valor e aplicar o desconto.",
              "Exiba o valor original, o desconto aplicado e o valor final."]),

    dict(n=6, titulo="Verificador de Ano Bissexto", arquivo="VerificadorAnoBissexto.java",
         enunciado="Desenvolva um programa que pe\u00e7a um ano ao usu\u00e1rio e verifique se ele \u00e9 "
                   "bissexto.",
         obs=["Utilize estruturas condicionais para verificar as condi\u00e7\u00f5es de ano bissexto.",
              "Exiba uma mensagem indicando se o ano \u00e9 ou n\u00e3o bissexto."]),

    dict(n=7, titulo="Calculadora de Imposto de Renda", arquivo="CalculadoraImpostoRenda.java",
         enunciado="Crie um programa que solicite ao usu\u00e1rio seu sal\u00e1rio bruto anual e calcule o "
                   "imposto de renda a pagar com base em al\u00edquotas definidas no c\u00f3digo. Utilize "
                   "faixas de renda progressivas para calcular o imposto.",
         obs=["Utilize estruturas condicionais para aplicar as al\u00edquotas.",
              "Exiba o valor do imposto a pagar e o sal\u00e1rio l\u00edquido."]),

    dict(n=8, titulo="Classifica\u00e7\u00e3o de Tri\u00e2ngulos", arquivo="ClassificacaoTriangulos.java",
         enunciado="Escreva um programa que solicite ao usu\u00e1rio os comprimentos de tr\u00eas lados de "
                   "um tri\u00e2ngulo e determine se ele \u00e9 equil\u00e1tero, is\u00f3sceles ou escaleno.",
         obs=["Utilize estruturas condicionais para verificar os tipos de tri\u00e2ngulo.",
              "Verifique tamb\u00e9m se as medidas formam um tri\u00e2ngulo v\u00e1lido."]),

    dict(n=9, titulo="Validador de Senha", arquivo="ValidadorSenha.java",
         enunciado="Crie um programa que solicite ao usu\u00e1rio que cadastre uma senha e, em "
                   "seguida, pe\u00e7a a senha novamente at\u00e9 que seja digitada corretamente.",
         obs=["Utilize um la\u00e7o de repeti\u00e7\u00e3o para solicitar a senha at\u00e9 que esteja correta.",
              "Exiba uma mensagem de sucesso ao final."]),

    dict(n=10, titulo="Jogo de Adivinha\u00e7\u00e3o", arquivo="JogoAdivinhacao.java",
         enunciado="Desenvolva um jogo de adivinha\u00e7\u00e3o em que o usu\u00e1rio deve descobrir um n\u00famero "
                   "gerado aleatoriamente pelo programa (entre 1 e 100). O programa deve informar "
                   "se o palpite \u00e9 maior ou menor que o n\u00famero sorteado at\u00e9 que o usu\u00e1rio acerte.",
         obs=["Utilize um la\u00e7o de repeti\u00e7\u00e3o para permitir m\u00faltiplos palpites.",
              "Utilize a classe Random para gerar o n\u00famero secreto."]),

    dict(n=11, titulo="Sequ\u00eancia Num\u00e9rica Personalizada", arquivo="SequenciaNumerica.java",
         enunciado="Escreva um programa que solicite dois n\u00fameros ao usu\u00e1rio: um valor inicial e "
                   "um incremento. O programa deve exibir uma sequ\u00eancia num\u00e9rica a partir do "
                   "valor inicial, aumentando de acordo com o incremento at\u00e9 ultrapassar 100.",
         obs=["Utilize um la\u00e7o de repeti\u00e7\u00e3o para gerar a sequ\u00eancia.",
              "Exiba os n\u00fameros separados por v\u00edrgulas."]),

    dict(n=12, titulo="Contagem de Palavras", arquivo="ContagemPalavras.java",
         enunciado="Crie um programa que solicite ao usu\u00e1rio uma frase e conte quantas palavras a "
                   "frase cont\u00e9m.",
         obs=["Utilize um la\u00e7o de repeti\u00e7\u00e3o para percorrer a frase.",
              "Utilize o m\u00e9todo split() para separar as palavras."]),
]

# ---------------------------------------------------------------- montagem
story = []
faltando = []

story.append(Spacer(1, 5 * cm))
story.append(Paragraph("Trabalho Pr\u00e1tico 2", title_style))
story.append(Paragraph(DISCIPLINA, capa_sub))
story.append(Spacer(1, 3 * cm))
story.append(Paragraph("<b>Aluno:</b> %s" % ALUNO, capa_nome))
story.append(Paragraph("Instituto Infnet", capa_sub))
story.append(PageBreak())

for ex in EXERCICIOS:
    # A faixa da Parte abre a pagina do primeiro exercicio dela, em vez de
    # ocupar uma pagina propria quase vazia.
    if ex["n"] in PARTES:
        story.append(Paragraph(PARTES[ex["n"]], parte_style))

    story.append(Paragraph("Exerc\u00edcio %d \u2014 %s" % (ex["n"], ex["titulo"]), h2))
    story.append(Paragraph("<b>Enunciado</b>", h3))
    story.append(Paragraph(ex["enunciado"], body))
    story.append(Paragraph("<b>Observa\u00e7\u00f5es</b>", h3))
    for o in ex["obs"]:
        story.append(Paragraph(o, bullet, bulletText="\u2022"))

    story.append(Paragraph("<b>C\u00f3digo-fonte</b> (%s)" % ex["arquivo"], h3))
    story.append(bloco_codigo(ex["arquivo"]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>Execu\u00e7\u00e3o</b>", h3))
    flow, ok = evidencia(ex["n"])
    story.extend(flow)
    if not ok:
        faltando.append(ex["n"])

    story.append(PageBreak())

corpo = os.path.join(BASE, "_corpo.pdf")
doc = SimpleDocTemplate(corpo, pagesize=A4,
                        leftMargin=2 * cm, rightMargin=2 * cm,
                        topMargin=2 * cm, bottomMargin=2 * cm,
                        title="%s - TP2" % DISCIPLINA, author=ALUNO)
doc.build(story)

capa_gerada = gerar_capa(os.path.join(BASE, "_capa_tp2.pdf"))

writer = PdfWriter()
writer.add_page(PdfReader(capa_gerada).pages[0])
for p in PdfReader(corpo).pages:
    writer.add_page(p)

writer.add_metadata({
    "/Title": "Trabalho Prático 2 — %s" % DISCIPLINA,
    "/Author": ALUNO,
    "/Subject": "TP2",
})

destino = os.path.join(BASE, SAIDA)
with open(destino, "wb") as fh:
    writer.write(fh)
os.remove(corpo)
os.remove(capa_gerada)

print("OK ->", destino)
print("paginas:", len(writer.pages))
if faltando:
    print("prints faltando (exercicios):", ", ".join(str(n) for n in faltando))
else:
    print("todos os prints incluidos")
