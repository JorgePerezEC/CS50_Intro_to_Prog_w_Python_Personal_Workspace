from fpdf import FPDF
from datetime import date

class PDF(FPDF):
    def __init__(self, orientation="portrait", format="A4", name="Jorge Perez"):
        super().__init__(orientation=orientation, format=format)
        self.name = name

    def header(self):
        self.set_font("helvetica", "B", 30)
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        self.ln(20)

    def stamp(self):
        self.add_page()
        self.image("shirtificate.png", x=0, y=70)
        self.set_font_size(32)
        self.set_text_color(255,255,255)
        self.text(x=45, y=140, txt=f"{self.name} took CS50")
        self.output(f"shirtificate.pdf")

def main():
    name = input("Name: ")
    pdf = PDF("portrait", "A4", name)
    pdf.stamp()


if __name__ == "__main__":
    main()
