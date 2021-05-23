from flask import Flask

app = Flask(__name__)

@app.route('/')    #localhost:5000
@app.route('/Home')
def Home():
    return '<h1>Salam Baki</h1>'

@app.route('/about/<aboutme>')
def about(aboutme):
    return f'About sehifesine xos geldin {aboutme}'


if __name__ == '__main__':
    app.run(debug=True)
