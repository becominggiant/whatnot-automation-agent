from __future__ import annotations

from typing import Any, Dict

from app.data.store import data_store


class OrderAgent:
    def __init__(self) -> None:
        self.store = data_store

    def get_order_status(self, order_id: str) -> Dict[str, Any]:
        order = self.store.orders.get(order_id)
        if not order:
            return {"order_id": order_id, "status": "not_found", "message": "Order not found"}

        product = self.store.get_product(order["product_id"])
        return {
            "order_id": order_id,
            "product_id": order["product_id"],
            "product_name": product["name"],
            "status": order["status"],
            "payment_status": order["payment_status"],
            "shipping_status": order["shipping_status"],
            "next_action": self._suggest_next_action(order),
        }

    def _suggest_next_action(self, order: Dict[str, Any]) -> str:
        if order["status"] == "pending":
            return "Validate payment and reserve stock before fulfillment."
        if order["status"] == "shipped":
            return "Track delivery and confirm customer receipt."
        return "No action needed unless a customer question or refund request is logged."
