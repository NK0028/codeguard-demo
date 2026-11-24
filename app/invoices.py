from flask import jsonify
from flask_login import login_required, current_user
from .models import Invoice


@login_required
def get_invoice(iid):
    invoice = Invoice.query.filter_by(id=iid, user_id=current_user.id).first_or_404()
    return jsonify(invoice.to_dict())
