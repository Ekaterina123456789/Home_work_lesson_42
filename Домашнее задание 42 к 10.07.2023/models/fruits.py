from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base


class Fruits(Base):
    __tablename__ = 'fruits'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fruit_name = Column(String(100), nullable=False)
    canning_name = Column(String(100), ForeignKey('canning.canning_name'))

    def __init__(self, fruit_name, canning_name):
        self.fruit_name = fruit_name
        self.canning_name = canning_name

    def __repr__(self):
        return f'Фрукт (Название: {self.fruit_name}, ' \
               f'Название заготовки: {self.canning_name}) '
