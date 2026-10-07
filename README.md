# Whatnot Automation MVP

This repository is a lightweight operations automation starter for a Whatnot business. It includes a multi-agent backend that covers:

- Inventory monitoring
- Order status guidance
- Research and sourcing opportunities
- Finance and pricing analysis
- Orchestration across all AI tasks

## Stack

- Python
- FastAPI
- Pydantic
- OpenAI API

## Basic project structure

- app/main.py
- app/api/routes.py
- app/agents/
- app/services/
- app/data/store.py

## Quick start

1. Create a virtual environment:

   python -m venv .venv
   source .venv/bin/activate

2. Install dependencies:

   pip install -r requirements.txt

3. Set your environment variables:

   cp .env.example .env

4. Run the app:

   uvicorn app.main:app --reload

## Example requests

Inventory check:

curl -X POST http://localhost:8000/inventory/check \
  -H "Content-Type: application/json" \
  -d '{"product_id":"sku-1001","quantity_needed":12}'

Order status:

curl -X POST http://localhost:8000/orders/status \
  -H "Content-Type: application/json" \
  -d '{"order_id":"ord-001"}'

Research opportunities:

curl -X POST http://localhost:8000/research/source \
  -H "Content-Type: application/json" \
  -d '{"category":"phone accessories","max_cost":5.0,"target_margin":0.4,"max_results":3}'

Profit estimate:

curl -X POST http://localhost:8000/finance/profit \
  -H "Content-Type: application/json" \
  -d '{"product_id":"sku-1001","quantity":4}'

## Current maturity

This is intentionally an MVP. It is built as an operational foundation, not a full production ERP. The goal is to give you a real starting point for:

- product sourcing decisions
- stock alerts
- margin tracking
- order flow triage
- business orchestration

## Recommended next steps

- Swap the in-memory sample store for PostgreSQL
- Add real supplier and shipping APIs
- Add human approval thresholds for risky finance choices
- Add authentication and admin routes
- Expand each agent into separate services and workflows
