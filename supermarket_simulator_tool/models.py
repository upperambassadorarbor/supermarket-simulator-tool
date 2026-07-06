"""Data models for supermarket simulator."""

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
import uuid

@dataclass
class Product:
    """Represents a product in the supermarket."""
    name: str
    price: float
    quantity: int
    category: str
    product_id: str = None

    def __post_init__(self):
        if self.product_id is None:
            self.product_id = str(uuid.uuid4())[:8]

    def update_stock(self, amount: int) -> bool:
        """Update product stock level."""
        if self.quantity + amount < 0:
            return False
        self.quantity += amount
        return True

@dataclass
class Customer:
    """Represents a customer in the supermarket."""
    name: str
    budget: float
    cart: List[Product] = None

    def __post_init__(self):
        if self.cart is None:
            self.cart = []

    def add_to_cart(self, product: Product) -> bool:
        """Add product to customer's cart if affordable."""
        if product.price <= self.budget:
            self.cart.append(product)
            self.budget -= product.price
            return True
        return False

@dataclass
class Transaction:
    """Represents a completed purchase transaction."""
    transaction_id: str
    customer: Customer
    products: List[Product]
    total: float
    timestamp: datetime
    success: bool

    def __init__(self, customer: Customer, products: List[Product], success: bool):
        self.transaction_id = str(uuid.uuid4())[:12]
        self.customer = customer
        self.products = products
        self.total = sum(p.price for p in products)
        self.timestamp = datetime.now()
        self.success = success