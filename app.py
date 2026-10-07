from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def dashboard():

    return render_template('index.html')



@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    erros = []


    return render_template('cadastro.html', erros=erros)

@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/lista')
def lista():

    return render_template('lista-users.html')

if __name__ == '__main__':
    app.run(debug=True)


    