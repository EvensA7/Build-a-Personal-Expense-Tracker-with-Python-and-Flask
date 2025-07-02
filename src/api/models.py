from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name = Mapped[str](String(100), nullable=False)
    picture: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    expenses=relationship("Expense", back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "picture": self.picture,
            "email": self.email,
            "is_active": self.is_active
        }
    

class Expense(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    transaction_date: Mapped[datetime] = mapped_column(nullable=False)
    transaction_category: Mapped[str] = mapped_column(String(120), unique=False, nullable=False)
    transaction_description: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    transaction_currency: Mapped[str] = mapped_column(String(120), unique=False, nullable=False)
    transaction_amount: Mapped[Float] = mapped_column(nullable=False)
    is_recurring: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    expenses=relationship("User", back_populates="expense")

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    user=relationship("User", back_populates="expense")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "transaction_date": self.transaction_date,
            "transaction_category": self.transaction_category,
            "transaction_description": self.transaction_description,
            "transaction_currency": self.transaction_currency,
            "transaction_amount": self.transaction_price,
            "is_recurring": self.is_recurring,
            "is_active": self.is_active
        }