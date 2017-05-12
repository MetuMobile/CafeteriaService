from flask import render_template, request
from datetime import datetime
import os
from Config import Config
from MealImportExcelFileRefresh import MealImportExcelFileRefresh
from flask.views import MethodView
from Admin import Admin

class WebMenuUploader(MethodView):
    def get(self):
        Admin().checkSuperAdminAuth()
        return render_template("upload.html")

class WebMenuUploadComplete(MethodView):
    def post(self):
        target = os.path.join(Config.dynamicFilesFolderPath)
        if not os.path.isdir(target):
            os.mkdir(target)

        selected_files = request.files.getlist("file")
        time_stamp = str(datetime.now().timestamp())
        for file in selected_files:
            file_name = time_stamp+'.xlsx'
            destination = os.path.join(Config.dynamicFilesFolderPath, file_name)# "/".join([target, file_name])
            file.save(destination)
            MealImportExcelFileRefresh(destination).updateCafeteriaMenu()

        return render_template("complete.html")
