class Bill:
    amount = 0
    def __init__(self, amount):
        self.amount = amount
    def Pay(self, payment):
        self.amount -= payment.amount
        print("Payment made using", payment.mode)
        print("Balance:", self.amount)
    
class Payment:
    amount = 0
    mode = "Cash"
    def __init__(self, amount):
        self.amount = amount
        
class Ewallet(Payment):
    def __init__(self, name, amount):
        self.mode = name
        self.amount = amount
        
bigBeautifulBill = Bill(100)
bayad = Payment(67)
bigBeautifulBill.Pay(bayad)
gcash = Ewallet("PisayCash", 33)
bigBeautifulBill.Pay(gcash)