with open("report.pdf", "rb") as source:
    pdf_data = source.read()
with open("report_copy.pdf", "wb") as destination:
    destination.write(pdf_data)
print("PDF copied successfully.")