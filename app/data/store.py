from __future__ import annotations

from typing import Any, Dict, List


class DataStore:
    def __init__(self) -> None:
        self.products = [
            {
                "id": "sku-1001",
                "name": "Minimal Phone Case",
                "category": "phone accessories",
                "buy_price": 3.75,
                "suggested_price": 14.99,
                "shipping_cost": 2.10,
                "packaging_cost": 0.65,
                "platform_fee_pct": 0.08,
                "supplier": "AliExpress",
                "supplier_url": "https://example.com/supplier/phone-case",
                "notes": "Strong demand / lightweight / easy to bundle",
            },
            {
                "id": "sku-1002",
                "name": "Cable Organizer",
                "category": "desk accessories",
                "buy_price": 2.20,
                "suggested_price": 9.99,
                "shipping_cost": 1.60,
                "packaging_cost": 0.45,
                "platform_fee_pct": 0.08,
                "supplier": "Printful",
                "supplier_url": "https://example.com/supplier/cable-organizer",
                "notes": "Low acquisition cost and strong impulsive-buy potential",
            },
            {
                "id": "sku-1003",
                "name": "Travel Bottle Set",
                "category": "wellness",
                "buy_price": 5.50,
                "suggested_price": 18.99,
                "shipping_cost": 2.40,
                "packaging_cost": 0.75,
                "platform_fee_pct": 0.08,
                "supplier": "Alibaba",
                "supplier_url": "https://example.com/supplier/travel-bottle-set",
                "notes": "Seasonal upswing, lower risk due to lower volume",
            },
        ]

        self.inventory = {
            "sku-1001": {"product_id": "sku-1001", "quantity_on_hand": 14, "reorder_level": 10, "lead_time_days": 4},
            "sku-1002": {"product_id": "sku-1002", "quantity_on_hand": 8, "reorder_level": 12, "lead_time_days": 5},
            "sku-1003": {"product_id": "sku-1003", "quantity_on_hand": 22, "reorder_level": 10, "lead_time_days": 6},
        }

        self.orders = {
            "ord-001": {
                "id": "ord-001",
                "product_id": "sku-1001",
                "quantity": 2,
                "selling_price": 14.99,
                "status": "pending",
                "payment_status": "paid",
                "shipping_status": "not_started",
                "customer_email": "alice@example.com",
            },
            "ord-002": {
                "id": "ord-002",
                "product_id": "sku-1002",
                "quantity": 1,
                "selling_price": 9.99,
                "status": "shipped",
                "payment_status": "paid",
                "shipping_status": "in_transit",
                "customer_email": "bob@example.com",
            },
        }

    def get_product(self, product_id: str) -> Dict[str, Any]:
        for item in self.products:
            if item["id"] == product_id:
                return item
        raise KeyError(f"Product {product_id} not found")

    def get_orders(self) -> List[Dict[str, Any]]:
        return list(self.orders.values())

    def get_inventory(self) -> Dict[str, Dict[str, Any]]:
        return self.inventory

    def get_inventory_for_product(self, product_id: str) -> Dict[str, Any]:
        return self.inventory.get(product_id, {"product_id": product_id, "quantity_on_hand": 0, "reorder_level": 0, "lead_time_days": 0})


data_store = DataStore()
