from flask import Blueprint, render_template
from models import Colecionador, Figurinha, ItemOferta, OfertaTroca, db


# Blueprint da home — sem url_prefix, então "/" é a raiz do site
dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def index():
    return render_template(
        "index.html", total_ofertas=ItemOferta.query.count(), total_colecionadores=Colecionador.query.count(), total_figurinhas=Figurinha.query.count()
    )