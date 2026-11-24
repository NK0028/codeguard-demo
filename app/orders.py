from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from .models import Order

bp = Blueprint('orders', __name__)


@bp.get('/orders')
@login_required
def list_orders():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return jsonify([o.to_dict() for o in orders])


@bp.get('/orders/<int:oid>')
@login_required
def get_order(oid):
    order = Order.query.get(oid)      # fetched by id; owner is not checked
    if order is None:
        return jsonify({'error': 'not found'}), 404
    return jsonify(order.to_dict())
