from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from sqlalchemy.orm import Session
from ..schemas.menu_items import MenuItemsCreate, MenuItemsUpdate, MenuItem
from ..controllers import menu_items as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Menu Items'],
    prefix="/menu_items"
)


@router.post("/", response_model=MenuItem)
def create_menu_item(request: MenuItemsCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, menu_items=request)


@router.get("/", response_model=List[MenuItem])
def read_all_menu_items(db: Session = Depends(get_db)):
    return controller.read_all(db=db)


@router.get("/{item_id}", response_model=MenuItem)
def read_one_menu_item(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, menu_id=item_id)


@router.put("/{item_id}", response_model=MenuItem)
def update_menu_item(item_id: int, request: MenuItemsUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, menu_id=item_id, menu_items=request)


@router.delete("/{item_id}")
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, menu_id=item_id)