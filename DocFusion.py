import os
from PyPDF2 import PdfMerger

def merge_pdfs(directory):
    merger = PdfMerger()
    pdf_files = [file for file in os.listdir(directory) if file.lower().endswith('.pdf')]

    if not pdf_files:
        print(f"No PDF files found in {directory}")
        return

    pdf_files.sort()  # Ensure files are sorted for consistent merging order

    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)
        merger.append(pdf_path)

    merged_pdf_path = os.path.join(directory, f"{os.path.basename(directory)}.pdf")
    merger.write(merged_pdf_path)
    merger.close()

def main():
    root_directory = "D:\OICL\ESTATE MANAGEMENT\BOX 138 - Copy"  # Change this to the root directory of your PDFs
    subdirectories = [d for d in os.listdir(root_directory) if os.path.isdir(os.path.join(root_directory, d))]

    for subdir in subdirectories:
        subdir_path = os.path.join(root_directory, subdir)
        merge_pdfs(subdir_path)
        print(f"Merged PDFs in {subdir} directory.")

if __name__ == "__main__":
    main()
