from database import create_db, Session
from fruits import Fruits
from vegetables import Vegetables
from canning import Canning


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    pass
    fruit_name = ['Яблоко Антоновка', 'Яблоко Красное', 'Груша Дюшес', 'Груша Мария',
                  'Вишня', 'Слива', 'Клубника', 'Черника']
    vegetables_name = ['Огурцы', 'Помидоры', 'Перец', 'Капуста']

    canning1 = Canning(canning_name='Варенье')
    canning2 = Canning(canning_name='Соленье')
    session.add(canning1)
    session.add(canning2)

    for key, fr in enumerate(fruit_name):
        fruit = Fruits(fruit_name=fr)
        fruit.canning_name.append(canning1)
        session.add(fruit_name)

    for key, veg in enumerate(vegetables_name):
        vegetable = Vegetables(vegetables_name=veg)
        vegetable.canning_name.append(canning2)
        session.add(vegetables_name)

    session.commit()
    session.close()
