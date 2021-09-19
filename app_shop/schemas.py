from datetime import datetime
from typing import List

from pydantic import BaseModel


########################################## Покупатели
class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    created_on: datetime
    updated_on: datetime


class CustomerCreate(CustomerBase):
    password: str


class Customer(CustomerBase):
    id: int
    orders: List["Order"] = []


    class Config:
        orm_mode = True

########################################## Товар
class ItemBase(BaseModel):
    name: str
    cost_price: float
    selling_price: float
    quantity: int


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int


    class Config:
        orm_mode = True


########################################### Заказы(дата)
class OrderBase(BaseModel):
    date_placed: datetime


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    customer_id: int
    line_items: List["OrderItem"] = []


    class Config:
        orm_mode = True


########################################### Заказ - Товар(кол-во)
class OrderItemBase(BaseModel):
    quantity: int


class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    id: int
    order_id: int
    item_id: int
    item: List[Item] = []


    class Config:
        orm_mode = True

