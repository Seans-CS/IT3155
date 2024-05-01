from . import orders, order_details, customer, customer_review,Restaurant


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(customer.router)
    app.include_router(customer_review.router)
    app.include_router(Restaurant.router)

