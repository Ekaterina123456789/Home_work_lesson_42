from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Vegetables(Base):
    __tablename__ = 'vegetables'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vegetable_name = Column(String(100), nullable=False)
    weight_v = Column(Integer)
    canning_name = Column(String(100), ForeignKey('canning.name'))

    def __init__(self, fruit_name, weight_v, canning_name):
        self.surname = fruit_name[0]
        self.name = fruit_name[1]
        self.weight_v = weight_v
        self.canning_name = canning_name

    def __repr__(self):
        return f'Овощ (Название: {self.surname} {self.name}, ' \
               f'Вес: {self.weight_v}, ' \
               f'Название заготовки: {self.canning_name}) '

