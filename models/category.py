from sqlalchemy import Column, String
from models.base_model import BaseModel
from sqlalchemy.orm import validates
from utils.validators import ValidateModel


class Category(BaseModel):
    __tablename__ = "CATEGORY"
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=255), nullable=True)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validates_name(self, key, name: str) -> str:
        v = ValidateModel()
        name = v.validate_type(name, str, key)
        name = v.validate_not_empty(name, key)
        return v.validate_len(name, 100, key)

    @validates('description')
    def validate_description(self, key, description):
        v = ValidateModel()
        description = v.validate_type(description, str, key)
        return v.validate_len(description, 200, key)
