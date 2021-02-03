from dao.category_dao import CategoryDao
from models.category import Category


class CategoryController:
    def __init__(self):
        self.__dao = CategoryDao()

    def create(self, model: Category) -> Category:
        self.__dao.save(model)
    
    def update(self, model: Category) -> Category:
        self.__dao.read_by_id(model.id)
        return self.__dao.save(model)
    
    def read_by_id(self, id_:int) -> Category:
        result = self.__dao.read_by_id(id_)
        if result:
            return result
        raise Exception('Object not found in database')
    
    def read_all(self) -> list:
        return self.__dao.read_all()
    
    def delete(self, model: Category) -> None:
        self.__dao.delete(model)
        