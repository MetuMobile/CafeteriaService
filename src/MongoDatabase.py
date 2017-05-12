from Config import Config

class MongoDatabase:
    lastImportedCafeteriaMenu = []

    def __init__(self):
        from CredentialsConfig import CredentialsConfig
        self.credentials = CredentialsConfig.mongoDbCredentials
        try:
            from datetime import datetime
            from pymongo import MongoClient
            self.client = MongoClient(self.credentials.ip)
            self.db = self.client.admin
            self.db.authenticate(self.credentials.user, self.credentials.password)#
            self.db = self.client.metumobile
            print ("mongodb connection successful! " + str(datetime.now()))
        except:
            print ("mongodb connection failed!")
            self.client.close()

    def getUpcomingCafeteriaMenu(self):
        from datetime import datetime
        #results = self.db['cafeteriaMenu'].find({})
        results = self.db['cafeteriaMenu'].find({"endTime": {"$gt": datetime.now()}})
        jsonableArray = []
        for each in results:
            each['endTime'] = each['endTime'].isoformat()
            each['startTime'] = each['startTime'].isoformat()
            each['_id'] = str(each['_id'])
            jsonableArray.append(each)
        return jsonableArray


    def setCafeteriaMenu(self, allMealsInFile):
        MongoDatabase.lastImportedCafeteriaMenu = allMealsInFile
        for eachMeal in allMealsInFile:
            #assert isinstance(eachMeal, MealContainer)
            self.db['cafeteriaMenu'].update({'endTime':eachMeal['endTime']}, eachMeal, upsert=True)

    # TODO refactor the next 3 functions!
    def insertCafeteriaRating(self, day, month, year, dinnerName, rating, remoteIp, datetime):
        self.db['cafeteriaRating'].insert({'day':day, 'month':month, 'year':year, 'dinnerName':dinnerName, 'rating':rating, 'remoteIp':remoteIp, 'lastUpdateTime': datetime})

    def insertCafeteriaRatingByMealId(self, mealId, rating, remoteIp, datetime, comment):
        self.db['cafeteriaRating'].insert({'mealId': mealId, 'rating': rating, 'remoteIp': remoteIp,
                                           'lastUpdateTime': datetime, 'comment': comment})

    def getMealRating(self, mealId):
        results = self.db['cafeteriaRating'].find({"mealId": mealId})
        _sum, index = 0, 0  # if results empty
        for index, each in enumerate(results):
            _sum += each['rating']
        return float(_sum) / (index+1)

    def getMealRateCount(self, mealId):
        from bson import ObjectId
        mealId = ObjectId(mealId)
        results = self.db['cafeteriaRating'].find({"mealId": mealId})
        rateCount = 0
        for mealRate in results:
            rateCount += 1
        return rateCount

    def getMeal(self, mealId):
        result = self.db['cafeteriaMenu'].find_one({"_id": mealId})
        result['_id'] = str(result['_id'])
        return result

    def getAllCafeteriaMenu(self):
        results = self.db['cafeteriaMenu'].find({})
        jsonableArray = []
        for each in results:
            try:
                each['endTime'] = each['endTime'].isoformat()
                each['startTime'] = each['startTime'].isoformat()
                each['_id'] = str(each['_id'])
                jsonableArray.append(each)
            except:
                pass
        return jsonableArray

