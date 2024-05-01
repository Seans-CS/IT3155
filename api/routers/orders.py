from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import orders as order_controller
from ..schemas import orders as order_schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)

@router.post("/", response_model=order_schema.Order)
def create_order(request: order_schema.OrderCreate, db: Session = Depends(get_db)):
    return order_controller.create(db=db, request=request)

@router.get("/", response_model=list[order_schema.Order])
def read_all_orders(db: Session = Depends(get_db)):
    return order_controller.read_all(db)

@router.get("/{item_id}", response_model=order_schema.Order)
def read_one_order(item_id: int, db: Session = Depends(get_db)):
    return order_controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=order_schema.Order)
def update_order(item_id: int, request: order_schema.OrderUpdate, db: Session = Depends(get_db)):
    return order_controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}")
def delete_order(item_id: int, db: Session = Depends(get_db)):
    return order_controller.delete(db=db, item_id=item_id)
