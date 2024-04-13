from flask import render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user
from app import app, db, login_manager
from models import User
from forms import LoginForm, RegisterForm


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['Get', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('add'))
        else:
            error = 'Неверные учетные данные. Пожалуйста, зарегестрируйтесь.'
        return render_template('register.html', form=form, error=error)


@app.route('/register', methods=['Get', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/')
def home():
    return render_template('home.html')