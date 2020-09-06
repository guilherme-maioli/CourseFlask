from flask import Flask, request

app = Flask(__name__)

@app.route("/form")
def formulario():
    return (
        "<form action='/receiver' method='post' enctype='multipart/form-data'>"
            "<label for='username'>User:</label>"
            "<input type='text' name='username' /> <br>"
            "<label for='cor'>Cor:</label>"
            "<input type='text' name='cor' /> <br>"
            "<input type='file' name='foto' /> <br>"
            "<input type='submit' value='envia ai!!' />"
        "</form>"
    )

@app.route("/receiver", methods=["POST"])
def receiver():
    __import__("ipdb").set_trace()
    return f"{request.values['username']}"
