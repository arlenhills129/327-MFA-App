from app import create_app, db
from app.Model.models import User, Question

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': app.db, 'User': User, 'Question':Question}

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)