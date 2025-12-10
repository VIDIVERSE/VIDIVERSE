#!/usr/bin/env python3
import sys
import json
from pathlib import Path

ORDERS_FILE = Path("orders.json")

def save_order(order_data):
    # Falls Datei existiert, alte Bestellungen laden
    if ORDERS_FILE.exists():
        with open(ORDERS_FILE, "r", encoding="utf-8") as f:
            try:
                orders = json.load(f)
            except json.JSONDecodeError:
                orders = []
    else:
        orders = []

    # Neue Bestellung hinzufügen
    orders.append(order_data)

    # Datei speichern
    with open(ORDERS_FILE, "w", encoding="utf-8") as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    try:
        # JSON von stdin lesen
        raw_input = sys.stdin.read()
        order = json.loads(raw_input)
        save_order(order)
        print(json.dumps({"status": "success"}))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)