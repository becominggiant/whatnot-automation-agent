from __future__ import annotations

from typing import Any, Dict

from app.agents.finance_agent import FinanceAgent
from app.agents.inventory_agent import InventoryAgent
from app.agents.order_agent import OrderAgent
from app.agents.research_agent import ResearchAgent


class Orchestrator:
    def __init__(self) -> None:
        self.inventory_agent = InventoryAgent()
        self.order_agent = OrderAgent()
        self.finance_agent = FinanceAgent()
        self.research_agent = ResearchAgent()

    async def route_task(self, task_type: str, data: Dict[str, Any]) -> Dict[str, Any]:
        task_type = (task_type or "inventory").lower()

        if task_type == "inventory":
            product_id = data.get("product_id")
            quantity = int(data.get("quantity_needed", 1))
            return self.inventory_agent.check_stock(product_id, quantity)

        if task_type == "order":
            order_id = data.get("order_id")
            return self.order_agent.get_order_status(order_id)

        if task_type == "research":
            return self.research_agent.find_opportunities(
                category=data.get("category", "all"),
                max_cost=float(data.get("max_cost", 5.0)),
                target_margin=float(data.get("target_margin", 0.4)),
                max_results=int(data.get("max_results", 3)),
            )

        if task_type == "finance":
            return self.finance_agent.calculate_product_profit(
                data.get("product_id"),
                quantity=int(data.get("quantity", 1)),
            )

        return {
            "task_type": task_type,
            "status": "unknown_task",
            "message": "Task type not recognized. Supported: inventory, order, research, finance.",
        }
