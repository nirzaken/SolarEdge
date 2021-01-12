import pymongo


class MongoDBClient:

    def __init__(self, ip, port, db, collection):
        self.ip = ip
        self.port = port
        self.db = db
        self.collection = collection
        self.myClient = None
        self.myDb = None
        self.myCol = None

    def initDB(self):
        try:
            self.myClient = pymongo.MongoClient("mongodb://" + self.ip + ":" + self.port + "/")
            self.myDb = self.myClient[self.db]
            self.myCol = self.myDb[self.collection]
        except pymongo.errors.ConnectionFailure:
            print("Connection to host failed")
            return
        except:
            print("Failed to establish connection, credentials: "
                  + self.ip + ", " + self.port, ", " + self.db + ", " + self.collection)
            return
        else:
            dbResponse = self.myCol.delete_many({})
            myList = [
                {"_id": 0, "count": 0},
                {"_id": 1, "count": 0},
                {"_id": 2, "count": 0},
                {"_id": 3, "count": 0},
                {"_id": 4, "count": 0},
                {"_id": 5, "count": 0},
                {"_id": 6, "count": 0},
                {"_id": 7, "count": 0},
                {"_id": 8, "count": 0},
                {"_id": 9, "count": 0},
                {"_id": 10, "count": 0},
                {"_id": 11, "count": 0},
                {"_id": 12, "count": 0},
                {"_id": 13, "count": 0},
                {"_id": 14, "count": 0},
                {"_id": 15, "count": 0},
                {"_id": 16, "count": 0},
                {"_id": 17, "count": 0},
                {"_id": 18, "count": 0},
                {"_id": 19, "count": 0},
                {"_id": 20, "count": 0},
                {"_id": 21, "count": 0},
                {"_id": 22, "count": 0},
                {"_id": 23, "count": 0},
                {"_id": 24, "count": 0},
                {"_id": 25, "count": 0},
                {"_id": 26, "count": 0},
                {"_id": 29, "count": 0},
                {"_id": 27, "count": 0},
                {"_id": 28, "count": 0},
                {"_id": 30, "count": 0}
            ]
            dbResponse = self.myCol.insert_many(myList)
