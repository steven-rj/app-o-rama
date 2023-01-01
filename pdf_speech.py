import main_menu

import pyttsx3
import PyPDF2


def pdf_to_mp3(file):

    pdf_reader = PyPDF2.PdfReader(open(file, "rb"))
    num_pages = len(pdf_reader.pages)
    speaker = pyttsx3.init()

    for page in range(num_pages):
        data = pdf_reader.pages[page]
        text = data.extract_text()
        clean_text = text.strip().replace("\n", " ")
        print(clean_text)

    speaker.save_to_file(clean_text, "output.mp3")
    speaker.runAndWait()
    speaker.stop()


def main():

    print("PDF-to-Speech v1.0")
    pdf_name = input("Enter PDF filename (include .pdf): ")
    print("A recording of your PDF has been saved as 'output.mp3'.")
    main_menu.display_main_menu()


if __name__ == "__main__":
    main()
