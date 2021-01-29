import sys
sys.path.append('.')

from models.categories import Category
from models.base_model import BaseModel
import pytest

class TestCategoryModel:
    @pytest.mark.parametrize("name, description", [
        ('N',''), 
        ('N'*100, 'D'*200), 
        ('N' * 50,'D' * 120),
        ('N' * 45,'D' * 120)
    ])
    def test_category_instance(self, name, description):
        category = Category(name, description)
        assert isinstance(category, Category)
        assert isinstance(category, BaseModel)

    def test_name_isinstance_str(self):
        with pytest.raises(TypeError):
            category = Category(None, 'test description')

    @pytest.mark.parametrize("name, description", [
        (10, 'Melhor time do Brasil'),
        (10.5, 'Melhor time do Brasil'),
        (False, 'Melhor time do Brasil')
    ])
    def test_name_not_str(self, name, description):
        with pytest.raises(TypeError):
            category = Category(name, description)

    def test_name_blank_spaces(self):
        with pytest.raises(ValueError):
            category = Category(' ', 'test description')

    def test_name_min_len(self):
        name = 'N'
        description = ''
        category = Category(name, description)
        assert category.name is name

    def test_name_max_len(self):
        with pytest.raises(ValueError):
            category = Category('test name'*100, 'test description')

    def test_description_min_len(self):
        name = 'N'
        description = ''
        category = Category(name, description)
        assert category.description is description

    def test_description_not_none(self):
        with pytest.raises(TypeError):
            category = Category('test name', None)

    def test_description_not_str(self):
        with pytest.raises(TypeError):
            category = Category('test name', 10)

    def test_description_len(self):
        with pytest.raises(ValueError):
            category = Category('test name', 'test description'*250)
