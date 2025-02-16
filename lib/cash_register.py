class CashRegister:
    def __init__(self, discount=0):
        """Initialize a new cash register with an optional discount percentage"""
        self.discount = discount
        self.total = 0
        self.items = []
        self._last_transaction_amount = 0
        self._last_transaction_quantity = 0

    def add_item(self, title, price, quantity=1):
        """Add an item to the register with a title, price, and optional quantity"""
        transaction_total = price * quantity
        self.total += transaction_total
        
        # Store info about this transaction for potential void
        self._last_transaction_amount = transaction_total
        self._last_transaction_quantity = quantity
        
        # Add the items to our items list
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        """Apply the registered discount to the current total"""
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        
        # Calculate discounted total
        self.total = self.total * (1 - self.discount / 100)
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        """Remove the last transaction from the total and items list"""
        # Subtract the last transaction amount from the total
        self.total -= self._last_transaction_amount
        
        # Remove the items from the items list
        for _ in range(self._last_transaction_quantity):
            if self.items:  # Check if there are items to remove
                self.items.pop()
        
        # Reset the last transaction tracking
        self._last_transaction_amount = 0
        self._last_transaction_quantity = 0