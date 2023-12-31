from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Vegetables(Base):
    __tablename__ = 'vegetables'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vegetable_name = Column(String(100), nullable=False)
    canning_name = Column(String(100), ForeignKey('canning.canning_name'))

    def __init__(self, vegetable_name, canning_name):
        self.vegetable_name = vegetable_name
        self.canning_name = canning_name

    def __repr__(self):
        return f'Овощ (Название: {self.vegetable_name}, ' \
               f'Название заготовки: {self.canning_name}) '

