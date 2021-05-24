from flask import Flask,render_template

app = Flask(__name__)

@app.route('/html1')
def Home():
    return render_template('html1/index1.html')

@app.route('/html2')
def Func():
    return render_template('html2/index2.html')

if __name__ == '__main__':
    app.run(debug=True)