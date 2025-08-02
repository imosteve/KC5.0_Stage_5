from fastapi import FastAPI
from .cart import load_products, add_to_cart

app = FastAPI()


@app.get('/products/')
def list_products():
    products = load_products()
    return {
        "message": "products fetched successfully",
        "status": True,
        "data": products
    }

@app.post('/cart/add')
def add_item_to_cart(product_id: int, qty: int):
    try:
        order = add_to_cart(product_id, qty)
        return {
            "message": "item added to cart",
            "status": True,
            "data": order
        }
    except Exception as e:
        return {
        "message": str(e),
        "status": False,
        "data": None
        }

@app.get('/cart/checkout')
def list_products():
    return {"message": "cart checked out successfully"}