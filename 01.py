import os
import subprocess
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def criar_recibo(recebedor, valor, contato, descricao):
    # Obtém o caminho para a área de trabalho do usuário no Linux
    area_de_trabalho = os.path.join(os.path.expanduser('~'), 'Desktop')

    # Define o nome do arquivo PDF na área de trabalho
    nome_arquivo = os.path.join(area_de_trabalho, f"recibo_{recebedor.replace(' ', '_')}.pdf")

    # Criação do arquivo PDF
    pdf = canvas.Canvas(nome_arquivo, pagesize=letter)
    pdf.setFont("Helvetica", 12)

    pdf.drawString(100, 750, "Recibo")
    pdf.drawString(100, 730, "-" * 30)

    # Informações do recibo
    pdf.drawString(100, 710, f"Recebedor: {recebedor}")
    pdf.drawString(100, 690, f"Valor: R$ {valor}")
    pdf.drawString(100, 670, f"Contato: {contato}")
    pdf.drawString(100, 650, f"Descrição: {descricao}")

    # Salva o conteúdo do PDF e fecha o arquivo
    pdf.save()

    print(f"Recibo gerado com sucesso: {nome_arquivo}")

    # Abre o arquivo PDF com o leitor padrão do sistema
    abrir_comando = f"xdg-open {nome_arquivo}"
    subprocess.run(abrir_comando, shell=True)

def main():
    # Solicita informações ao usuário
    recebedor = input("Informe o nome do recebedor: ")
    valor = input("Informe o valor: ")
    contato = input("Informe o contato: ")
    descricao = input("Informe a descrição: ")

    # Cria o recibo com as informações fornecidas
    criar_recibo(recebedor, valor, contato, descricao)

if __name__ == "__main__":
    main()

