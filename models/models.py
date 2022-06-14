#!/usr/bin/env python

from core import db

# Creating many to many relationships
dinosaurs_eating = db.Table(
    'dinosaurs_eating', db.Column(
        'dinosaurs_id', db.Integer, db.ForeignKey('dinosaurs.id')),
    db.Column('eating_id', db.Integer, db.ForeignKey('eating.id'))
)

dinosaurs_colour = db.Table(
    'dinosaurs_colour', db.Column(
        'dinosaurs_id', db.Integer, db.ForeignKey('dinosaurs.id')),
    db.Column('colour_id', db.Integer, db.ForeignKey('colour.id'))
)

dinosaurs_period = db.Table(
    'dinosaurs_period', db.Column(
        'dinosaurs_id', db.Integer, db.ForeignKey('dinosaurs.id')),
    db.Column('period_id', db.Integer, db.ForeignKey('period.id'))
)

dinosaurs_size = db.Table(
    'dinosaurs_size', db.Column(
        'dinosaurs_id', db.Integer, db.ForeignKey('dinosaurs.id')),
    db.Column('size_id', db.Integer, db.ForeignKey('size.id'))
)

dinosaurs_weight = db.Table(
    'dinosaurs_weight', db.Column(
        'dinosaurs_id', db.Integer, db.ForeignKey('dinosaurs.id')),
    db.Column('weight_id', db.Integer, db.ForeignKey('weight.id'))
)


class Dinosaurs(db.Model):
    __tablename__ = 'dinosaurs'

    id = db.Column(db.Integer, primary_key='True')
    name = db.Column(db.String(30), nullable=False)
    images = db.relationship('Images', backref='dinosaurs',
                             cascade='all,delete', uselist=False)
    eating = db.relationship('Eating', secondary=dinosaurs_eating,
                             backref='dinosaurs', uselist=False)
    colour = db.relationship('Colour', secondary=dinosaurs_colour,
                             backref='dinosaurs', uselist=False)
    period = db.relationship('Period', secondary=dinosaurs_period,
                             backref='dinosaurs', uselist=False)
    size = db.relationship('Size', secondary=dinosaurs_size,
                           backref='dinosaurs', uselist=False)
    weight = db.relationship('Weight', secondary=dinosaurs_weight,
                             backref='dinosaurs', uselist=False)

    def __repr__(self):
        return f'{self.name}'

    @property
    def serialized(self) -> list:
        """ Customizing my serializer """
        return self.name, {
            'images': str(self.images).split(),
            'eating': str(self.eating),
            'colour': str(self.colour),
            'period': str(self.period),
            'size': str(self.size),
            'weight': str(self.weight)
        }


class Favourite(db.Model):
    __tablename__ = 'favourite'

    id = db.Column(db.Integer, primary_key=True)
    image1 = db.Column(db.Boolean, default=False)
    image2 = db.Column(db.Boolean, default=False)
    images_id = db.Column(db.Integer, db.ForeignKey('images.id'))

    def __init__(self, image1, image2, images_id):
        self.image1 = image1
        self.image2 = image2
        self.images_id = images_id

    def __repr__(self):
        return f'{self.image1}, {self.image2}'


class Images(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    image1 = db.Column(db.String(128))
    image2 = db.Column(db.String(128))
    dinosaurs_id = db.Column(db.Integer, db.ForeignKey('dinosaurs.id'))
    favourite = db.relationship('Favourite', backref='Images',
                                cascade='all,delete', uselist=False)

    def __repr__(self):
        return f'{self.image1} {self.image2}'


class Eating(db.Model):
    __tablename__ = 'eating'

    id = db.Column(db.Integer, primary_key='True')
    diet = db.Column(db.String(20), nullable=False)

    def __init__(self, diet):
        self.diet = diet

    def __str__(self):
        return self.diet


class Colour(db.Model):
    __tablename__ = 'colour'

    id = db.Column(db.Integer, primary_key='True')
    color = db.Column(db.String(20), nullable=False)

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color


class Period(db.Model):
    __tablename__ = 'period'

    id = db.Column(db.Integer, primary_key='True')
    lived = db.Column(db.String(20), nullable=False)

    def __init__(self, lived):
        self.lived = lived

    def __str__(self):
        return self.lived


class Size(db.Model):
    __tablename__ = 'size'

    id = db.Column(db.Integer, primary_key='True')
    avg_size = db.Column(db.String(20), nullable=False)

    def __init__(self, avg_size):
        self.avg_size = avg_size

    def __str__(self):
        return self.avg_size


class Weight(db.Model):
    __tablename__ = 'weight'

    id = db.Column(db.Integer, primary_key='True')
    mass = db.Column(db.String(20), nullable=False)

    def __init__(self, mass):
        self.mass = mass

    def __str__(self):
        return self.mass
