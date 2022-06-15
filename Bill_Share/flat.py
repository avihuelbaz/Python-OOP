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