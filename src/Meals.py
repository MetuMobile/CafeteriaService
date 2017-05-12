from MongoDatabase import MongoDatabase
from flask.views import MethodView

class Meals(MethodView):
    def __init__(self):
        pass

    def get(self):
        from flask import jsonify, request
        futureOnly = request.values.get('futureonly')
        if futureOnly=='true' or futureOnly=='True':
            return jsonify(CafeteriaMenu=MongoDatabase().getUpcomingCafeteriaMenu())
        else:
            return jsonify(CafeteriaMenu=MongoDatabase().getAllCafeteriaMenu())