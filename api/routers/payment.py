from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import payments as payment_controller
from ..schemas import payments as payment_schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Payments'],
    prefix="/payments"
)

@router.post("/", response_model=payment_schema.Payment)
def create_payment(request: payment_schema.PaymentCreate, db: Session = Depends(get_db)):
    return payment_controller.create(db=db, request=request)

@router.get("/", response_model=list[payment_schema.Payment])
def read_all_payments(db: Session = Depends(get_db)):
    return payment_controller.read_all(db)

@router.get("/{item_id}", response_model=payment_schema.Payment)
def read_one_payment(item_id: int, db: Session = Depends(get_db)):
    return payment_controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=payment_schema.Payment)
def update_payment(item_id: int, request: payment_schema.PaymentUpdate, db: Session = Depends(get_db)):
    return payment_controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}")
def delete_payment(item_id: int, db: Session = Depends(get_db)):
    return payment_controller.delete(db=db, item_id=item_id)
