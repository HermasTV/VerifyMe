import pymongo

class Matcher():
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.table = self.myclient["database"]
        self.db = self.table["verifyme"]

    def initialize(self):
        
        
        pass