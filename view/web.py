import sys
sys.path.append('.')

from flask import Flask, render_template, request, redirect
from controllers.category_controller import CategoryController
from models.category import Category

app = Flask(__name__)

controller = CategoryController()


@app.route('/')
def home():
    return render_template('template.html')


@app.route('/category')
def category():
    category_list = controller.read_all()
    return render_template('category.html', categories=category_list)


@app.route('/category/create', methods=['POST', 'GET'])
def create_category():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        new_category = Category(name, description)
        controller.create(new_category)
        return redirect('/category')
    return render_template('create_category.html')


@app.route('/category/update', methods=['POST'])
def category_update():
    identifier = int(request.form.get('id'))
    up_cat = controller.read_by_id(identifier)
    up_cat.name = request.form.get('name')
    up_cat.description = request.form.get('description')
    controller.update(up_cat)
    return redirect('/category')


@app.route('/category/update/<int:id>')
def category_update_form(id):
    category = controller.read_by_id(id)
    return render_template('update_category.html', category=category)


@app.route('/category/delete/<int:id>')
def delete_category(id):
    category = controller.read_by_id(id)
    controller.delete(category)
    return redirect('/category')


app.run(debug=True)
