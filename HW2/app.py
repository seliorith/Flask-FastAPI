from flask import Flask, render_template, redirect, url_for, request, make_response

app = Flask(__name__)


@app.route('/hello/<name>')
def hello(name):
    context = {"name": name}
    return render_template('hello.html', **context)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        login_new = request.form.get('login')
        email_new = request.form.get('email')

        # Создание ответа с перенаправлением на страницу с приветствием
        response = make_response(redirect(url_for('hello', name=login_new)))
        response.set_cookie('login', login_new)
        response.set_cookie('email', email_new)

        return response

    return render_template('index.html')


@app.route('/getcookie')
def get_cookie():
    login = request.cookies.get('login')
    email = request.cookies.get('email')
    return f'Значение cookie - Имя: {login}, Электронная почта: {email}'


@app.route('/logout', methods=['POST'])
def logout():
    # Создание ответа с перенаправлением на главную страницу
    response = make_response(redirect(url_for('index')))

    # Удаление cookie
    response.set_cookie('login', '', expires=0)
    response.set_cookie('email', '', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
