from flask import Blueprint, render_template
from flask import request, jsonify, redirect, url_for
from db_manager import db_manager
from datetime import datetime

views = Blueprint(__name__, 'views')

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/api/temperatures', methods=['GET'])
def get_daily_temperatures():
    current_date = datetime.now().date()
    query = "SELECT * FROM temperatures WHERE timestamp = %s"
    params = (current_date,)  # replace with your desired date
    data = db_manager.select(query=query, params=params)
    return jsonify(data)
