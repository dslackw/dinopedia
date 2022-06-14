#!/usr/bin/env python

from core import db, create_app
from flask_admin import Admin
from flask_restful import Api
from flask_admin.contrib.sqla import ModelView
from views.views import (Dinopedia, DinosaurSearch, ImagesView,
                         DinopediaModelView, SeeFavouriteImages)
from models.models import (Dinosaurs, Images, Colour, Eating, Period,
                           Size, Weight, Favourite)


app = create_app()
api = Api(app)
app.config.from_object("config.Config")
admin = Admin(app, template_mode='bootstrap4')
db.init_app(app)


@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'


# admin views
admin.add_view(DinopediaModelView(Dinosaurs, db.session))
admin.add_view(ImagesView(Images, db.session))
admin.add_view(ModelView(Favourite, db.session))
admin.add_view(ModelView(Colour, db.session))
admin.add_view(ModelView(Eating, db.session))
admin.add_view(ModelView(Period, db.session))
admin.add_view(ModelView(Size, db.session))
admin.add_view(ModelView(Weight, db.session))


# api views
api.add_resource(Dinopedia, '/dinosaurs')
api.add_resource(DinosaurSearch, '/dinosaurs/<string:name>')
api.add_resource(SeeFavouriteImages, '/dinosaurs/favourites')


if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(host='0.0.0.0', port=8000)
else:
    app.app_context().push()
    db.create_all()
