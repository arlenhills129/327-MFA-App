from flask import app, jsonify, Blueprint,render_template, flash, redirect, url_for, request
from config import Config
from app import db

bp_routes = Blueprint('routes', __name__)

@bp_routes.route('/', methods=['GET'])
def index():
    return jsonify({"Hello":"World"})
