from models.category import Category
from .session import Session

class CategoryDao:
    def save(self, model: Category) -> Category:
        with Session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
        return model

    def read_by_id(self, id_: int) -> Category:
        if isinstance(id_, int):
            with Session() as session:
                result = session.query(Category).filter_by(id=id_).first()
            return result
        else:
            raise TypeError('Id mut be integer')

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(Category).order_by('id').all()
        return result

    def delete(self, model: Category) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()