from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', bashliq3 = 'Home Page')

@app.route('/about')
def about():
    return render_template('about.html', bashliq2 = 'About Page')

@app.route('/contact')
def contact():
    return render_template('contact.html', bashliq = 'Contact Page')

if __name__ == '__main__':
    app.run(debug=True)
