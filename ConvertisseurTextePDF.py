from fpdf import FPDF

def text_to_pdf(texte, pdf_sortie):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, texte)
    pdf.output(pdf_sortie)

"""
Enlevez ce commentaire afin de pouvoir tester.
"""
# text_to_pdf("Bonjour, ceci est un test.", "texte.pdf")
