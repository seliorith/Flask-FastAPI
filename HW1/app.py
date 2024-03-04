from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/hero/')
def home():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')


@app.route('/jackets/')
def jackets():
    _jackets = [
        {
            "brand": "Reima",
            "season": "зима",
            "size": 128,
            "gender": "женский"
        },
        {
            "brand": "Reima",
            "season": "осень",
            "size": 140,
            "gender": "мужской"
        },
        {
            "brand": "Gusti",
            "season": "зима",
            "size": 152,
            "gender": "женский"
        },

    ]
    context = {"jackets": _jackets}
    return render_template('jackets.html', **context)


@app.route('/shoes/')
def shoes():
    _shoes = [
        {
            "brand": "Reima",
            "season": "зима",
            "size": 34,
            "gender": "женский"
        },
        {
            "brand": "Reima",
            "season": "осень",
            "size": 28,
            "gender": "мужской"
        },
        {
            "brand": "Kuoma",
            "season": "зима",
            "size": 36,
            "gender": "женский"
        },

    ]
    context = {"shoes": _shoes}
    return render_template('shoes.html', **context)


@app.route('/contact/')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
