from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('med1.html')

@app.route('/medical')
def medical():
    return render_template('med2.html')

if __name__ == '__main__':
    app.run(debug=True)