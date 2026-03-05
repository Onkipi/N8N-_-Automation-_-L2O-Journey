
import requests, json, os

N8N_URL = os.getenv("N8N_URL","http://localhost:5678/api/v1/workflows")
API_KEY = os.getenv("N8N_API_KEY")

headers = {
    "X-N8N-API-KEY": API_KEY,
    "Content-Type": "application/json"
}

with open("../workflows/lead_to_order_workflow.json") as f:
    workflow = json.load(f)

r = requests.post(N8N_URL, headers=headers, json=workflow)
print("Status:", r.status_code)
print(r.text)
