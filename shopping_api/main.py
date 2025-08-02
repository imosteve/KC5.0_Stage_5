from fastapi import FastAPI, Query
from .cart import load_products, add_to_cart, checkout, save_cart

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
def add_item_to_cart(
    product_id: int = Query(..., description="ID of the product"),
    qty: int = Query(..., gt=0, description="Quantity to add")
):
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
def checkout_cart():
    try:
        order = checkout()
        save_cart([])
        return {
            "message": "checkout successful",
            "status": True,
            "data": order
        }
    except Exception as e:
        return {
        "message": str(e),
        "status": False,
        "data": None
        }
