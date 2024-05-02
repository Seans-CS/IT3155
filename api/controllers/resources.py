from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models.resources import Resource as model
from ..schemas.resources import ResourceCreate, ResourceUpdate
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, resource: ResourceCreate):
    new_resource = model(
        item=resource.item,
        amount=resource.amount
    )
    try:
        db.add(new_resource)
        db.commit()
        db.refresh(new_resource)
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_resource


def read_all(db: Session):
    try:
        result = db.query(model).all()
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, resource_id: int):
    try:
        item = db.query(model).filter(model.id == resource_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found!")
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, resource_id: int, resource: ResourceUpdate):
    try:
        item = db.query(model).filter(model.id == resource_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found!")

        update_data = resource.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(item, key, value)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def delete(db: Session, resource_id: int):
    try:
        item = db.query(model).filter(model.id == resource_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found!")
        db.delete(item)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)