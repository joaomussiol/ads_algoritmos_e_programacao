from shoppinglib.users import user_exists, create_user, get_user_password
from shoppinglib.shopping_list import ShoppingListManager


class App:

    def __init__(self):
        self.user = None
        self.shopping = ShoppingListManager()

    def validate_login(self, login, password):
        self.user = user_exists(login)
        if self.user and get_user_password(login) == password:
            return True
        self.user = None
        return False

    def register_user(self, username, password):
        if not user_exists(username):
            self.user = create_user(username, password)
            return self.user is not None
        return False

    def create_list(self, name, market):
        self.shopping.create_list(name, market)

    def add_item(self, name, barcode, price, quantity):
        self.shopping.add_item(name, barcode, price, quantity)

    def get_items(self):
        return self.shopping.get_items()

    def get_item_by_barcode(self, barcode):
        current_list = self.shopping.get_current_list()
        if not current_list:
            return None

        for entry in current_list.items:
            if entry.item.bar_code == barcode:
                return {
                    "name": entry.item.name,
                    "price": entry.price,
                    "quantity": entry.quantity
                }

        return None

