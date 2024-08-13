from flask import render_template, redirect, url_for, flash
from app import db
from app.models import User
from app.forms import UserForm

def register_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = UserForm()
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            user = User(username=username, email=email)
            db.session.add(user)
            db.session.commit()
            flash('User added successfully!', 'success')
            return redirect(url_for('index'))
        
        users = User.query.all()
        return render_template('index.html', form=form, users=users)