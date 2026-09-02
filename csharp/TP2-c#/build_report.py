# -*- coding: utf-8 -*-
"""Gera o PDF do TP2 de C# a partir dos fontes em ./src e dos prints em ./screenshots."""
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
SRC = os.path.join(BASE, "src")
SCREENSHOTS = os.path.join(BASE, "screenshots")

ALUNO = "Gabriel Alves Sandre da Silva"
DISCIPLINA = "Fundamentos de Desenvolvimento com C#"
TRABALHO = "TP-2"
DATA_ENTREGA = "02/09/2026"
LOGO = os.path.join(BASE, "capa_logo.png")
SAIDA = "Gabriel_Sandre_DR2_TP2.PDF"

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


# Exercicios sem codigo ainda (arquivo nao existe em src/): aparecem como
# pendencia visivel em vez de quebrar a geracao do PDF.
def bloco_codigo_ou_pendencia(arquivo):
    caminho = os.path.join(SRC, arquivo)
    if os.path.exists(caminho):
        return [bloco_codigo(arquivo)], True
    return [Paragraph("[ PENDENTE: adicionar <b>src/%s</b> ]" % arquivo, pendente)], False


def evidencia(num):
    """Print da execucao, se existir; senao um aviso visivel de pendencia."""
    for base in ("ex%d" % num, "ex%02d" % num):
        for ext in (".png", ".jpg", ".jpeg"):
            nome = base + ext
            if os.path.exists(os.path.join(SCREENSHOTS, nome)):
                return [imagem_ajustada(nome),
                        Paragraph("Execu\u00e7\u00e3o do Exerc\u00edcio %d." % num, caption)], True
    return [Paragraph("[ PENDENTE: inserir o print da execu\u00e7\u00e3o como "
                      "<b>screenshots/ex%d.png</b> ]" % num, pendente)], False


def gerar_capa(caminho):
    """Redesenha a capa institucional com os dados deste trabalho."""
    from reportlab.pdfgen import canvas as _canvas

    AZUL_FUNDO = HexColor("#EAF2FB")
    BRANCO = HexColor("#FFFFFF")
    TINTA = HexColor("#1A1A1A")

    c = _canvas.Canvas(caminho, pagesize=A4)
    larg, alt = A4

    c.setFillColor(AZUL_FUNDO)
    c.rect(0, 0, larg, alt, stroke=0, fill=1)

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
    1: "Parte 1 \u2014 Programa que manipula datas",
    4: "Parte 2 \u2014 Programas que utilizam entrada do usu\u00e1rio",
    7: "Parte 3 \u2014 C\u00f3digos usando elementos de controle de fluxo",
    10: "Parte 4 \u2014 C\u00f3digos usando instru\u00e7\u00f5es de repeti\u00e7\u00e3o",
}

EXERCICIOS = [
    dict(n=1, titulo="C\u00e1lculo de Idade Precisa", arquivo="CalculoIdadePrecisa.cs",
         enunciado="Crie um programa em C# que solicite a data de nascimento do usu\u00e1rio e "
                   "calcule sua idade exata em anos, meses e dias.",
         obs=["Utilize a classe DateTime para capturar e manipular datas.",
              "Considere anos bissextos no c\u00e1lculo.",
              "Exiba a idade formatada corretamente."]),

    dict(n=2, titulo="Dias at\u00e9 o Pr\u00f3ximo Anivers\u00e1rio", arquivo="DiasProximoAniversario.cs",
         enunciado="Desenvolva um programa que pe\u00e7a ao usu\u00e1rio sua data de nascimento e informe "
                   "quantos dias faltam para o pr\u00f3ximo anivers\u00e1rio.",
         obs=["Utilize a classe DateTime para calcular a diferen\u00e7a entre datas.",
              "Exiba o resultado em dias."]),

    dict(n=3, titulo="Diferen\u00e7a Entre Duas Datas", arquivo="DiferencaEntreDatas.cs",
         enunciado="Escreva um programa que solicite ao usu\u00e1rio duas datas e calcule a "
                   "diferen\u00e7a em dias, meses e anos entre elas.",
         obs=["Utilize a classe DateTime e TimeSpan para o c\u00e1lculo.",
              "Exiba o intervalo formatado corretamente."]),

    dict(n=4, titulo="Formul\u00e1rio de Cadastro Simples", arquivo="FormularioCadastroSimples.cs",
         enunciado="Crie um programa que solicite nome, idade, telefone e e-mail do usu\u00e1rio e "
                   "exiba os dados cadastrados de forma organizada.",
         obs=["Utilize Console.ReadLine() para entrada de dados.",
              "Exiba os dados de forma formatada e clara."]),

    dict(n=5, titulo="Conversor de Temperatura", arquivo="ConversorTemperatura.cs",
         enunciado="Desenvolva um programa que pe\u00e7a ao usu\u00e1rio um valor em graus Celsius e o "
                   "converta para Fahrenheit e Kelvin.",
         obs=["Utilize a f\u00f3rmula: F = C * 9/5 + 32 e K = C + 273.15.",
              "Exiba os resultados com duas casas decimais."]),

    dict(n=6, titulo="C\u00e1lculo de IMC", arquivo="CalculoIMC.cs",
         enunciado="Escreva um programa que solicite peso e altura do usu\u00e1rio e calcule seu "
                   "\u00cdndice de Massa Corporal (IMC), classificando-o em faixas de peso.",
         obs=["Utilize a f\u00f3rmula: IMC = peso / (altura * altura).",
              "Classifique o usu\u00e1rio conforme as faixas do IMC."]),

    dict(n=7, titulo="Verificador de N\u00famero Par ou \u00cdmpar", arquivo="VerificadorParImpar.cs",
         enunciado="Crie um programa que solicite um n\u00famero inteiro e determine se ele \u00e9 par "
                   "ou \u00edmpar.",
         obs=["Utilize estruturas condicionais para verificar a paridade.",
              "Exiba uma mensagem indicando o resultado."]),

    dict(n=8, titulo="Classifica\u00e7\u00e3o de Nota Escolar", arquivo="ClassificacaoNotaEscolar.cs",
         enunciado="Desenvolva um programa que pe\u00e7a ao usu\u00e1rio uma nota de 0 a 10 e "
                   "classifique-a como \"Insuficiente\" (&lt; 6), \"Regular\" (&gt;= 6 e &lt; 7), "
                   "\"Bom\" (&gt;= 7 e &lt; 9) ou \"Excelente\" (&gt;= 9 e &lt;= 10).",
         obs=["Utilize estruturas condicionais para determinar a classifica\u00e7\u00e3o."]),

    dict(n=9, titulo="Calculadora de Sal\u00e1rio L\u00edquido", arquivo="CalculadoraSalarioLiquido.cs",
         enunciado="Escreva um programa que solicite o sal\u00e1rio bruto do usu\u00e1rio e calcule o "
                   "valor l\u00edquido ap\u00f3s descontos de impostos.",
         obs=["Utilize faixas de imposto definidas no c\u00f3digo.",
              "Exiba o sal\u00e1rio bruto, os descontos e o sal\u00e1rio l\u00edquido."]),

    dict(n=10, titulo="Contagem Regressiva", arquivo="ContagemRegressiva.cs",
         enunciado="Crie um programa que solicite um n\u00famero ao usu\u00e1rio e exiba uma contagem "
                   "regressiva at\u00e9 0.",
         obs=["Utilize um la\u00e7o de repeti\u00e7\u00e3o para realizar a contagem.",
              "Exiba os n\u00fameros separados por v\u00edrgula."]),

    dict(n=11, titulo="Tabuada Interativa", arquivo="TabuadaInterativa.cs",
         enunciado="Desenvolva um programa que solicite um n\u00famero ao usu\u00e1rio e exiba sua "
                   "tabuada de 1 a 10.",
         obs=["Utilize um la\u00e7o de repeti\u00e7\u00e3o para calcular a tabuada."]),

    dict(n=12, titulo="Jogo de Adivinha\u00e7\u00e3o", arquivo="JogoAdivinhacao.cs",
         enunciado="Escreva um programa que gere um n\u00famero aleat\u00f3rio de 1 a 100 e permita que "
                   "o usu\u00e1rio tente adivinh\u00e1-lo, informando se o palpite \u00e9 maior ou menor at\u00e9 "
                   "acertar.",
         obs=["Utilize um la\u00e7o de repeti\u00e7\u00e3o para permitir m\u00faltiplos palpites.",
              "Utilize a classe Random para gerar o n\u00famero secreto."]),
]

# ---------------------------------------------------------------- montagem
story = []
faltando_codigo = []
faltando_print = []

story.append(Spacer(1, 5 * cm))
story.append(Paragraph("Trabalho Pr\u00e1tico 2", title_style))
story.append(Paragraph(DISCIPLINA, capa_sub))
story.append(Spacer(1, 3 * cm))
story.append(Paragraph("<b>Aluno:</b> %s" % ALUNO, capa_nome))
story.append(Paragraph("Instituto Infnet", capa_sub))
story.append(PageBreak())

for ex in EXERCICIOS:
    if ex["n"] in PARTES:
        story.append(Paragraph(PARTES[ex["n"]], parte_style))

    story.append(Paragraph("Exerc\u00edcio %d \u2014 %s" % (ex["n"], ex["titulo"]), h2))
    story.append(Paragraph("<b>Enunciado</b>", h3))
    story.append(Paragraph(ex["enunciado"], body))
    story.append(Paragraph("<b>Observa\u00e7\u00f5es</b>", h3))
    for o in ex["obs"]:
        story.append(Paragraph(o, bullet, bulletText="\u2022"))

    story.append(Paragraph("<b>C\u00f3digo-fonte</b> (%s)" % ex["arquivo"], h3))
    flow, ok = bloco_codigo_ou_pendencia(ex["arquivo"])
    story.extend(flow)
    if not ok:
        faltando_codigo.append(ex["n"])
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>Execu\u00e7\u00e3o</b>", h3))
    flow, ok = evidencia(ex["n"])
    story.extend(flow)
    if not ok:
        faltando_print.append(ex["n"])

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
    "/Title": "Trabalho Pr\u00e1tico 2 \u2014 %s" % DISCIPLINA,
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
if faltando_codigo:
    print("codigo faltando (exercicios):", ", ".join(str(n) for n in faltando_codigo))
if faltando_print:
    print("prints faltando (exercicios):", ", ".join(str(n) for n in faltando_print))
if not faltando_codigo and not faltando_print:
    print("tudo incluido")
