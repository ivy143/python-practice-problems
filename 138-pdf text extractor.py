# PDF Text Extractor
import fitz  # PyMuPDF
import os
def extract_text_from_pdf(input_pdf_path, output_txt_path):
    # Open the PDF file
    pdf_document = fitz.open(input_pdf_path)
    all_text = []

    # Iterate through each page and extract text
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text()
        all_text.append(text)

    # Write the extracted text to a .txt file
    with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write('\n'.join(all_text))

    print(f"Text extracted and saved to: {output_txt_path}")
# Example usage
input_pdf = "sample.pdf"  # Path to your input PDF file
output_txt = "output.txt"  # Path to save the extracted text

extract_text_from_pdf(input_pdf, output_txt)
# This code extracts text from a PDF file and saves it to a .txt file using the PyMuPDF library.
# Make sure to have the required library installed:
# pip install PyMuPDF