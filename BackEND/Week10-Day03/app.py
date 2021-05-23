from flask import Flask

app = Flask(__name__)


@app.route('/')
def tapsiriq():
    return 'Tapsiriq Hazirdi'

@app.route('/<Salam>')
def home(Salam):
    return f'{Salam} xos geldin.'

@app.route('/Sorgu')
def sorgu():
    return 'Sorgu hazirdi' 


if __name__ == '__main__':
    app.run(debug=True)