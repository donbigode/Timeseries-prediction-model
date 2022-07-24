#create a class that receives a pdf file as input and generates a csv file with all the data
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter


class PDF2CSV:
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file
        self.csv_file = None
        self.text = None

    def convert_pdf_to_txt(self):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos = set()

        with open(self.pdf_file, 'rb') as fp:
            parser = PDFParser(fp)
            document = PDFDocument(parser, password)

            if document.is_extractable:
                for page in PDFPage.create_pages(document):
                    interpreter.process_page(page)
                    data = retstr.getvalue()
                    self.text = data.decode('utf-8')
                    self.csv_file = self.pdf_file.replace('.pdf', '.csv')
                    with open(self.csv_file, 'w') as f:
                        f.write(self.text)
            else:
                raise PDFTextExtractionNotAllowed

        device.close()
        retstr.close()

    def get_text(self):
        return self.text

    def get_csv_file(self):
        return self.csv_file


#call the PDF2CSV class using Prod.pdf as input
pdf = PDF2CSV('Prod.pdf')