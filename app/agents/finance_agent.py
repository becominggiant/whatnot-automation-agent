from __future__ import annotations

from typing import Any, Dict

from app.data.store import data_store
from app.services.finance_service import FinanceService


class FinanceAgent:
    def __init__(self) -> None:
        self.store = data_store

    def calculate_product_profit(self, product_id: str, quantity: int = 1) -> Dict[str, Any]:
        product = self.store.get_product(product_id)
        metrics = FinanceService.calculate_net_profit(product, quantity=quantity)

        payload = {
            "product_id": product_id,
            "product_name": product["name"],
            "quantity": quantity,
            "gross_revenue": round(metrics.gross_revenue, 2),
            "platform_fee": round(metrics.platform_fee, 2),
            "product_cost": round(metrics.product_cost, 2),
            "shipping_cost": round(metrics.shipping_cost, 2),
            "packaging_cost": round(metrics.packaging_cost, 2),
            "net_profit": round(metrics.net_profit, 2),
            "profit_margin": round(metrics.profit_margin, 4),
            "recommendation": self._recommendation(metrics.profilt_margin if hasattr(metrics, 'profilt_margin') else metrics.profit_margin),
        }
        return payload

    def _recommendation(self, margin: float) -> str:
        if margin >= 0.45:
            return "Strong margin. Maintain or expand volume."
        if margin >= 0.3:
            return "Healthy margin. Monitor buyer acquisition and shipping costs."
        if margin >= 0.15:
            return "Tight margin. Consider price adjustment or lower-cost sourcing."
        return "Low-margin product. Reprice, discontinue, or renegotiate supplier cost."
