from flask import Flask, render_template, url_for, request
from flask_wtf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm
from models import db, User
from flask_migrate import Migrate

"""
Задание №8
Создать форму для регистрации пользователей на сайте.
Форма должна содержать поля "Имя", "Фамилия", "Email",
"Пароль" и кнопку "Зарегистрироваться".
При отправке формы данные должны сохраняться в базе
данных, а пароль должен быть зашифрован.

"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seminar3.db'
db.init_app(app)
migrate = Migrate(app, db)
app.config[
    'SECRET_KEY'] = b'b0ee5a2c6515091072087d57c6693be951cd9fc4629e5e66324c8c33331b5768'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hi'


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    context = {'alert_message': "Добро пожаловать!"}
    form = RegistrationForm()  # используется для отображения и обработки формы регистрации на веб-странице
    # строки извлекают данные, введённые пользователем
    name = form.name.data
    surname = form.surname.data
    email = form.email.data
    password = form.password.data

    if request.method == 'POST' and form.validate():
        if User.query.filter(User.name == name).all() or \
                User.query.filter(User.surname == surname).all() or \
                User.query.filter(User.email == email).all():
            context = {'alert_message': "Пользователь уже существует!"}
            return render_template('registration.html', form=form, **context)
        else:
            hashed_password = generate_password_hash(
                password)  # выполняет кодирование строки данных по стандарту PBKDF2
            new_user = User(name=name, surname=surname, email=email,
                            password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return render_template('registration.html', form=form, **context)
    return render_template('registration.html', form=form)
