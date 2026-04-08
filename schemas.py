from pydantic import BaseModel, Field
from decimal import Decimal

class CategoryBase(BaseModel):
    name: str = Field(max_length=100)

class CategoryCreate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int



class MenuItemBase(BaseModel):
    name: str = Field(max_length=100)
    price: Decimal = Field(gt=0, decimal_places=2)
    description: str = Field(max_length=200)
    
class MenuItemCreate(MenuItemBase):
    category_id: int

class MenuItemOut(MenuItemBase):
    id: int 
    category_id: int
    



class OrderItemBase(BaseModel):
    quantity: int = Field(ge=1, le=100)
    total: Decimal = Field(max_digits=10, decimal_places=2)
    
    

class OrderItemCreate(OrderItemBase):
    order_id: int
    menu_item_id: int

class OrderItemOut(OrderItemBase):
    id: int 
    order_id: int
    menu_item_id: int
    



class OrderBase(BaseModel):
    address: str = Field(max_length=200)
    phone_nubmer: str = Field(max_length=20)
    status: str = Field(max_length=100)
    
class OrderCreate(OrderBase):
    pass

class OrderOut(OrderBase):
    id: int
    total: Decimal = Field(max_digits=10, decimal_places=2)

    
    
