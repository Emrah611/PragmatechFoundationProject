from flask import Flask, render_template, request, redirect
app = Flask(__name__)

data = [
    {'id': 0, 'name': 'Phone', 'price': 500}, # melumat
    {'id': 1, 'name': 'Laptop', 'price': 1000,},
    {'id': 2, 'name': 'IPad', 'price': 800,},
    {'id': 3, 'name': 'Car', 'price': 80000,}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id = data[-1]['id']
        id += 1
        name = request.form['name']
        price = request.form['price']
        data.append({'id': id, 'name': name, 'price': price})
        return redirect('/')
    return render_template('home.html', melumatlar=data, bashliq='Home')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    updatable = data[id]
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        updatable['name'] = name
        updatable['price'] = price
        data[id] = updatable
        return redirect('/')

    return render_template('update.html')

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    data.pop(id)
    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)