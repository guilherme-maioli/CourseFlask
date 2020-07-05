""" Extensão Flask """
def init_app(app):
    """ Inicialização de extensões """
    @app.route("/") # views
    def index():
        return "Hello world"

    @app.route("/contato")
    def contato():
        return "<form><input type='text'></input></form>"