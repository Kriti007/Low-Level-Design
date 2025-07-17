from vending_machine import VendingMachine
from product import Product
from coin import Coin
from note import Note


class VendingMachineDemo:
    @staticmethod
    def run():
        vending_machine = VendingMachine.getInstance()

        coke = Product("Coke", 50)
        chips = Product("Chips", 20)
        biscuits = Product("Biscuits", 20)
        vending_machine.inventory.add_product(coke, 10)
        vending_machine.inventory.add_product(biscuits, 10)
        vending_machine.inventory.add_product(chips, 10)

        vending_machine.select_product(coke)
        vending_machine.insert_coin(Coin.FIVE)
        vending_machine.insert_coin(Coin.FIVE)
        vending_machine.insert_coin(Coin.FIVE)
        vending_machine.insert_coin(Coin.FIVE)
        vending_machine.insert_note(Note.TEN)
        vending_machine.insert_note(Note.TWENTY)
        vending_machine.dispense_product()
        vending_machine.select_product(chips)
        vending_machine.insert_note(Note.HUNDRED)
        vending_machine.dispense_product()
        vending_machine.insert_coin(Coin.FIVE)


if __name__ == "__main__":
    VendingMachineDemo.run()


