from __future__ import annotations

from typing import Any, Dict, List

from app.data.store import data_store
from app.services.finance_service import FinanceService


class ResearchAgent:
    def __init__(self) -> None:
        self.store = data_store

    def find_opportunities(self, category: str, max_cost: float = 5.0, target_margin: float = 0.4, max_results: int = 3) -> Dict[str, Any]:
        candidates = []
        for product in self.store.products:
            if product["category"] != category and category != "all":
                continue
            if float(product["buy_price"]) > max_cost:
                continue

            metrics = FinanceService.calculate_net_profit(product, quantity=1)
            margin = metrics.profit_margin
            if margin < target_margin:
                continue

            candidates.append(
                {
                    "product_id": product["id"],
                    "name": product["name"],
                    "category": product["category"],
                    "buy_price": product["buy_price"],
                    "suggested_price": product["suggested_price"],
                    "estimated_margin": round(margin, 4),
                    "estimated_net_profit": round(metrics.net_profit, 2),
                    "reason": "Strong margin and lightweight supply profile.",
                }
            )

        ranked = sorted(candidates, key=lambda x: x["estimated_margin"], reverse=True)[:max_results]
        return {
            "category": category,
            "target_margin": target_margin,
            "max_cost": max_cost,
            "opportunities": ranked,
        }
