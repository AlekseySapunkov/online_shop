from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.createDB import Base  # Импорт базового класса

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True, nullable=False)
    description = Column(String(500))
    price = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'), index=True)

    # Связь с моделью User
    owner = relationship("User", back_populates="products")