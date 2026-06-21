from flask import Blueprint, redirect, render_template, request, url_for

from models import Colecionador, Figurinha, ItemOferta, OfertaTroca, db

# Apelido "figurinhas" → use url_for('figurinhas.index') nos templates
figurinhas_bp = Blueprint("figurinhas", __name__, url_prefix="/figurinhas")


@figurinhas_bp.route("/")
def index():
    ofertas = OfertaTroca.listar_com_colecionador()
    return render_template("figurinhas/lista_ofertas.html", ofertas=ofertas)


@figurinhas_bp.route("/oferta/cadastrar", methods=["GET", "POST"])
def cadastrar_oferta():
    colecionadores = Colecionador.listar()
    figurinhas = Figurinha.listar()
    if request.method == "POST":
        # TODO ALUNO: criar OfertaTroca + ItemOferta (oferece/deseja)
        oferta = OfertaTroca(colecionador_id=request.form["colecionador_id"], observacao=request.form["observacao"])
        db.session.add(oferta)
        db.session.commit()
        item = ItemOferta(oferta_id=oferta.id, figurinha_id=request.form["figurinha_oferece_id"], tipo="oferece")
        db.session.add(item)
        db.session.commit()
        item = ItemOferta(oferta_id=oferta.id, figurinha_id=request.form["figurinha_deseja_id"], tipo="deseja")
        db.session.add(item)
        db.session.commit()
        return redirect(url_for("figurinhas.index"))

    return render_template(
        "figurinhas/formulario_oferta.html",
        colecionadores=colecionadores,
        figurinhas=figurinhas,
    )
