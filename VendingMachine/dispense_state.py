from state import State
from coin import Coin
from note import Note


class DispenseState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def select_product(self):
        print("Product already selected. Payment Completed.")

    def insert_coin(self, coin: Coin):
        print("Product already selected. Payment Completed.")

    def insert_note(self, note: Note):
        print("Product already selected. Payment Completed.")

    def dispense_product(self):

        product = self.vending_machine.selected_product
        self.vending_machine.inventory.update_quantity(product, self.vending_machine.inventory.get_quantity(product)-1)
        print("Please collect your product.")
        self.vending_machine.set_state(self.vending_machine.idle_state)


    def return_change(self):
        print("Product already selected. Payment Completed.")



