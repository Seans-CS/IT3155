from . import orders, order_details, recipes, sandwiches, resources, customer, customer_review, main, payment, promotions, menu_items

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    customer.Base.metadata.create_all(engine)
    customer_review.Base.metadata.create_all(engine)
    main.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)

