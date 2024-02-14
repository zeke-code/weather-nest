from flask import Blueprint, render_template
from flask import request, jsonify, redirect, url_for, current_app
from db_manager import db_manager

views = Blueprint(__name__, 'views')

@views.route('/')
def home():
    return render_template('index.html')
