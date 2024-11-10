"""Authentication Service: blue print of the API."""
import json
from flask import Blueprint, current_app, Response

ApiMock = Blueprint('authorization_service', __name__)
API_ROOT = '/api/v1'

VALID = Response('', status=204)
INVALID = Response('Not found', status=404)


@ApiMock.route(f'{API_ROOT}/alive', methods=('GET',))
def live_probe() -> Response:
    """Use to make probes."""
    return Response('', status=204)

@ApiMock.route(f'{API_ROOT}/is_authorized/<auth_code>', methods=('GET',))
def is_authorized(auth_code: str) -> Response:
    """Check auth_code."""
    return VALID if current_app.config['service'].is_authorized(auth_code) else INVALID
@ApiMock.route(f'{API_ROOT}/user/<username>', methods=('GET',))
def get_user(username: str) -> Response:
    """Get user info."""
    user,roles = current_app.config['service'].get_user(username)
    return Response(json.dumps({"username":user,"roles":roles}), status=200) if user else INVALID
