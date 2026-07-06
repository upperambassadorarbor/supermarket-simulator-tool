"""Tests for supermarket simulator tool."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from supermarket_simulator_tool import SupermarketSimulator, Product, Customer, Trainer

class TestSupermarketSimulator(unittest.TestCase):
    """Test suite for SupermarketSimulator."""

    def setUp(self):
        self.sim = SupermarketSimulator("TestMart")
        self.apple = Product("Apple", 0.50, 100, "Fruit")
        self.banana = Product("Banana", 0.30, 150, "Fruit")
        self.sim.add_product(self.apple)
        self.sim.add_product(self.banana)

    def test_add_product(self):
        self.assertEqual(len(self.sim.inventory), 2)
        new_product = Product("Orange", 0.80, 50, "Fruit")
        self.sim.add_product(new_product)
        self.assertEqual(len(self.sim.inventory), 3)

    def test_remove_product(self):
        result = self.sim.remove_product(self.apple.product_id)
        self.assertTrue(result)
        self.assertEqual(len(self.sim.inventory), 1)

    def test_find_product(self):
        found = self.sim.find_product("Apple")
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Apple")

    def test_process_purchase_success(self):
        customer = Customer("Alice", 10.0)
        transaction = self.sim.process_purchase(customer, "Apple")
        self.assertTrue(transaction.success)
        self.assertEqual(self.sim.daily_revenue, 0.50)

    def test_process_purchase_failure(self):
        customer = Customer("Bob", 0.10)
        transaction = self.sim.process_purchase(customer, "Apple")
        self.assertFalse(transaction.success)

    def test_inventory_summary(self):
        summary = self.sim.get_inventory_summary()
        self.assertEqual(summary["total_products"], 2)
        self.assertAlmostEqual(summary["total_value"], 95.0)

    def test_reset_simulation(self):
        self.sim.reset_simulation()
        self.assertEqual(len(self.sim.inventory), 0)
        self.assertEqual(self.sim.daily_revenue, 0.0)

class TestTrainer(unittest.TestCase):
    """Test suite for Trainer."""

    def setUp(self):
        self.sim = SupermarketSimulator("TrainMart")
        self.sim.add_product(Product("Milk", 2.50, 50, "Dairy"))
        self.sim.add_product(Product("Bread", 1.50, 80, "Bakery"))
        self.trainer = Trainer(self.sim)

    def test_optimize_pricing(self):
        product = self.sim.inventory[0]
        price = self.trainer.optimize_pricing(product.product_id, demand_factor=1.5)
        self.assertGreater(price, product.price)

    def test_restock_suggestion(self):
        suggestions = self.trainer.restock_suggestion(threshold=60)
        self.assertEqual(len(suggestions), 1)  # Milk has 50 < 60

    def test_run_training_episode(self):
        data = self.trainer.run_training_episode(steps=5)
        self.assertIn("transactions", data)
        self.assertIn("revenue_generated", data)

    def test_training_summary(self):
        self.trainer.run_training_episode(steps=3)
        summary = self.trainer.get_training_summary()
        self.assertEqual(summary["episodes"], 1)
        self.assertGreater(summary["total_revenue"], 0)

if __name__ == "__main__":
    unittest.main()