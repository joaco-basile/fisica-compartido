from flask import Flask, request
from flask_cors import CORS


from cal import calcular

app = Flask(__name__)
CORS(app)


@app.route("/calcular/")
def index():
    masa = request.args.get("masa")
    fuerza = request.args.get("fuerza")
    ue = request.args.get("ue")
    ud = request.args.get("ud")
    inclinacion = request.args.get("inclinacion")

    response = calcular(masa, fuerza, ue, ud, inclinacion)

    return {"message": response}


if __name__ == "__main__":
    app.run(debug=True)
