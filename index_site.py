from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#henrique oliveira da rocha - site teste 2
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///index_site.db'
db = SQLAlchemy(app)


class Preços(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False, unique=True)


@app.route("/")
@app.route("/inicio")
def inicio():
    return render_template("inicio.html")


@app.route("/Sobre")
def Sobre():
    return render_template("Sobre.html")


@app.route("/Cardapio")
def Cardapio():
    pratos = Preços.query.all()

    return render_template("Cardapio.html", pratos=pratos)


@app.route("/Reserva")
def Reserva():
    return render_template("Reserva.html")


@app.route("/Contato")
def Contato():
    return render_template("Contato.html")



if __name__ == '__main__':
    app.run(debug=True, port=5000)

