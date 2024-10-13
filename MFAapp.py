from app import create_app, db
from app.Model.models import User, Question

app = create_app()

#allows use of db and models in Flask shell
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Question':Question}


with app.app_context():
    db.create_all() #creating all tables

    #populate default security questions if not yet in db
    if Question.query.count() == 0:
            questions = [{'sec_question':'What was the name of your first pet?'},
                      {'sec_question':'In what city were you born?'},
                      {'sec_question':'What is your mother\'s maiden name?'},
                      {'sec_question':'What was the make and model of your first car?'},
                      {'sec_question':'What is the name of your elementary school?'}  ]
            
            for q in questions:
                db.session.add(Question(sec_question=q['sec_question']))

            db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)