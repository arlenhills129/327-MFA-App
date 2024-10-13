from app import create_app, db
from app.backend.Model.models import User, Question

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': app.db, 'User': User, 'Question':Question}

@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()


if __name__ == "__main__":
    app.run(debug=True)