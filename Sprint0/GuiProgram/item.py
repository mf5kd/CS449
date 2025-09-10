class Item:

    # Constructor
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
    
    # setters and getters
    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id
    
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    
    def set_quantity(self, quantity):
        self.quantity = quantity
    def get_quantity(self):
        return self.quantity
    
    def set_price(self, price):
        self.price = price
    def get_price(self):
        return self.price
    
    # returns the fields as a string separated by commas
    def fields_as_string(self):
        return f"{self.get_id()},{self.get_name()},{self.get_quantity()},{self.get_price()}"

    def fields_as_list(self):
        return [self.get_id(), self.get_name(), self.get_quantity(), self.get_price()]
    
    def display(self):
        return f"ID = {self.get_id()} |Name = {self.get_name()} |Quantity = {self.get_quantity()} |Price = {self.get_price()}"