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


    def pays(self,bill):
       return bill.amount/2

class PdfReport:
    """
    Create PDF file that describe the bill
    """
    def __init__(self, filename):
        self.filename=filename
        def generate(self,flatmate1, flatmate2, bill):
            pass


bill = Bill(120, "March 2021")
john = flatmate("John", 20)
marry = flatmate("Marry", 10)

print (john.pays(bill=bill))
