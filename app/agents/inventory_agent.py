from __future__ import annotations

from typing import Any, Dict, List

from app.data.store import data_store
from app.services.finance_service import FinanceService


class InventoryAgent:
    def __init__(self) -> None:
        self.store = data_store

    def check_stock(self, product_id: str, quantity_needed: int = 1) -> Dict[str, Any]:
        product = self.store.get_product(product_id)
        inventory = self.store.get_inventory_for_product(product_id)
        quantity_on_hand = int(inventory.get("quantity_on_hand", 0))
        reorder_level = int(inventory.get("reorder_level", 0))

        if quantity_on_hand >= quantity_needed:
            return {
                "product_id": product_id,
                "product_name": product["name"],
                "status": "stock_ok",
                "quantity_on_hand": quantity_on_hand,
                "quantity_needed": quantity_needed,
                "recommendation": "No reorder needed.",
            }

        metrics = FinanceService.calculate_net_profit(product, quantity=quantity_needed)
        return {
            "product_id": product_id,
            "product_name": product["name"],
            "status": "low_stock",
            "quantity_on_hand": quantity_on_hand,
            "quantity_needed": quantity_needed,
            "reorder_level": reorder_level,
            "recommended_action": "reorder",
            "estimated_profit_if_reordered": round(metrics.net_profit, 2),
            "recommendation": "Inventory is below the required threshold. Reorder or slow down promotion volume.",
        }

    def get_all_inventory(self) -> List[Dict[str, Any]]:
        output = []
        for product_id, inventory in self.store.get_inventory().items():
            product = self.store.get_product(product_id)
            output.append(
                {
                    "product_id": product_id,
                    "product_name": product["name"],
                    "quantity_on_hand": inventory["quantity_on_hand"],
                    "reorder_level": inventory["reorder_level"],
                    "lead_time_days": inventory["lead_time_days"],
                    "status": "low" if inventory["quantity_on_hand"] <= inventory["reorder_level"] else "ok",
                }
            )
        return output
