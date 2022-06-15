import time
from flat import *
from report import *

bill_amount=float(input("hey user enter the bill amount: "))
period=input("What is the bill period?: ")
flatmate_1_name=input("What is your name?: ")
flatmate_1_period=float(input(f"How many days did {flatmate_1_name} stay in the house?: "))
flatmate_2_name=input("What is the flatmate name?: ")
flatmate_2_period=float(input(f"How many days did {flatmate_2_name} stay in the house?: "))
bill = Bill(bill_amount, period)
flat1 = flatmate(flatmate_1_name, flatmate_1_period)
flat2 = flatmate(flatmate_2_name, flatmate_2_period)

print (flat1.pays(bill,flat2))
print (flat2.pays(bill,flat1))

pdf_report=PdfReport('Report.pdf')
pdf_report.generate(flat1,flat2,bill)
time.sleep(10)
