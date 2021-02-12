class atm():
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
    def withdraw(self, amount):
        amount = amount
        print("Succesfully withdrew "+amount)
    def balance(self):
        print('idk how much u have lol i is crummy atm')
    def deposit(self, amount):
        amount = amount
        print("Successfully deposited "+amount)
    def heist(self):
        print("YOU ROBBED THE AUTOMATIC TRANSACTION MACHINE WHATCHAMACALLIT POGGERS")
Atm = atm(5381671900418464, 9169)
Atm.withdraw("300")
Atm.balance()
Atm.heist()