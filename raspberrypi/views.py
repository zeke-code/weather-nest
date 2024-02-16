from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from db_manager import db
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/configure')
def configure_page():
    return None

@views.route('/api/temperatures/', methods=['GET'])
def get_daily_temperatures():
    current_date = datetime.now().date()
    date_str = current_date.strftime('%Y-%m-%d')
    like_pattern = '%' + date_str + '%'
    query = "SELECT * FROM measurements WHERE timestamp LIKE %s"
    print('HERE IS CURRENT DATE IN STRING: ' + str(current_date))
    params = (like_pattern,)
    db_manager = db(
        user='pythonUser',
        pwd='pythonPWD',
        url='localhost',
        db='weather')
    data = db_manager.select(query=query, params=params)
    return data