from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from sqlalchemy.orm import Session
from ..schemas.resources import ResourceCreate, ResourceUpdate, Resource
from ..controllers import resources as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Resources'],
    prefix="/resources"
)


@router.post("/", response_model=Resource)
def create_resource(request: ResourceCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, resource=request)


@router.get("/", response_model=List[Resource])
def read_all_resources(db: Session = Depends(get_db)):
    return controller.read_all(db=db)


@router.get("/{resource_id}", response_model=Resource)
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, resource_id=resource_id)

@router.put("/{resource_id}", response_model=Resource)
def update_resource(resource_id: int, request: ResourceUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, resource_id=resource_id, resource=request)


@router.delete("/{resource_id}")
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, resource_id=resource_id)