import ipdb

class Coffee:
    def __init__(self, name=""):
            self._name = name
            self.coffee_orders = []
            self.unique_customers = ()
            
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) == str and 3 <= len(new_name):
            return new_name
        
    def orders(self):
        return self.coffee_orders
        
    def customers(self):
        unique_customers = set()
        for order in self.coffee_orders:
            unique_customers.add(order.customer)
        return list(unique_customers)
    
    def num_orders(self):
        return len(self.coffee_orders) if self.coffee_orders else 0
    
    def average_price(self):
        if not self.coffee_orders:
            return 0
        total_price = sum(order.price for order in self.coffee_orders)
        return total_price / len(self.coffee_orders)
    

class Customer:
    def __init__(self, name):
        self._name = name
        self.customer_orders = []
        self.unique_coffees = ()
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) == str and (1 <= len(new_name) <= 15):
            self._name = new_name
        
    def orders(self):
        return self.customer_orders
    
    def coffees(self):
        unique_coffees = set()
        for order in self.customer_orders:
            unique_coffees.add(order.coffee)
        return list(unique_coffees)
    
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self.customer_orders.append(order)
        coffee.coffee_orders.append(order)
        return order

    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = price
        self.coffee.coffee_orders.append(self)
        self.customer.customer_orders.append(self)
        Order.all.append(self)

    @property
    def price(self):
            return self._price

    def __repr__(self):
       return f"Order(customer={self.customer}, coffee={self.coffee}, price={self.price})"
    
    @classmethod
    def orders(cls, coffee):
        coffee_orders = []

        for order in cls.all:
            if order.coffee == coffee:
                coffee_orders.append(order)
        return coffee_orders
    
    @classmethod
    def customers(cls, coffee):
        unique_customers = set()
        for order in cls.all:
            if order.coffee == coffee:
                unique_customers.add(order)
        return list(unique_customers)
    
    @classmethod
    def orders_for_customer(cls, customer):
        customer_orders = []

        for order in cls.all:
            if order.customer == customer:
                customer_orders.append(order)
        return customer_orders
    
    @classmethod
    def coffees_for_customers(cls, customer):
        unique_coffees = set()
        for order in cls.all:
            if order.customer == customer:
                unique_coffees.add(order.coffee)
        return list(unique_coffees)