import base64
import hashlib
import os

import pymongo


DATABASE = "schedtodo"


TODOS = {

'8:00AM - 9:00AM':'',
'9:00AM - 10:00AM':'',
'10:00AM - 11:00AM':'',
'11:00AM - 12:00PM':'',
'12:00PM - 1:00PM':'',
'1:00PM - 2:00PM':'',
'2:00PM - 3:00PM':'',
'3:00PM - 4:00PM':'',
'4:00PM - 5:00PM':'',
'5:00PM - 6:00PM':'',
'6:00PM - 7:00PM':'',
'7:00PM - 8:00PM':'',
'8:00PM - 9:00PM':'',
'9:00PM - 10:00PM':'',
'10:00PM - 11:00PM':''

}


class PasswordHelper:

    def get_hash(self,plain):
        return hashlib.sha512(plain).hexdigest()

    def get_salt(self):
        return base64.b64encode(os.urandom(20))

    def validate_password(self, plain, salt, expected):
        return self.get_hash(plain + salt) == expected

class DBHelper():

    def __init__(self):
        client = pymongo.MongoClient()
        self.db = client[DATABASE]

    def create_user(self, email, salt, hashed):
        self.db.users.insert({"email": email, "salt": salt, "hashed": hashed})
