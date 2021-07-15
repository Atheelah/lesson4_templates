from flask import Flask, render_template

app = Flask(__name__)


@app.route('/students')
def form():
    dictionary = {'Atheelah': 20, 'Abdurazak': 25, 'Apple': 24, 'Banana': 18}
    return render_template('homepage.html', dictionary=dictionary)


@app.route('/<name>')
def homepage(name):
    return render_template("homepage.html", name=name)


@app.route('/loopy/<int:number>')
def loopy(number):
    return render_template('numbers_page.html', number=number)


if __name__ == '__main__':
    app.debug = True
    app.run()
