from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('app/index.html')

@app.route('/admin')
def Func():
    return render_template('admin/admin.html')

@app.route('/contact')
def Cont():
    return render_template('app/contact.html')

if __name__ == '__main__':
    app.run(debug=True)