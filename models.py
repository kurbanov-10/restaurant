from sqlalchemy import String, Integer, ForeignKey,CHAR, DECIMAL,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from database import Base

class Category(Base):
    __tablename__='categories'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=100))
    

    menu_items: Mapped[list['MenuItem']] = relationship(back_populates='category',
                                         cascade='all, delete-orphan')
    
class MenuItem(Base):
    __tablename__ = 'menu_items'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=100))
    price: Mapped[DECIMAL] = mapped_column(Numeric(precision=10, scale=2))
    description: Mapped[str] = mapped_column(String(length=200))
    
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category: Mapped['Category'] = relationship(back_populates='menu_items')
    

    order_items: Mapped[list['OrderItem']] = relationship(back_populates='menu_item')
      
class OrderItem(Base):
    __tablename__ = 'order_items'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer)
    total: Mapped[DECIMAL] = mapped_column(Numeric(10,2))

    menu_item_id: Mapped[int] = mapped_column(ForeignKey('menu_items.id'))
    menu_item: Mapped['MenuItem'] = relationship(back_populates='order_items')
    
    
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'))
    order: Mapped['Order'] = relationship(back_populates='order_items')
    

    
class Order(Base):
    __tablename__ = 'orders'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address: Mapped[str] = mapped_column(String(length=200))
    total: Mapped[DECIMAL] = mapped_column(Numeric(10,2))
    phone_nubmer: Mapped[CHAR] = mapped_column(CHAR)
    status: Mapped[str] = mapped_column(String(length=100))
    
    order_items: Mapped[OrderItem] = relationship(back_populates='order')