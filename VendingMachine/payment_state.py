from state import State
from coin import Coin
from note import Note


class PaymentState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def select_product(self):
        print("Product already selected. Make Payment.")

    def insert_coin(self, coin: Coin):
        self.vending_machine.add_coin(coin)
        print(f"Coin inserted: {coin.name}")
        self.check_payment_status()

    def insert_note(self, note: Note):
        self.vending_machine.add_coin(note)
        print(f"Coin inserted: {note.name}")
        self.check_payment_status()

    def dispense_product(self):
        print("Wait for payment to complete.")

    def return_change(self):
        change = self.vending_machine.total_amount_inserted - self.vending_machine.selected_product.price
        if change > 0:
            print(f"Change returned: ${change:.2f}")
        else:
            print(f"No change to return.")
        self.vending_machine.reset_payment()

    def check_payment_status(self):
        if self.vending_machine.selected_product.price <= self.vending_machine.total_amount_inserted:
            self.return_change()
            self.vending_machine.set_state(self.vending_machine.dispense_state)

