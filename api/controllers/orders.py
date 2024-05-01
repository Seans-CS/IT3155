from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.orders import Order
from ..schemas.orders import OrderCreate, OrderUpdate

def create_order(db: Session, order: OrderCreate):
    """
    Create a new order.
    """
    try:
        new_order = Order(**order.dict())
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        return new_order
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

def get_orders(db: Session):
    """
    Get all orders.
    """
    try:
        return db.query(Order).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

def get_order_by_id(db: Session, order_id: int):
    """
    Get an order by its ID.
    """
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        return order
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with id {order_id} not found")

def update_order(db: Session, order_id: int, order: OrderUpdate):
    """
    Update an existing order.
    """
    try:
        db_order = db.query(Order).filter(Order.id == order_id).first()
        if not db_order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with id {order_id} not found")
        for key, value in order.dict(exclude_unset=True).items():
            setattr(db_order, key, value)
        db.commit()
        return db_order
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

def delete_order(db: Session, order_id: int):
    """
    Delete an order by its ID.
    """
    try:
        db_order = db.query(Order).filter(Order.id == order_id).first()
        if not db_order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with id {order_id} not found")
        db.delete(db_order)
        db.commit()
        return {"message": f"Order with id {order_id} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
