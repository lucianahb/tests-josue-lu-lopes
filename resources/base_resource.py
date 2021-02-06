from typing import Type
from flask import request
from flask_restful import Resource
from dao.base_dao import BaseDao


class BaseResource(Resource):
    def __init__(self, dao: BaseDao, model_type: Type):
        self.__dao = dao
        self.__model_type = model_type

    def get(self, identifier=None):
        if identifier:
            return self.__dao.read_by_id(identifier)
        return self.__dao.read_all()

    def post(self):
        data = request.json
        model = self.__model_type(**data)
        self.__dao.save(model)
        return model, 201

    def put(self, identifier):
        data = request.json
        if data['id_'] == identifier:
            model = self.__dao.read_by_id(identifier)
            for key, value in data.items():
                setattr(model, key, value)
            return self.__dao.save(model)
        return None, 404

    def delete(self, identifier):
        model = self.__dao.read_by_id(identifier)
        self.__dao.delete(model)
        return None, 204
