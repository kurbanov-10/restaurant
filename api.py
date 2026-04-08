from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas import CategoryCreate, CategoryOut,MenuItemCreate,MenuItemOut,OrderItemCreate,OrderItemOut
from database import Base, get_db, engine
from models import Base, Category, MenuItem, OrderItem
from typing import List

Base.metadata.create_all(bind=engine)
api_router = APIRouter(prefix='/api/restaurants')

@api_router.post('/categoreas', response_model=CategoryOut)
def create_category(category_in: CategoryCreate, db: Session = Depends(get_db)):
    category = Category(**category_in.model_dump())

    db.add(category)
    db.commit()
    db.refresh(category)

    return category

@api_router.get('/categoreas', response_model=List[CategoryOut])
def get_categories(db = Depends(get_db)):
    stmt = select(Category)
    categories = db.scalars(stmt).all()
    
    if not categories:
        raise HTTPException(status_code=404, detail="mavjud emas")
    
    return categories

@api_router.post('/MenuItem', response_model=MenuItemOut)
def create_menuItem(menuItem_in: MenuItemCreate, db: Session = Depends(get_db)):
    stmt = select(Category).where(Category.id == menuItem_in.category_id)
    category = db.scalar(stmt)

    if not category:
        raise HTTPException(status_code=404, detail=f"{menuItem_in.category_id}-raqamli category mavjud emas")

    menuItem = MenuItem(**menuItem_in.model_dump())

    db.add(menuItem)
    db.commit()
    db.refresh(menuItem)

    return menuItem

@api_router.get('/MenuItem', response_model=List[MenuItemOut])
def get_menuItem(db = Depends(get_db)):
    stmt = select(MenuItem)
    menuItem = db.scalars(stmt).all()
    
    if not menuItem:
        raise HTTPException(status_code=404, detail="mavjud emas")
    
    return menuItem

@api_router.get('/MenuItem/{post_id}', response_model=MenuItemOut)
def get_MenuItem(MenuItem_id: int, db = Depends(get_db)):
    stmt = select(MenuItem).where(MenuItem.id == MenuItem_id)
    post = db.scalar(stmt)

    if not post:
        raise HTTPException(status_code=404, detail=f"{MenuItem_id}-raqamli mavjud emas")

    return post

@api_router.post('/OrderItem', response_model=OrderItemOut)
def create_orderItem(orderItem_in: OrderItemCreate, db: Session = Depends(get_db)):
    stmt = select(MenuItem).where(MenuItem.id == orderItem_in.menu_item_id)
    orderItem = db.scalar(stmt)

    if not orderItem:
        raise HTTPException(status_code=404, detail=f"{orderItem_in.menu_item_id}-raqamli mavjud emas")

    orderItem = OrderItem(**orderItem_in.model_dump())

    db.add(orderItem)
    db.commit()
    db.refresh(orderItem)

    return orderItem


@api_router.get('/OrderItem', response_model=List[OrderItemOut])
def get_OrderItem(db = Depends(get_db)):
    stmt = select(OrderItem)
    menuItem = db.scalars(stmt).all()
    
    if not menuItem:
        raise HTTPException(status_code=404, detail="mavjud emas")
    
    return menuItem

@api_router.put('/OrderItem/{orderItem_id}', response_model=OrderItemOut)
def update_orderItem(orderItem_id: int, orderItem_in: OrderItemCreate, db: Session = Depends(get_db)):
    stmt = select(OrderItem).where(OrderItem.id == orderItem_id)
    orderItem = db.scalar(stmt)

    if not orderItem:
        raise HTTPException(status_code=404, detail=f"{orderItem_id}-raqamli mavjud emas")

    orderItem.quantity = orderItem_in.quantity
    orderItem.total = orderItem_in.total
    

    db.commit()
    db.refresh(orderItem)

    return orderItem

@api_router.delete('/OrderItem/{orderItem_id}', response_model=OrderItemOut)
def delete_orderItem(orderItem_id: int, db: Session = Depends(get_db)):
    stmt = select(OrderItem).where(OrderItem.id == orderItem_id)
    orderItem = db.scalar(stmt)

    if not orderItem:
        raise HTTPException(status_code=404, detail=f"{orderItem_id}-raqamli mavjud emas")

    db.delete(orderItem)
    db.commit()

    return orderItem
