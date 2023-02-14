import fpdf

class PDF():
    def __init__ (self, name):
        self._pdf=fpdf.FPDF()
        self._pdf.add_page()
        self._pdf.set_font('helvetica','B',48)
        self._pdf.cell(0, 50,'CS50 Shirtificate', align = 'C')
        self._pdf.image('shirtificate.png',x=0, y=60)
        self._pdf.set_font('helvetica','B',30)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(50, 120, txt= f'{name} took CS50')

    def save(self, N):
        self._pdf.output(N)




name = input('please enter name: ')
pdf = PDF(name)

pdf.save('shirtificate.pdf')
