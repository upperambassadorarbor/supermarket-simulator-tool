"""Core supermarket simulator engine."""

from typing import List, Optional
from .models import Product, Customer, Transaction
from datetime import datetime
import random

class SupermarketSimulator:
    """Simulates a supermarket environment with inventory and transactions."""

    def __init__(self, name: str = "SuperMart"):
        self.name = name
        self.inventory: List[Product] = []
        self.customers: List[Customer] = []
        self.transactions: List[Transaction] = []
        self.daily_revenue: float = 0.0

    def add_product(self, product: Product) -> None:
        """Add a product to inventory."""
        existing = [p for p in self.inventory if p.product_id == product.product_id]
        if existing:
            existing[0].quantity += product.quantity
        else:
            self.inventory.append(product)

    def remove_product(self, product_id: str) -> bool:
        """Remove a product from inventory by ID."""
        for i, product in enumerate(self.inventory):
            if product.product_id == product_id:
                self.inventory.pop(i)
                return True
        return False

    def find_product(self, name: str) -> Optional[Product]:
        """Find a product by name."""
        for product in self.inventory:
            if product.name.lower() == name.lower() and product.quantity > 0:
                return product
        return None

    def process_purchase(self, customer: Customer, product_name: str) -> Transaction:
        """Process a single product purchase for a customer."""
        product = self.find_product(product_name)
        if product and customer.add_to_cart(product):
            product.quantity -= 1
            transaction = Transaction(customer, [product], True)
            self.daily_revenue += product.price
        else:
            transaction = Transaction(customer, [], False)
        self.transactions.append(transaction)
        return transaction

    def get_inventory_summary(self) -> dict:
        """Get summary of current inventory."""
        return {
            "total_products": len(self.inventory),
            "total_value": sum(p.price * p.quantity for p in self.inventory),
            "categories": list(set(p.category for p in self.inventory))
        }

    def reset_simulation(self) -> None:
        """Reset the simulator state."""
        self.inventory.clear()
        self.customers.clear()
        self.transactions.clear()
        self.daily_revenue = 0.0