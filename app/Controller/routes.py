from flask import app, jsonify, Blueprint,render_template, flash, redirect, url_for, request
from config import Config
from app import db
from app.Model.models import User, Question

bp_routes = Blueprint('routes', __name__)

@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/index', methods=['GET'])
def index():
    return jsonify({"Hello":"World"})

@bp_routes.route('/createusertest', methods=['GET'])
def createusertest():
    # Fetch the questions from the Question table
    question1 = Question.query.get(1)  # Assume valid question ID exists
    question2 = Question.query.get(2)
    question3 = Question.query.get(3)

    # Create a user with security questions
    user = User(
        username="johndoe",
        email="john@example.com",
        sec_question1_id=question1.id,
        sec_question1_answer="fido",  # answer for question 1
        sec_question2_id=question2.id,
        sec_question2_answer="pullman",  # Answer for question 2
        sec_question3_id=question3.id,
        sec_question3_answer="Herrera"  # Answer for question 3
    )
    user.set_password("prehashedpassword")

    # Add and commit the user
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('routes.index'))

