from pydantic import BaseModel
from typing import List, Optional
from .recipes import Recipe
from .resources import Resource


class menuItemsBase(BaseModel):
    dish_name: str
    price: float
    calories: int
    food_categories: str


class MenuItemsCreate(menuItemsBase):
    recipe_id: int


class MenuItemsUpdate(menuItemsBase):
    dish_name: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    food_categories: Optional[str] = None
    recipe_id: Optional[int] = None


class MenuItem(menuItemsBase):
    id: int
    recipe: Optional[Recipe]
    ingredients: Optional[List[Resource]]

    class Config:
        orm_mode = True