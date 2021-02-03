import sys
sys.path.append('.')

from controllers.category_controller import CategoryController
from models.category import Category
import pytest

class TestCategoryController:
    @pytest.fixture
    def create_instance(self):
        controller = CategoryController()
        return controller

    def test_category_controller_instance(self, create_instance):

        assert isinstance(create_instance, CategoryController)


    def test_read_all_should_return_list(self, create_instance):

        result = create_instance.read_all()

        assert isinstance(result, list)


    def test_create_category(self, create_instance):
        name = 'Test'
        description = 'Test'
        category = Category(name, description)

        result = create_instance.create(category)

        assert result.id_ is not None
        assert result.name == name
        assert result.description == description

        create_instance.delete(result)


    def test_update_category(self, create_instance):
        name = 'Category'
        description = 'Test'
        category = Category(name, description)
        created = create_instance.create(category)

        created.name = 'Category 2'
        created.description = 'Test 2'
        result = create_instance.update(created)

        assert result.id_ is not None
        assert result.name == 'Category 2'
        assert result.description == 'Test 2'

        create_instance.delete(result)


    def test_delete_category(self, create_instance):
        name = 'Category'
        description = 'Test'
        category = Category(name, description)
        created = create_instance.create(category)

        create_instance.delete(created)

        with pytest.raises(Exception) as exc:
            create_instance.read_by_id(created.id_)
            assert exc.value == 'Object not found in database.'


    def test_read_by_id_should_return_category(self, create_instance):
        name = 'Category'
        description = 'Test'
        category = Category(name, description)
        created = create_instance.create(category)

        result = create_instance.read_by_id(created.id_)

        assert isinstance(result, Category)
        assert result.name == name
        assert result.description == description

        create_instance.delete(created)


    def test_read_by_id_with_invalid_id_should_raise_exception(self, create_instance):
        with pytest.raises(Exception) as exc:
            create_instance.read_by_id(71289379)
            assert str(exc.value) == 'Object not found in database.'
