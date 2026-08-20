import os

from PyPDF2 import PdfReader


def extract_text(file_path: str):

    """
    Extract text from PDF or TXT file.
    """

    extension = os.path.splitext(
        file_path
    )[1].lower()


    # ======================================================
    # PDF
    # ======================================================

    if extension == ".pdf":

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

        return text.strip()


    # ======================================================
    # TXT
    # ======================================================

    elif extension == ".txt":

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read().strip()


    # ======================================================
    # Unsupported
    # ======================================================

    else:

        raise ValueError(
            "Unsupported file format. "
            "Only PDF and TXT are supported."
        )