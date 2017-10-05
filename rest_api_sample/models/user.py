from rest_api_sample.utils.database import *
from passlib.apps import custom_app_context as pwd_context
import json

class User(object):
    """ A user of the rest API with the following properties:

    Attributes:
        id: primary key of user table
        username
        password: encrypted password
        email
        phone
        address
        additional_info: extra information provided by user during setup """

    def encrypted_password(password):
        return pwd_context.encrypt(password)

    def verify_password(id, password):
        hash = User.find(id)
        return pwd_context.verify(password, hash)

    def __init__(self, username, password, email, phone, address, additional_info, is_admin):
        self.username = username
        self.password = User.encrypted_password(password)
        self.email = email
        self.phone = phone
        self.address = address
        self.additional_info = additional_info
        self.is_admin = is_admin

    def save(self):
        connection = create_connection(DB_PATH)
        cursor = connection.cursor()
               
        cursor.execute('INSERT INTO user(username, password, email, phone, address, additional_info, is_admin) VALUES (?, ?, ?, ?, ?, ?, ?)', (self.username, self.password, self.email, self.phone, self.address, self.additional_info, self.is_admin))        
        connection.commit()
        
        cursor.close()
        connection.close()

    def __str__(self):
        return ('username: ' + self.username + 
            'email: ' + self.email +
            'phone: ' + self.phone + 
            'address: ' + self.address +
            'additional_info: ' + self.additional_info + 
            'is_admin: ' + self.is_admin)

    def to_json(self):
        return json.dumps(self.dict)

    

    @staticmethod
    def find_by_username(username):
        connection = create_connection(DB_PATH)
        cursor = connection.cursor()
        
        cursor.execute('SELECT * FROM user WHERE username = ?', (username,))
        rows = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        return rows

    @staticmethod
    def find(id):
        connection = create_connection(DB_PATH)
        cursor = connection.cursor()
        
        cursor.execute('SELECT * FROM user WHERE id = ?', (id,))
        rows = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        return rows[0]

    @staticmethod
    def find_all():
        connection = create_connection(DB_PATH)
        cursor = connection.cursor()
        
        cursor.execute('SELECT * FROM user')
        rows = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        return rows