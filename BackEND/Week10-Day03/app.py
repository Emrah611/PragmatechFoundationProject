from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

ad = ''
soyad = ''

@app.route('/' , methods = ['GET','POST'])
def index():
    # name = request.args.get('name')
    # name = request.args['name']
    method = request.method
    global ad
    global soyad
    if request.method == 'POST':
        ad = request.form['user-ad']
        soyad = request.form['user-soyad']
        # return render_template('user.html', ad=ad,soyad=soyad)
        return redirect(url_for('user'))

    return render_template('home.html', my_method=method)
@app.route('/user')
def user():
    return render_template('user.html', ad=ad,soyad=soyad)


if __name__ == '__main__':
    app.run(debug=True)