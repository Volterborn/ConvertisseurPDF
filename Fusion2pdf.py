from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output):
    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output)
    merger.close()

"""
Assurez-vous d'avoir les fichiers PDF dans le projet et d'avoir deux fichiers pdf.
"""

#merge_pdfs(["", ""], "merged.pdf")