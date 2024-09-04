class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0  # Initialize the total to 0.0
        self.discount = discount  # Initialize the discount
        self.items = []  # Initialize an empty list to store items
        self.last_transaction = 0  # Track the last transaction amount

    def add_item(self, title, price, quantity=1):
        # Add the price multiplied by the quantity to the total
        self.total += price * quantity
        # Add the item to the items list the number of times it was purchased
        self.items.extend([title] * quantity)
        # Keep track of the last transaction amount
        self.last_transaction = price * quantity

    def apply_discount(self):
        # Check if there's a discount to apply
        if self.discount > 0:
            # Calculate the discount and apply it to the total
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # Print the success message with the updated total
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            # Print the error message when no discount is available
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Subtract the last transaction from the total
        self.total -= self.last_transaction
        # Reset the last transaction to 0
        self.last_transaction = 0
