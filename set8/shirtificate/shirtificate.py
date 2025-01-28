from fpdf import FPDF

DEFAULT_NAME_FILE = "shirtificate"
DEFAULT_TITLE = "CS50 Shirtificate"
DEFAULT_IMAGE = "shirtificate.png"

class ShirtPDF:
    def __init__(self, name: str, name_file: str = DEFAULT_NAME_FILE,
                 title: str = DEFAULT_TITLE, image: str = DEFAULT_IMAGE) -> None:
        self._name = name
        self._name_file = name_file
        self._title = title
        self._image = image


    def generate_pdf(self) -> None:
        pdf = FPDF()

        # New Page
        pdf.add_page()

        # Add image
        pdf.image(self._image, 0, 50)

        # Add title
        pdf.set_font("Helvetica", size=50)
        pdf.set_text_color(130, 0, 130)
        pdf.text(40, 30, self._title)

        # Add title
        pdf.set_font("Helvetica", size=25)
        pdf.set_text_color(255, 255, 255)
        pdf.text(50, 130, f"{self._name} Harvard took CS50")

        pdf.output(f"{self._name_file}.pdf")


    @property
    def name(self):
        return self._name


    @property
    def name_file(self):
        return self._name_file


    @property
    def title(self):
        return self._title


    @property
    def image(self):
        return self._image


def main():
    name: str = input("Name: ").strip()
    pdf: ShirtPDF = ShirtPDF(name=name)
    pdf.generate_pdf()


if __name__ == "__main__":
    main()
