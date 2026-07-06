"""Trainer module for optimizing supermarket operations."""

from typing import List, Dict, Tuple
from .models import Product
from .simulator import SupermarketSimulator
import random

class Trainer:
    """Provides optimization and training methods for supermarket simulation."""

    def __init__(self, simulator: SupermarketSimulator):
        self.simulator = simulator
        self.training_data: List[Dict] = []

    def optimize_pricing(self, product_id: str, demand_factor: float = 1.0) -> float:
        """Suggest optimal price based on demand and current stock."""
        product = None
        for p in self.simulator.inventory:
            if p.product_id == product_id:
                product = p
                break
        
        if not product:
            return 0.0
        
        base_price = product.price
        stock_ratio = product.quantity / 100.0 if product.quantity < 100 else 1.0
        optimal_price = base_price * (1.0 + (demand_factor - stock_ratio) * 0.1)
        return round(optimal_price, 2)

    def restock_suggestion(self, threshold: int = 10) -> List[Tuple[Product, int]]:
        """Suggest products that need restocking."""
        suggestions = []
        for product in self.simulator.inventory:
            if product.quantity < threshold:
                suggested_amount = threshold * 2 - product.quantity
                suggestions.append((product, suggested_amount))
        return suggestions

    def run_training_episode(self, steps: int = 10) -> Dict:
        """Run a training episode to simulate random transactions."""
        initial_revenue = self.simulator.daily_revenue
        episode_data = {
            "transactions": 0,
            "revenue_generated": 0.0,
            "products_sold": 0
        }

        for _ in range(steps):
            if not self.simulator.inventory:
                break
            
            product = random.choice(self.simulator.inventory)
            customer_name = f"Customer_{random.randint(1, 100)}"
            customer = Customer(customer_name, random.uniform(1.0, 50.0))
            
            transaction = self.simulator.process_purchase(customer, product.name)
            if transaction.success:
                episode_data["transactions"] += 1
                episode_data["revenue_generated"] += transaction.total
                episode_data["products_sold"] += len(transaction.products)

        episode_data["revenue_generated"] = round(episode_data["revenue_generated"], 2)
        self.training_data.append(episode_data)
        return episode_data

    def get_training_summary(self) -> Dict:
        """Get summary of all training episodes."""
        if not self.training_data:
            return {"episodes": 0, "total_revenue": 0.0, "avg_transactions": 0.0}
        
        total_revenue = sum(e["revenue_generated"] for e in self.training_data)
        total_transactions = sum(e["transactions"] for e in self.training_data)
        
        return {
            "episodes": len(self.training_data),
            "total_revenue": round(total_revenue, 2),
            "avg_transactions": round(total_transactions / len(self.training_data), 2)
        }