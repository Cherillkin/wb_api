from itertools import product
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="WB_API"
)

class User(BaseModel):
    id_user: int
    login: str
    hash_password: str
    role: str

class Product(BaseModel):
    article: int
    name: str
    amount: int
    price: float

fake_bd_users = [
    {"user_id": 1, "login": "kirill_klim@gmail.com", "hash_password": "32u4ihioh332",    "role": "consumer"},
    {"user_id": 2, "login": "artym_klim@yandex.com", "hash_password": "fwjfioej134",     "role": "consumer"},
    {"user_id": 3, "login": "sergey_nef@list.ru",    "hash_password": "383290ru320ru23", "role": "provider"},
]

@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [
        {"id_user": user["user_id"], "login": user["login"], "hash_password": user["hash_password"], "role": user["role"]}
        for user in fake_bd_users if user.get("user_id") == user_id
    ]

fake_bd_products = [
    {"article": 1, "name": "table",      "amount": 10, "price": 2.50},
    {"article": 2, "name": "detail car", "amount": 18, "price": 6.20},
    {"article": 3, "name": "pen",        "amount": 71, "price": 1.10},
]
@app.get("/products/{product_id}", response_model=List[Product])
def get_thing(article: int):
    return [
        {"article": product["article"], "name": product["name"], "amount": product["amount"], "price": product["price"]}
        for product in fake_bd_products if product.get("article") == article
    ]
