# 1) Создать базу данных товаров, у товара есть: 
# Category (связанная таблица), name, есть ли товар в продаже или на складе, price, кол-во
# единиц.
# Создать html страницу. На первой странице выводить ссылки на все
# категории, при переходе на категорию получать список всех товаров в
# наличии ссылками, при клике на товар выводить его цену, полное описание и
# кол-во единиц в наличии.
# 2) Создать страницу для администратора, через которую он может добавлять
# новые товары и категории.

from flask import Flask
from flask import render_template

app = Flask(__name__)

"""
       <html>
           <body>
               <h4> Hello world </h1>
           </body>
       </html>
       """

products = [
    {'Category': 'Овощи', 'name': 'Помидор', 'on_stock': True, 'price': 25, 'quantity': 50},
    {'Category': 'Овощи', 'name': 'Огурец', 'on_stock': True, 'price': 25, 'quantity': 50},
    {'Category': 'Фрукты', 'name': 'Яблоко', 'on_stock': True, 'price': 15, 'quantity': 25},
    {'Category': 'Фрукты', 'name': 'Черешня', 'on_stock': True, 'price': 15, 'quantity': 25},
    {'Category': 'Зелень', 'name': 'Укроп', 'on_stock': True, 'price': 267, 'quantity': 500},
    {'Category': 'Зелень', 'name': 'Петрушка', 'on_stock': True, 'price': 267, 'quantity': 500},
]


@app.route('/')
def show_categories():
    products_1 = []
    for _indx, prod in enumerate(products):
        products_1.append(prod["Category"])
    categories = set(products_1)
    return render_template('index.html', categories=categories)


@app.route('/<Category>')
def show_category_products(Category):
    list_cat_prod = []
    for _id, cat in enumerate(products):
        if Category in cat.values():
            list_cat_prod.append(products[_id])

    return render_template('category.html', list_cat=list_cat_prod, category=Category)


@app.route('/admin')
def admin():
    return render_template('admin.html')
    


if __name__ == '__main__':
    app.run(debug=True, port=8000)