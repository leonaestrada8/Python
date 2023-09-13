
# CÓDIGO ORIGINAL PARA SER REFATORADO

class StockManagement:
    def __init__(self):
        self.stock = {}

    def add_product(self, product_name, quantity):
        if product_name in self.stock:
            self.stock[product_name] += quantity
        else:
            self.stock[product_name] = quantity

    def remove_product(self, product_name, quantity):
        if product_name in self.stock and self.stock[product_name] >= quantity:
            self.stock[product_name] -= quantity
        else:
            print("Not enough stock or product not found")

    def get_stock(self, product_name):
        if product_name in self.stock:
            return self.stock[product_name]
        else:
            return "Product not found"


# Usage
stock_manager = StockManagement()
stock_manager.add_product("Apple", 10)
stock_manager.remove_product("Orange", 5)
print(stock_manager.get_stock("Apple"))  # Outputs 10
print(stock_manager.get_stock("Orange"))  # Outputs "Product not found"
