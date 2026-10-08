from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def dashboard():

    return render_template('index.html')


@app.route('/cadastro-users', methods=['GET', 'POST'])
def cadastro_users():

    return render_template('cadastro-users.html')


@app.route('/lista-users')
def lista_users():

    return render_template('lista-users.html')


@app.route('/cadastro-jogos', methods=['GET', 'POST'])
def cadastro_jogos():

    return render_template('cadastro-jogos.html')


@app.route('/lista-jogos')
def lista_jogos():

    return render_template('lista-jogos.html')


@app.route('/cadastro-plataformas', methods=['GET', 'POST'])
def cadastro_plataformas():

    return render_template('cadastro-plataformas.html')


@app.route('/lista-plataformas')
def lista_plataformas():

    return render_template('lista-plataformas.html')



@app.route('/login')
def login():

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)


    