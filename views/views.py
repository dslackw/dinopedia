#!/usr/bin/env python

import os
import os.path as op
from typing import Dict
from markupsafe import Markup

from core import db
from flask_admin import form
from flask_restful import Resource
from flask_admin.contrib import sqla
from sqlalchemy.event import listens_for
from models.models import Images, Dinosaurs, Favourite
from flask import jsonify, url_for, request, Response, json


# Create directory for images to use
file_path = op.join(op.dirname(__file__), 'static')
try:
    os.mkdir(file_path)
except OSError:
    pass


class Dinopedia(Resource):

    def get(self) -> Dict:
        """
        Find all the available kinds of dinosaurs.
        """
        dinosaurs = Dinosaurs.query.all()

        if dinosaurs:
            return jsonify(dict(dino.serialized for dino in dinosaurs))

        return jsonify('Dinosaurs not found')


class DinosaurSearch(Resource):

    def get(self, name: str) -> Dict:
        """
        Search for a particular kind of dinosaur and gets their images.
        """
        dinosaur = Dinosaurs.query.filter(Dinosaurs.name == name).first()

        if dinosaur:
            return jsonify({'images': str(dinosaur.images).split()})

        return jsonify('Dinosaur not found')

    def post(self, name: str) -> Dict:
        """
        Give a like your favourite images of dinosaurs.
        Like = True
        """
        arg1 = request.args.get('image1')
        arg2 = request.args.get('image2')

        if arg1 or arg2:
            # converting string --> bool
            if type(arg1) == str:
                arg1 = eval(arg1.capitalize())
            if type(arg2) == str:
                arg2 = eval(arg2.capitalize())

            images = Images.query.join(
                Dinosaurs, Images.dinosaurs_id == Dinosaurs.id).filter(
                    Dinosaurs.name == name).first()

            likes = Favourite(image1=arg1,
                              image2=arg2,
                              images_id=int(images.id))

            db.session.add(likes)
            db.session.commit()

            return Response(json.dumps({'Thank': 'you!'}), status=201,
                            content_type='application/json')

        return jsonify('Please give a like!')


class SeeFavouriteImages(Resource):

    def get(self) -> Dict:
        """
        See your favourite images of dinosaurs.
        """
        images1 = Images.query.join(
            Favourite, Favourite.image1 == True).filter(
                Favourite.images_id == Images.id).all()

        images2 = Images.query.join(
            Favourite, Favourite.image2 == True).filter(
                Favourite.images_id == Images.id).all()

        favourites1 = [i.image1 for i in images1]
        favourites2 = [i.image2 for i in images2]

        if images1 or images2:
            return jsonify({'images': sorted(favourites1 + favourites2)})

        return jsonify('Images not found')


class ImagesView(sqla.ModelView):
    """
    Rendering and converting images to thumbnails to view.
    """
    def _list_thumbnail_1(view, context, model, name):
        if not model.image1:
            return ''

        return Markup('<img src="%s">' % url_for(
            'static', filename=form.thumbgen_filename(model.image1)))

    def _list_thumbnail_2(view, context, model, name):
        if not model.image2:
            return ''

        return Markup('<img src="%s">' % url_for(
            'static', filename=form.thumbgen_filename(model.image2)))

    column_formatters = {
        'image1': _list_thumbnail_1,
        'image2': _list_thumbnail_2
    }

    form_extra_fields = {
        'image1': form.ImageUploadField('Image',
                                        base_path=file_path,
                                        thumbnail_size=(100, 60, True)),
        'image2': form.ImageUploadField('Image',
                                        base_path=file_path,
                                        thumbnail_size=(100, 60, True))
    }


class DinopediaModelView(sqla.ModelView):
    """ Customising the Admin view.

        columns: The names of the columns.
        column_list: Collection of the model field names for
                     the list view.
        form_rules: List of rendering rules for model creation form.
        column_sortable_list: Collection of the sortable columns
                              for the list view.
    """
    columns = ('name', 'images', 'colour', 'eating', 'period',
               'size', 'weight')

    column_list = form_rules = columns
    column_searchable_list = ('name',)
    column_sortable_list = ('name', ('colour', 'colour.color'),
                            ('eating', 'eating.diet'),
                            ('period', 'period.lived'),
                            ('size', 'size.avg_size'),
                            ('weight', 'weight.mass'))


@listens_for(Images, 'after_delete')
def del_image(mapper, connection, target):
    """
    Deletes images and thumbnails when deleted from the database.
    """
    if target.image1:
        remove_images([target.image1,
                      form.thumbgen_filename(target.image1)])

    if target.image2:
        remove_images([target.image2,
                      form.thumbgen_filename(target.image2)])


def remove_images(images):
    try:
        for img in images:
            os.remove(op.join(file_path, img))
    except OSError:
        pass
