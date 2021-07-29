class ATM:
    def __init__(self, cardNo, pin):
        self.cardNo = cardNo
        self.pin = pin
        self.amount = 0
        self.amountInAccount = 10000
    def cashWithdrawal(self):
        print("You have ₹10000 in your account")
        amount = int(input("Type the amount to be withdrawn here."))
        if amount>8000:
            print("Amount is too high. Please enter a smaller amount")
            amount = int(input("Type the amount to be withdrawn here."))
        elif amount<100:
            print("Amount is too low. Enter a larger amount")
            amount = int(input("Type the amount to be withdrawn here."))
        self.amountInAccount = 10000 - amount
        print("Done! You now have ₹" + str(self.amountInAccount) + " left in you account.")
    def balanceInquiry(self):
        print("You have " + str(self.amountInAccount) + " in your account.")
pinNo = int(input("Please enter you pin number"))
cardNumber = int(input("Please enter your card number"))
customer = ATM(cardNumber, pinNo)
reply = int(input("Type 1 for cash withdrawal or 2 for balance enquiry"))
if reply==1:
  customer.cashWithdrawal()
else:
  customer.balanceInquiry()