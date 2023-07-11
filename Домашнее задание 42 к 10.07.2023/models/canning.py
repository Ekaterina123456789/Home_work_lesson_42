from sqlalchemy import Column, ForeignKey, Integer, String, Table
from database import Base
from sqlalchemy.orm import relationship


association_table = Table('association', Base.metadata,
                          Column('vegetables_id', Integer, ForeignKey('vegetables.id')),
                          Column('fruits_id', Integer, ForeignKey('canning.id')))


class Canning(Base):
    __tablename__ = 'canning'
    id = Column(Integer, primary_key=True)
    canning_name = Column(String(100), nullable=False)
    ingredient1 = (Integer, ForeignKey('vegetables.vegetables_name'))
    ingredient2 = (Integer, ForeignKey('fruits.fruits_name'))
    cans_plan = Column(Integer, nullable=False)
    cans_fact = Column(Integer)

    def __repr__(self):
        return f'Id заготовки: {self.id}, ' \
               f'Название заготовки: {self.canning_name}'
