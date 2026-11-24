import requests
from flask import Blueprint, request, jsonify

bp = Blueprint('webhook', __name__)


@bp.get('/preview')
def preview_link():
    target = request.args.get('url')
    resp = requests.get(target, timeout=5)   # SSRF: unvalidated user URL
    return jsonify({'status': resp.status_code, 'body': resp.text[:500]})
