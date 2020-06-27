# 1) Создать базу данных товаров, у товара есть: 
# Категория (связанная таблица), название, есть ли товар в продаже или на складе, цена, кол-во
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

persons = [
    {'name': 'John', 'age': 20, 'hobbie': 'Football', 'description': ',....'},
    {'name': 'Luci', 'age': 16, 'hobbie': 'Programming', 'description': ',....'}
]


@app.route('/')
def show_persons():
    return render_template('index.html', persons=persons)


@app.route('/<name>')
def show_certain_person(name):
    person_obj = None
    for _id, person in enumerate(persons):
        if name in person.values():
            person_obj = persons[_id]
            break

    return render_template('person_page.html', person=person_obj)


@app.route('/values/<int:id>')
def integer_handler(id):
    print(id)
    return str(id)


if __name__ == '__main__':
    app.run(debug=True, port=8000)