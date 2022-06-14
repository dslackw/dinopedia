import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Dinosaurs, Eating, Colour, Period, Size, Weight


URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/dinopedia"

URI = os.getenv('DATABASE_URL', URL)
engine = create_engine(URI)
session = sessionmaker(engine)()


eating = ['herbivorous', 'carnivorous', 'omnivorous']

colour = ['green', 'brown', 'black', 'brown-green',
          'brown-black', 'green-red', 'green-black']

period = ['jurassic', 'cretaceous', 'triassic',
          'paleogene', 'neogene']

size = ['tiny', 'very small', 'small',
        'medium', 'large', 'very large']


# Sample data only for development/test usage
dino_data = {
    1: {'name': 'Aardonyx', 'eating': 'herbivorous', 'colour': 'green', 'period': 'jurassic', 'size': 'large', 'weight': '8000 kg'},
    2: {'name': 'Bagaceratops', 'eating': 'herbivorous', 'colour': 'green', 'period': 'cretaceous', 'size': 'tiny', 'weight': '22 kg'},
    3: {'name': 'Chasmosaurus', 'eating': 'herbivorous', 'colour': 'brown-green', 'period': 'cretaceous', 'size': 'very small', 'weight': '1500 kg'},
    4: {'name': 'Deinonychus', 'eating': 'carnivorous', 'colour': 'brown-black', 'period': 'cretaceous', 'size': 'medium', 'weight': '8000 kg'},
    5: {'name': 'Elaphrosaurus', 'eating': 'carnivorous', 'colour': 'brown-black', 'period': 'cretaceous', 'size': 'very small', 'weight': '210 kg'},
    6: {'name': 'Fukuiraptor', 'eating': 'herbivorous', 'colour': 'green-red', 'period': 'cretaceous', 'size': 'very small', 'weight': '590 kg'},
    7: {'name': 'Giraffatitan', 'eating': 'herbivorous', 'colour': 'brown', 'period': 'jurassic', 'size': 'large', 'weight': '15000 kg'},
    8: {'name': 'Haplocanthosaurus', 'eating': 'herbivorous', 'colour': 'brown-green', 'period': 'jurassic', 'size': 'large', 'weight': '12800 kg'},
    9: {'name': 'Isisaurus', 'eating': 'herbivorous', 'colour': 'brown', 'period': 'cretaceous', 'size': 'large', 'weight': '14000 kg'},
    10: {'name': 'Jingshanosaurus', 'eating': 'herbivorous', 'colour': 'black', 'period': 'jurassic', 'size': 'small', 'weight': '2500 kg'},
    11: {'name': 'Kentrosaurus', 'eating': 'herbivorous', 'colour': 'brown', 'period': 'jurassic', 'size': 'small', 'weight': '700 kg'},
    12: {'name': 'Leaellynasaura', 'eating': 'herbivorous', 'colour': 'green-black', 'period': 'cretaceous', 'size': 'tiny', 'weight': '5 kg'},
    13: {'name': 'Magyatosaurus', 'eating': 'herbivorous', 'colour': 'green', 'period': 'cretaceous', 'size': 'very small', 'weight': '1100 kg'},
    14: {'name': 'Nanshiungosaurus', 'eating': 'omnivorous', 'colour': 'brown', 'period': 'cretaceous', 'size': 'very small', 'weight': '907 kg'},
    15: {'name': 'Omeisaurus', 'eating': 'herbivorous', 'colour': 'brown-black', 'period': 'jurassic', 'size': 'large', 'weight': '9800 kg'}
}


def insert_eating(eating):
    for e in eating:
        eat = Eating(diet=e)
        session.add(eat)

    session.commit()


def insert_colour(colour):
    for c in colour:
        color = Colour(color=c)
        session.add(color)

    session.commit()


def insert_period(period):
    for p in period:
        lived = Period(lived=p)
        session.add(lived)

    session.commit()


def insert_size(size):
    for s in size:
        width = Size(avg_size=s)
        session.add(width)

    session.commit()


def insert_dinopedia(data):
    for k, v in data.items():
        diet = session.query(Eating).filter(Eating.diet == v['eating']).first()
        color = session.query(Colour).filter(Colour.color == v['colour']).first()
        lived = session.query(Period).filter(Period.lived == v['period']).first()
        size = session.query(Size).filter(Size.avg_size == v['size']).first()
        dino = Dinosaurs(name=v['name'],
                         eating=diet,
                         colour=color,
                         period=lived,
                         size=size,
                         weight=Weight(mass=v['weight']))
        session.add(dino)

    session.commit()


if __name__ == '__main__':
    insert_eating(eating)
    insert_colour(colour)
    insert_period(period)
    insert_size(size)
    insert_dinopedia(dino_data)
