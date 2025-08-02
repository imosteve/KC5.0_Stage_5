import json
import os
from pydantic import BaseModel
from typing import List

PRODUCT_FILE = "shopping_api/data/products.json"
CART_FILE = "shopping_api/data/carts.json"

class Product(BaseModel):
    id: int
    name: str
    price: float

def load_products() -> List[Product]:
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

    for product in products:
        if product["id"] == product_id:
            
            for item in carts:
                if item["id"] == product_id:
                    item["quantity"] += qty
                    save_cart(carts)
                    return item

            order = {"id": product['id'], "name": product['name'], "quantity": qty, "price": product['price']}

            carts.append(order)
            save_cart(carts)
            return order

def checkout():
    carts = load_cart()
    