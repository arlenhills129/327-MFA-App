from app import db
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import ForeignKey
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)

    #will need to implement hashing
    password_hash = db.Column(db.String(128))

    #hashing functions go here
    #hoping to implement my own
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def check_password(self, password):
        return self.get_password(password)

    email = db.Column(db.String(120), unique=True)

    #storing chosen security questions and the respective answers per user
    #will need to hash answers as well.
    #i think this current solution doesn't prevent duplicates
    sec_question1_id = db.Column(db.Integer, ForeignKey('question.id'), nullable=False)
    sec_question1_answer = db.Column(db.String(200), nullable=False)

    sec_question2_id = db.Column(db.Integer, ForeignKey('question.id'), nullable=False)
    sec_question2_answer = db.Column(db.String(200), nullable=False)

    sec_question3_id = db.Column(db.Integer, ForeignKey('question.id'), nullable=False)
    sec_question3_answer = db.Column(db.String(200), nullable=False)

    #relating security questions to questions in the Question table
    sec_question1 = db.relationship('Question', foreign_keys=[sec_question1_id])
    sec_question2 = db.relationship('Question', foreign_keys=[sec_question2_id])
    sec_question3 = db.relationship('Question', foreign_keys=[sec_question3_id])

class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    sec_question = db.Column(db.String(400), unique=True, nullable = False)