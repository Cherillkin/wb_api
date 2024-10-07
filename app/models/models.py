from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, JSON, TIMESTAMP, ForeignKey, Float, Boolean

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("role_id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permission", JSON),
)

user = Table(
    "user",
    metadata,
    Column("user_id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey(role.c.role_id)),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)

product = Table(
    "product",
    metadata,
    Column("article", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("amount", Integer, nullable=False),
    Column("price", Float, nullable=False)
)