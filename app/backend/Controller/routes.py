from flask import app, jsonify, render_template, flash, redirect, url_for, request
from config import Config
from app import db

@app.route('/', method = ['GET'])
def index():
    return jsonify({"Hello":"World"})
