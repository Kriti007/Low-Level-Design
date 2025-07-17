from product import Product
from state import State


class IdleState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine



class IdleState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine


    def select_product(self, product: Product):
        if self.vending_machine.inventory.is_available(product):
            self.vending_machine.selected_product = product
            self.vending_machine.set_state(self.vending_machine.payment_state)
            print(f"product selected: {product.name}")
        else:
            print(f" Product {product.name} is out of stock")

    def insert_coin(self, coin):
        print("Please select a product first.")

    def insert_note(self, note):
        print("Please select a product first.")

    def dispense_product(self):
        print("Please select a product first.")

    def return_change(self):
        print("Please select a product first.")
