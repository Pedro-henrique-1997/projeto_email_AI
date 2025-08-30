from flask import Flask, render_template, request
from PyPDF2 import PdfReader

app = Flask(__name__)

# Função para extrair texto de PDF
def extrair_texto_pdf(file):
    reader = PdfReader(file)
    texto = ""
    for page in reader.pages:
        texto += page.extract_text() + "\n"
    return texto.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    category = None
    response = None
    texto_extraido = None

    if request.method == "POST":
        email_text = request.form.get("emailText")
        email_file = request.files.get("emailFile")

        # Verifica qual entrada foi enviada
        if email_file:
            if email_file.filename.endswith(".pdf"):
                texto_extraido = extrair_texto_pdf(email_file)
            elif email_file.filename.endswith(".txt"):
                texto_extraido = email_file.read().decode('utf-8')
        elif email_text:
            texto_extraido = email_text

        # Se houver texto extraído, faz a classificação (mock)
        if texto_extraido:
            lower_text = texto_extraido.lower()
            if any(palavra in lower_text for palavra in ["obrigado", "feliz", "concluído", "resolvido"]):
                category = "Improdutivo"
                response = "Obrigado pelo contato! Não é necessária ação."
            else:
                category = "Produtivo"
                response = "Recebemos sua mensagem e vamos analisar."

    return render_template("index.html", category=category, response=response, texto_extraido=texto_extraido)

if __name__ == "__main__":
    app.run(debug=True)
