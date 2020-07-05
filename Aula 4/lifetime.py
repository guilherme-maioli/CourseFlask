# Contextos 
from flask import Flask

app = Flask(__name__)

## 1- configuração
### Add configuração
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DB_URI"] = "mysql://.."

### Registrar Rotas
@app.route("/path")
def funcao():
    ...

app.add_url_rule("/path", callable)

### Inicializar extensoes
from flask_admin import Admin 
Admin.init_app(app)

### Registrar Blueprints
app.register_blueprint(...)

### add hooks
@app.before_request(...)
@app.error_handler(...)

### Chamar outras factories
views.init_app(app)


## 2 App context
### App está pronto! 'app'

### Testar
#app.test_client
#debug 
#objetos globais do flask
#(request, session, g)
#- Hooks

from flask import current_app, g

## 3 Request Context
### usar globais do flask
from flask import request, session

request.args
request.form
