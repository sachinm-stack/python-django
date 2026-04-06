from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount, currency='INR'):
        self.amount   = amount
        self.currency = currency

    @abstractmethod
    def process_payment(self):
        pass

    def payment_summary(self):
        print(f'--- Payment Summary ---')
        self.process_payment()
        print(f'Amount: {self.currency} {self.amount}')


class CashPayment(Payment):
    def process_payment(self):
        print(f'Processing cash payment of ₹{self.amount}')


class CardPayment(Payment):
    def __init__(self, amount, card_number, currency='INR'):
        super().__init__(amount, currency)
        self.card_number = card_number

    def process_payment(self):
        last4 = self.card_number[-4:]
        print(f'Processing card payment using **** **** **** {last4}')


class UPIPayment(Payment):
    def __init__(self, amount, upi_id, currency='INR'):
        super().__init__(amount, currency)
        self.upi_id = upi_id

    def process_payment(self):
        print(f'Processing UPI payment using {self.upi_id}')


# Test:
payments = [
    CashPayment(500),
    CardPayment(1200, '1234567890121234'),
    UPIPayment(750, 'rahul@upi')
]

for pay in payments:
    pay.payment_summary()
    print()