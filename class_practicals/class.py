class Purchase:
    counter = 10000
    total_order = 0
    total_quantity = 0
    def__init__(self, product_name, quantity, price):
    self.order_id = Purchase.counter
    Purchase.counter += 1
    self.product_name = product_name
    self.quantity = quantity
    self.price = price
    Purchase.total_order += 1
    Purchase.total_quantity += quantity


def total_cost(self):
    total = self.quantity * self.price
    return total


def update_quantity(self, update):
    Purchase.total_quantity -= self.quantity
    self.quantity = update
    Purchase.total_quantity += update
    print(f"Update successfully to {update}")


def discount(self):
    if self.total_cost() >= 500:
        discount_total = self.total_cost() * (5 / 100)  # makes it static
        return self.total_cost() - discount_total
    else:
        return self.total
        cost


def summary(self):
    print("Summary: ")
    print(f"Order ID:{self.order_id} ")
    print(f"Product name: {self.product_name}")
    print(f"Quantity: {self.quantity}")
    print(f"Unit price: {self.price}")
    print(f"Total: {self.total_cost()}")
    print(f"Discounted total: {self.discount()}")


@classmethod  # can use other methods e.g static
def statistics(cls):
    print(".....Summary.....")
    print(f"Total order:{cls.total_order}")
    print(f"Total quantity: {cls.total_quantity}")


order1 = Purchase("Phone", 10, 200)
order1.summary()

order2 = Purchase("Laptop", 2, 1000)
order2.summary()
# print("Total order for today: ", Purchase.total_order)
# print(f"Total quantity for today: {Purchase.total_quantity}")
Purchase.statistics()