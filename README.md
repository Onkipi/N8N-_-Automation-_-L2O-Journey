
# Enterprise Lead-to-Order Automation (n8n)

Production-ready workflow demonstrating Lead → Qualification → Proposal → Order → Notification.

## Import Workflow

1. Open n8n UI
2. Go to Workflows → Import
3. Upload workflows/lead_to_order_workflow.json

## Deploy via API

pip install requests

export N8N_API_KEY=your_key

python scripts/deploy_workflow.py
