from flask import app, jsonify, Blueprint,render_template, flash, redirect, url_for, request
from config import Config
from app import db

bp_auth = Blueprint('auth', __name__)