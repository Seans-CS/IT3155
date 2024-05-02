from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models.menu_items import MenuItems as model
from ..schemas.menu_items import MenuItemsCreate, MenuItemsUpdate
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, menu_items: MenuItemsCreate):
    new_item = menu_items.MenuItems(
        dish_name=menu_items.dish_name,
        price=menu_items.price,
        calories=menu_items.calories,
        food_categories=menu_items.food_categories,
        recipe_id=menu_items.recipe_id,
        recipe_name=menu_items.recipe_name,
        ingredients=menu_items.ingredients
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
        result = db.query(model).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, menu_id: int):
    try:
        item = db.query(model).filter(model.id == menu_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, menu_id: int, menu_items: MenuItemsUpdate):
    try:
        item = db.query(model).filter(model.id == menu_id).first()
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = menu_items.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, menu_id: int):
    try:
        item = db.query(model).filter(model.id == menu_id).first()
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)