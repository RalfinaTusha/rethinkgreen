from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Coupon:
    db_name = "rethinkgreen_db"
    def __init__(self, data):
        self.id = data['id']
        self.code = data['code']
        self.title = data['title']
        self.points = data['points']
        self.description = data['description']
        self.image = data['image']


    @classmethod
    def user_coupons(cls, data):
        query = "INSERT INTO user_coupons(user_id, coupon_id) VALUES (%(user_id)s, %(coupon_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    