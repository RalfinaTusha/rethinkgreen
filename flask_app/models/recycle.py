from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Recycle:
    db_name = "rethinkgreen_db"
    def __init__(self, data):
        self.id = data['id']
        self.address = data['address']
        self.material = data['material']
        self.items = data['items']
        self.image = data['image']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recycles (address, material, items, image, user_id) VALUES (%(address)s, %(material)s, %(items)s, %(image)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    
    @classmethod
    def get_recycles(cls, data):
        query = "SELECT * FROM recycles WHERE user_id = %(id)s LIMIT 3;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        recycles = []
        for item in results:
            recycles.append(cls(item))
        return recycles
        
    @staticmethod
    def validate_recycle(data):
        is_valid = True
        if data['totalItems'] is None or (int)(data['totalItems']) < 0:
            is_valid = False

        return is_valid
    
    