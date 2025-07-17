from threading import Lock
from idle_state import IdleState
from dispense_state import DispenseState
from payment_state import PaymentState
from state import State
from inventory import Inventory


class VendingMachine:
    _instance = None
    _lock = Lock()
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.inventory = Inventory()
                cls._instance.dispense_state = DispenseState(cls._instance)
                cls._instance.payment_state = PaymentState(cls._instance)
                cls._instance.idle_state = IdleState(cls._instance)
                cls._instance.total_amount_inserted = 0.0
                cls._instance.selected_product = None
                cls._instance.current_state = cls._instance.idle_state
        return cls._instance

    @classmethod
    def getInstance(cls):
        return cls()

    def select_product(self, product):
        self.current_state.select_product(product)

    def insert_coin(self, coin):
        self.current_state.insert_coin(coin)

    def insert_note(self, note):
        self.current_state.insert_note(note)

    def return_change(self):
        self.current_state.return_change()

    def dispense_product(self):
        self.current_state.dispense_product()

    def add_coin(self, coin):
        self.total_amount_inserted += coin.value

    def add_note(self, note):
        self.total_amount_inserted += note.value

    def set_state(self, state : State):
        self.current_state = state

    def reset_payment(self):
        self.total_amount_inserted = 0.0

    def reset_product_selection(self):
        self.selected_product = None


