from app import db
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import ForeignKey

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), unique=True)

    #One-way relationship to manage security questions
    security_questions = relationship('UserQuestion')

class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    sec_question = db.Column(db.String(400), unique=True, nullable = False)

    #no relationship here

#need a one-way relationship between users and questions
#only want users to access their questions and answers, dont want other models accessing users
#or chosen questions/answers (no back population)
class UserQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.Integer, ForeignKey('question.id'), nullable=False)
    answer = db.Column(db.String(200), nullable=False)

    question = relationship('Question')
    #User has UserQuestion (and answer) has Question