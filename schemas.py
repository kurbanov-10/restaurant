from pydantic import BaseModel, Field
from decimal import Decimal

class CategoryBase(BaseModel):
    name: str = Field(max_length=100)

class UserCreate(CategoryBase):
    pass

class UserOut(CategoryBase):
    id: int



class Menu_itemBase(BaseModel):
    name: str = Field(max_length=100)
    price: Decimal = Field(max_digits=10, decimal_places=2)
    description: str = Field(max_length=200)
    
class Menu_itemCreate(Menu_itemBase):
    category_id: int

class Menu_itemOut(Menu_itemBase):
    id: int 
    category_id: int
    



class Order_itemBase(BaseModel):
    quantity: int = Field(ge=1, le=100)

    
class Order_itemCreate(Menu_itemBase):
    pass

class Order_itemOut(Menu_itemBase):
    id: int 
    total: Decimal = Field(max_digits=10, decimal_places=2)



class OrderBase(BaseModel):
    address: str = Field(max_digits=200)
    phone_nubmer: str = Field(max_length=20)
    status: str = Field(max_digits=100)
    
class OrderCreate(Menu_itemBase):
    pass

class OrderOut(Menu_itemBase):
    id: int
    menu_item_id: int
    order_id: int 
    total: Decimal = Field(max_digits=10, decimal_places=2)

    
    
