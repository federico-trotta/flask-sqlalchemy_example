from flask import render_template
from app import db
from app.models import User

from app import create_app
app = create_app()

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)