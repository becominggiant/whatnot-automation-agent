from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.agents.orchestrator import Orchestrator

router = APIRouter()
_orchestrator = Orchestrator()


class InventoryCheckRequest(BaseModel):
    product_id: str
    quantity_needed: int = Field(default=1)


class OrderStatusRequest(BaseModel):
    order_id: str


class ResearchRequest(BaseModel):
    category: str = "home goods"
    max_cost: float = 5.0
    target_margin: float = 0.4
    max_results: int = 3


class FinanceRequest(BaseModel):
    product_id: str
    quantity: int = 1


@router.get("/inventory")
async def list_inventory() -> dict:
    return {"inventory": _orchestrator.inventory_agent.get_all_inventory()}


@router.post("/inventory/check")
async def check_inventory(payload: InventoryCheckRequest) -> dict:
    result = _orchestrator.inventory_agent.check_stock(payload.product_id, payload.quantity_needed)
    return result


@router.post("/orders/status")
async def status_for_order(payload: OrderStatusRequest) -> dict:
    result = _orchestrator.order_agent.get_order_status(payload.order_id)
    return result


@router.post("/research/source")
async def source_products(payload: ResearchRequest) -> dict:
    result = _orchestrator.research_agent.find_opportunities(
        category=payload.category,
        max_cost=payload.max_cost,
        target_margin=payload.target_margin,
        max_results=payload.max_results,
    )
    return result


@router.post("/finance/profit")
async def estimate_profit(payload: FinanceRequest) -> dict:
    result = _orchestrator.finance_agent.calculate_product_profit(payload.product_id, payload.quantity)
    return result


@router.post("/agent/route")
async def route_task(payload: dict) -> dict:
    task_type = payload.get("task_type", "inventory")
    data = payload.get("data", {})
    return await _orchestrator.route_task(task_type, data)
