from flask import Flask
from flask_restful import Api
from config import Config
from models import db
from resources.student import StudentApi
from resources.doctor import DoctorApi


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    api = Api(app)
    api.add_resource(StudentApi, '/student/<int:human_id>')
    api.add_resource(DoctorApi, '/doctor/<int:human_id>')

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
