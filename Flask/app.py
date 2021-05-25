from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('html1/index1.html')

@app.route('/MGC')
def func():
    return render_template('html2/index2.html')

if __name__ == '__main__':
    app.run(debug=True)