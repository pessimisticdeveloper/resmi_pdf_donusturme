import img2pdf

pdf_olacak = img2pdf.convert("resim.PNG")
pdf = open("resimpdf.pdf","wb")
pdf.write(pdf_olacak)
pdf.close()
