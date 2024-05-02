from . import orders, order_details, customer, customer_review,Restaurant, menu_items, resources


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(customer.router)
    app.include_router(customer_review.router)
    app.include_router(Restaurant.router)
    app.include_router(menu_items.router)
    app.include_router(resources.router)