# Task 2: Mini Shopping API with Cart

**Goal:** Create a product API that lets users browse, add to cart, and checkout.

### Features:
- Manage products with `id`, `name`, and `price`.
- Add products to a cart and perform checkout.
- Save cart data to `cart.json`.
- Use the `math` module for rounding prices.

### Endpoints:
- `GET /products/`: View all available products.
- `POST /cart/add?product_id=1&qty=2`: Add items to the cart using query parameters.
- `GET /cart/checkout`: View total cart value and clear cart.
