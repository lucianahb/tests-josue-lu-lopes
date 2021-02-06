import sys
sys.path.append('.')

from models.category import Category
from dao.category_dao import CategoryDao
import pytest


def test_save():
    category_dao = CategoryDao()
    model = Category('Test category', 'Category description test')
    model = category_dao.save(model)
    assert model.id_ is not None, "Object not saved!"
    category_dao.delete(model)


def test_read_all():
    category_dao = CategoryDao()
    assert isinstance(category_dao.read_all(), list)


def test_read_by_id():
    category_dao = CategoryDao()
    id_ = 42
    assert isinstance(category_dao.read_by_id(id_), Category)


def test_delete():
    model = Category('Category Test', 'Test Description')
    category_dao = CategoryDao()
    model = category_dao.save(model)
    id = model.id_
    category_dao.delete(model)
    with pytest.raises(Exception):
        test_read_by_id(id)


def test_update():
    model = Category('Category Test', 'Test Description')
    category_dao = CategoryDao()
    model = category_dao.save(model)
    if isinstance(model, Category):
        old_name = model.name
        model.name = 'New name test'
    category_dao.save(model)
    if isinstance(model, Category):
        assert old_name != model.name
    category_dao.delete(model)
