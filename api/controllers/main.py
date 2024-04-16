from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import customer as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_item = model.Restaurant(
        name=request.name,
        menu=request.menu,
        promotions=request.promotions
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.Restaurant).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result