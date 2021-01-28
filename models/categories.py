from sqlalchemy import Column, String
from models.base_model import BaseModel
from sqlalchemy.orm  import validates


class Category(BaseModel):
    __tablename__ = "CATEGORIES"
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=200), nullable=True)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validates_name(self, key, name: str) -> str:
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        if not name.strip():
            raise ValueError('Name can not be empty')
        if len(name) > 100:
            raise ValueError('Name is too big')
        return name

    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError('Description must be a string')
        if len(description) > 150:
            raise ValueError('Description is bigger than 150 characters')
        return description
