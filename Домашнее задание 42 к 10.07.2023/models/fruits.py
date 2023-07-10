from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base


class Fruits(Base):
    __tablename__ = 'fruits'
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname_fruit = Column(String(100), nullable=False)
    name_fruit = Column(String(100))
    weight_f = Column(Integer)
    canning_name = Column(String(100), ForeignKey('canning.name'))

    def __init__(self, fruit_name, weight_f, canning_name):
        self.surname = fruit_name[0]
        self.name = fruit_name[1]
        self.weight_f = weight_f
        self.canning_name = canning_name

    def __repr__(self):
        return f'Фрукт (Название: {self.surname} {self.name}, ' \
               f'Вес: {self.weight_f}, ' \
               f'Название заготовки: {self.canning_name}) '
