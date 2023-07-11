from database import create_db, Session
from fruits import Fruits
from vegetables import Vegetables
from canning import Canning


def create_database(load_fake_data=False):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    pass
    fruit = ['Яблоко Антоновка', 'Яблоко Красное', 'Груша Дюшес', 'Груша Мария',
             'Вишня', 'Слива', 'Клубника', 'Черника']
    vegetable = ['Огурцы', 'Помидоры', 'Перец', 'Капуста']

    canning1 = Canning(canning_name='Варенье')
    canning2 = Canning(canning_name='Соленье')
    session.add(canning1)
    session.add(canning2)

    for key, fr in enumerate(fruit):
        fruits = Fruits(fruit_name=fr, canning_name=canning1)
        session.add(fruits)

    for key, vg in enumerate(vegetable):
        vegetables = Vegetables(vegetable_name=vg, canning_name=canning2)
        session.add(vegetables)

    session.commit()
    session.close()
