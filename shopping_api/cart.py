import json
import os
from pydantic import BaseModel
import math

PRODUCT_FILE = "shopping_api/data/products.json"
CART_FILE = "shopping_api/data/carts.json"

class Product(BaseModel):
    id: int
    name: str
    price: float

def load_products():
    if not os.path.exists(PRODUCT_FILE):
        return []
    with open(PRODUCT_FILE, 'r') as f:
        products = json.load(f)
        return products

def load_cart():
    if not os.path.exists(CART_FILE):
        return []
    with open(CART_FILE, 'r') as f:
        return json.load(f)
    
def save_cart(carts):
    with open(CART_FILE, 'w') as f:
        return json.dump(carts, f, indent=4)


def add_to_cart(product_id: int, qty: int):
    products = load_products()
    carts = load_cart()

    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        raise ValueError(f"Product with id {product_id} not found.")

    for item in carts:
        if item["id"] == product_id:
            item["quantity"] += qty
            break
    else:
        item = {
            "id": product['id'],
            "name": product['name'],
            "quantity": qty,
            "price": product['price']
        }
        carts.append(item)

    save_cart(carts)
    return item

def checkout():
    carts = load_cart()
    if not carts:
        raise ValueError("No item in cart")
    total = sum(item['price'] * item['quantity'] for item in carts)
    total = math.ceil(total * 100) / 100
    return {
        "carts": carts,
        "total": total
    }
