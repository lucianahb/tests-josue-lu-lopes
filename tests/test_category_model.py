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

    @pytest.mark.parametrize("name", [
                                        None, 
                                        5, 
                                        5.0, 
                                        [1, 2, 3],
                                        ('a', 'b', 'c'),
                                        Category('name', 'description'),
                                        {"name":"name"}
                                    ])
    def test_name_not_instance_str(self, name):
        with pytest.raises(TypeError):
            Category(name, 'test description')

    @pytest.mark.parametrize("name", [
        10,
        10.5,
        False
    ])
    def test_name_not_str(self, name):
        with pytest.raises(TypeError):
            category = Category(name, 'description test')

    def test_name_blank_spaces(self):
        with pytest.raises(ValueError):
            category = Category(' ', 'test description')

    def test_name_is_name(self):
        name = 'N'
        category = Category(name, '')
        assert category.name is name

    def test_name_max_len(self):
        with pytest.raises(ValueError):
            category = Category('test name'*100, 'test description')

    def test_description_is_description(self):
        description = ''
        category = Category('N', description)
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
