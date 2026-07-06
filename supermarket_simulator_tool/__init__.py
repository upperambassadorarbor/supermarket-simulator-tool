"""Supermarket Simulator Trainer - A tool to simulate and manage supermarket operations."""

__version__ = "0.1.0"
__author__ = "Supermarket Simulator Team"

from .simulator import SupermarketSimulator
from .trainer import Trainer
from .models import Product, Customer, Transaction

__all__ = ["SupermarketSimulator", "Trainer", "Product", "Customer", "Transaction"]