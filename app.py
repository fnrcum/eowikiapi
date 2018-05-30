from flask import Flask, Blueprint
from flask_restful import Api

app = Flask(__name__)
app.config.from_object('config')
with app.app_context():
    from models._models import PagesModel, ImagesModel, VotesModel, jwt, dbSetup
    from resources import *
    dbSetup()


api_bp = Blueprint('api', __name__)
api = Api(api_bp)
app.register_blueprint(api_bp, url_prefix="/api/v1")


api.add_resource(PagesResource, '/tokens')
api.add_resource(PermissionsResource, '/permissions')
api.add_resource(AuthLogin, '/auth/login')
api.add_resource(AuthRegister, '/auth/register')
api.add_resource(UsersResource, '/users')


if __name__ == '__main__':
    app.run(debug=True, port=5001)