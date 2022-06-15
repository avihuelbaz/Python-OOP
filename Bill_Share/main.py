import webbrowser
from fpdf import *
import time

class Bill:
    """
    Object that contains data about a bill such as total amount and period
    """
    def __init__(self, amount, period):
        self.period = period
        self.amount = amount
    
class flatmate:
    """
    Contains person data such as name and days in house
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house=days_in_house


    def pays(self,bill,flatmate2):
        wehigt= self.days_in_house/(self.days_in_house+flatmate2.days_in_house)
        return bill.amount*wehigt
class PdfReport:
    """
    Create PDF file that describe the bill
    """
    def __init__(self, filename):
        self.filename=filename
    def generate(self,flatmate1,flatmate2,bill):
       flatmate1_pay=str(round(flatmate1.pays(bill,flatmate2),2))
       flatmate2_pay=str(round(flatmate2.pays(bill,flatmate1),2))
       pdf=FPDF(orientation='P',unit='pt',format='A4')
       pdf.add_page()
       #Insert title
       pdf.set_font(family='Times',size=24,style='B')
       pdf.cell(w=0,h=80,txt="Flatmates Bill",border=1,align="C",ln=1)
       #Insert Period label and value
       pdf.set_font(family='Times',size=12)
       pdf.cell(w=100,h=40,txt="Period:",border=1)
       pdf.cell(w=150,h=40,txt=bill.period,border=1,ln=1)
       #Insert name and due amount of the first flatmate
       pdf.cell(w=100,h=40,txt=flatmate1.name,border=1)
       pdf.cell(w=150,h=40,txt=flatmate1_pay,border=1,ln=1)
       pdf.cell(w=100,h=40,txt=flatmate2.name,border=1)       
       pdf.cell(w=150,h=40,txt=flatmate2_pay,border=1)    
       pdf.output(self.filename)
       webbrowser.open(self.filename)
       time.sleep(10)

bill = Bill(120, "March 2021")
john = flatmate("John", 20)
marry = flatmate("Marry", 25)

print (john.pays(bill,marry))
print (marry.pays(bill,john))

pdf_report=PdfReport('Report.pdf')
pdf_report.generate(john,marry,bill)
