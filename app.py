import os

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, url_for, request
from flask_wtf.csrf import CSRFProtect

from db import execute_one

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Liga a proteção CSRF: todo formulário POST do sistema vai precisar do token
CSRFProtect(app)

@app.route('/')
def index():

    return render_template('index.html')

# ==============================================================================
# USUARIOS
# ==============================================================================

@app.route('/usuarios/cadastro-users', methods=['GET', 'POST'])
def cadastro_users():

    return render_template('usuarios/cadastro-users.html')


@app.route('/usuarios/lista-users')
def lista_users():

    return render_template('usuarios/lista-users.html')

# ==============================================================================
# JOGOS
# ==============================================================================

@app.route('/jogos/cadastro-jogos', methods=['GET', 'POST'])
def cadastro_jogos():

    return render_template('jogos/cadastro-jogos.html')


@app.route('/jogos/lista-jogos')
def lista_jogos():

    return render_template('jogos/lista-jogos.html')

# ==============================================================================
# PLATAFORMAS
# ==============================================================================

@app.route('/plataformas/cadastro-plataformas', methods=['GET', 'POST'])
def cadastro_plataformas():
    return render_template('plataformas/cadastro-plataformas.html')


@app.route('/plataformas/lista-plataformas')
def lista_plataformas():
    return render_template('plataformas/lista-plataformas.html')

# ==============================================================================
# PERFIL
# ==============================================================================

@app.route('/perfis/inserir', methods=['GET', 'POST'])
def inserir_perfil():

    if request.method == 'POST':
        redirect(url_for(listar_perfis))
    return render_template('perfis/perfil-form.html')

@app.route('/perfis/listar')
def listar_perfis():
    return render_template('perfis/perfis-listar.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', titulo='Sistema de Gestão')




# ==============================================================================
# TELAS DE ERROS
# ==============================================================================

@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    return render_template('404.html'), 404


@app.errorhandler(500)
def erro_no_servidor(erro):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True) 