from flask import Flask, jsonify  # , request, render_template
import sys
from Config import Config
from Meals import Meals
from MealImportExcelFileRefresh import MealImportExcelFileRefresh
from WebMenuUploader import WebMenuUploader, WebMenuUploadComplete

class PhonebookService:
    serviceName = "cafeteria"

    def __init__(self):
        self._initializeService()
        # self.app.add_url_rule('/phonebook', '', self.getPhonebook)
        # self.app.add_url_rule('/cafeteria', view_func=Cafeteria.as_view('myview'))
        # self.app.add_url_rule('/updatecafeteriamenu', view_func=Cafeteria.as_view('myview'))
        self.app.add_url_rule('/readExcelImport', view_func=MealImportExcelFileRefresh.as_view('MealImportExcelFileRefresh'))
        self.app.add_url_rule('/excelUpload', view_func=WebMenuUploader.as_view('upload'))
        self.app.add_url_rule('/excelUploadComplete', view_func=WebMenuUploadComplete.as_view('complete'))
        self.app.add_url_rule('/meals', view_func=Meals.as_view('meals'))
        self._runService()


    def updateCafeteriaMenu():
        # Admin().checkSuperAdminAuth(request.values.get('pw'))
        MealImportExcelFileRefresh().updateCafeteriaMenu()
        return jsonify(Response="200")

    def _addLogger(self):
        import logging
        handler = logging.FileHandler(Config.loggerPath)  # errors logged to this file
        handler.setLevel(logging.ERROR)  # only log errors and above
        self.app.logger.addHandler(handler)  # attach the handler to the app's logger

    def _runService(self):
        self.app.run(debug=Config.debug, host='0.0.0.0', port=Config.services[self.serviceName]['port'], threaded=True)
        print(str(self.serviceName) + " service is started.")

    def _initializeService(self):
        sys.stdout.flush()
        self.app = Flask(__name__)
        self._addLogger()
        self.app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


if __name__ == "__main__":
    service = PhonebookService()
