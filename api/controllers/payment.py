from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models.payment import Payment
from ..schemas.payment import PaymentCreate, PaymentUpdate


def create_payment(db: Session, payment: PaymentCreate):
    """
    Create a new payment.
    """
    try:
        new_payment = Payment(**payment.dict())
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)
        return new_payment
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def get_payments(db: Session):
    """
    Get all payments.
    """
    try:
        return db.query(Payment).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def get_payment_by_id(db: Session, payment_id: int):
    """
    Get a payment by its ID.
    """
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if payment:
        return payment
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Payment with id {payment_id} not found")


def update_payment(db: Session, payment_id: int, payment: PaymentUpdate):
    """
    Update an existing payment.
    """
    try:
        db_payment = db.query(Payment).filter(Payment.id == payment_id).first()
        if not db_payment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Payment with id {payment_id} not found")
        for key, value in payment.dict(exclude_unset=True).items():
            setattr(db_payment, key, value)
        db.commit()
        return db_payment
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def delete_payment(db: Session, payment_id: int):
    """
    Delete a payment by its ID.
    """
    try:
        db_payment = db.query(Payment).filter(Payment.id == payment_id).first()
        if not db_payment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Payment with id {payment_id} not found")
        db.delete(db_payment)

