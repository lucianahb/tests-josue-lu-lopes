from models.categories import Category
from models.base_model import BaseModel
import pytest


class TestModels:
    @pytest.mark.parametrize("name, description", [
        ('test name', 'test description'),
        ('t', ''),
        ('t' * 100, 't' * 200)
    ])
    def test_category_instance(self, name, description):
        test_instance = Category(name, description)
        assert isinstance(test_instance, Category)
        assert isinstance(test_instance, BaseModel)

    def test_category_args(self):
        name = 'test name'
        description = 'test description'
        test_instance = Category(name, description)
        assert test_instance.name is name
        assert test_instance.description is description

    @pytest.mark.parametrize("name", [
        None, 5, 5.0, [1, 2, 3],
        ('a', 'b', 'c'),
        Category('name', 'description'),
        {'name': 'test name',
         'description': 'test description'}
    ])
    def test_name_not_instance_str(self, name):
        with pytest.raises(TypeError):
            Category(name, 'test description')

    def test_name_blank_spaces(self):
        with pytest.raises(ValueError):
            Category(' ', 'test description')

    def test_name_too_big(self):
        with pytest.raises(ValueError):
            Category('test name' * 100, 'test description')

    @pytest.mark.parametrize("description", [
        None, 5, 5.0, [1, 2, 3],
        ('a', 'b', 'c'),
        Category('name', 'description'),
        {'name': 'test name',
         'description': 'test description'}
    ])
    def test_description_not_instance_str(self, description):
        with pytest.raises(TypeError):
            Category('test name', description)

    def test_description_too_big(self):
        with pytest.raises(ValueError):
            Category('test name', 'test description' * 200)
