from flask import request
from http import HTTPStatus
from flask_restful import Resource, reqparse, abort
from utils.error_list import ValidationError
from utils import check_url_params_set, str2bool
from decorators import login_required, validate_user
from models._models import ImagesModel, PagesModel


class PagesResource(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, help='Rate to charge for this resource')
        parser.add_argument('name', type=str, help='Rate to charge for this resource')
        parser.add_argument('category', type=str, help='Rate to charge for this resource')
        parser.add_argument('registry', type=str, help='Rate to charge for this resource')
        self.args = parser.parse_args()

    @login_required
    def get(self):
        filter_dict = {}
        for key, value in self.args.items():
            if value is not None:
                filter_dict[key] = value
        if check_url_params_set(self.args):
            if self.args.get("id") is not None:
                return PagesModel.find(self.args.get("id"))
            else:
                results = PagesModel.filter(filter_dict)
        else:
            results = PagesModel.get_all()
        return results

    def post(self):
        post_args = self.args
        if post_args["id"]:
            del post_args['id']
        PagesModel.create(post_args)
        return {"status": HTTPStatus.CREATED, "message": "Record Created"}, HTTPStatus.CREATED

    def delete(self):
        PagesModel.delete(self.args.get("id"))
        return {"status": HTTPStatus.ACCEPTED, "message": "Record Deleted"}, HTTPStatus.ACCEPTED

    def put(self):
        id = self.args.get("id")
        put_args = self.args
        if put_args["id"]:
            del put_args['id']
        PagesModel.update(id, put_args)
        return {"status": HTTPStatus.ACCEPTED, "message": "Record Updated"}, HTTPStatus.ACCEPTED


class PermissionsResource(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, help='Rate to charge for this resource')
        parser.add_argument('name', type=str, help='Rate to charge for this resource')
        parser.add_argument('number', type=str, help='Rate to charge for this resource')
        self.args = parser.parse_args()

    def get(self):
        filter_dict = {}
        for key, value in self.args.items():
            if value is not None:
                filter_dict[key] = value
        if check_url_params_set(self.args):
            if self.args.get("id") is not None and not self.args.get("relation"):
                return ImagesModel.find(self.args.get("id"))
            else:
                results = ImagesModel.filter(filter_dict)
        else:
            results = ImagesModel.get_all()
        return results

    def post(self):
        post_args = self.args
        if post_args["id"]:
            del post_args['id']
        ImagesModel.create(post_args)
        return {"status": HTTPStatus.CREATED, "message": "Record Created"}, HTTPStatus.CREATED

    def delete(self):
        ImagesModel.delete(self.args.get("id"))
        return {"status": HTTPStatus.ACCEPTED, "message": "Record Deleted"}, HTTPStatus.ACCEPTED

    def put(self):
        id = self.args.get("id")
        put_args = self.args
        if put_args["id"]:
            del put_args['id']
        ImagesModel.update(id, put_args)
        return {"status": HTTPStatus.ACCEPTED, "message": "Record Updated"}, HTTPStatus.ACCEPTED


class UsersResource(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str, help='John', required=True)
        parser.add_argument('last_name', type=str, help='Snow', required=True)
        parser.add_argument('email', type=str, help='mail@abcd.com', required=True)
        parser.add_argument('password', type=str, help='some witty password', required=True)
        parser.add_argument('password_conf', type=str, help='some witty password', required=True)
        parser.add_argument('address', type=str, help='your address', default=None)
        parser.add_argument('zip', type=str, help='your zip code', default=None)
        parser.add_argument('phone', type=str, help='phone number', default=None)
        parser.add_argument('mode', type=str, help='the user mode', default='buyer')
        parser.add_argument('ban', type=bool, help='True or False', default=False)
        parser.add_argument('permissions_by_number', help='permission number list', default=[])
        self.args = parser.parse_args()

    def get(self):
        filter_dict = {}
        for key, value in self.args.items():
            if value is not None:
                filter_dict[key] = value
        if check_url_params_set(self.args):
            if self.args.get("id") is not None and not self.args.get("relation"):
                return ImagesModel.find(self.args.get("id"))
            else:
                results = ImagesModel.filter(filter_dict)
        else:
            results = ImagesModel.get_all()
        return results

    def post(self):
        post_args = self.args
        if post_args["id"]:
            del post_args['id']
        ImagesModel.create(post_args)
        return {"status": HTTPStatus.CREATED, "message": "Record Created"}, HTTPStatus.CREATED

    def delete(self):
        ImagesModel.delete(self.args.get("id"))
        return {"status": HTTPStatus.ACCEPTED, "message": "Record Deleted"}, HTTPStatus.ACCEPTED

    def put(self):
        id = self.args.get("id")
        put_args = self.args
        if put_args["id"]:
            del put_args['id']
        ImagesModel.update(id, put_args)
        return {"status": HTTPStatus.ACCEPTED, "message": "Record Updated"}, HTTPStatus.ACCEPTED
