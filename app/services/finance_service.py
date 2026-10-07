from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FinanceMetrics:
    gross_revenue: float
    platform_fee: float
    product_cost: float
    shipping_cost: float
    packaging_cost: float
    net_profit: float
    profit_margin: float


class FinanceService:
    @staticmethod
    def calculate_net_profit(product: dict, quantity: int = 1) -> FinanceMetrics:
        sell_price = float(product.get("suggested_price", 0.0))
        buy_price = float(product.get("buy_price", 0.0))
        shipping_cost = float(product.get("shipping_cost", 0.0))
        packaging_cost = float(product.get("packaging_cost", 0.0))
        platform_fee_pct = float(product.get("platform_fee_pct", 0.08))

        gross_revenue = sell_price * quantity
        product_cost = buy_price * quantity
        shipping_total = shipping_cost * quantity
        packaging_total = packaging_cost * quantity
        platform_fee = gross_revenue * platform_fee_pct

        net_profit = gross_revenue - product_cost - shipping_total - packaging_total - platform_fee
        profit_margin = (net_profit / gross_revenue) if gross_revenue else 0.0

        return FinanceMetrics(
            gross_revenue=gross_revenue,
            platform_fee=platform_fee,
            product_cost=product_cost,
            shipping_cost=shipping_total,
            packaging_cost=packaging_total,
            net_profit=net_profit,
            profit_margin=profit_margin,
        )
