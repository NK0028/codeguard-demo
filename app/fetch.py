import requests
from urllib.parse import urlparse
from flask import request, abort

ALLOWED = load_allowed_hosts()


def proxy():
    url = request.args.get('url')
    if urlparse(url).hostname in ALLOWED:
        return requests.get(url).text
    abort(400)
