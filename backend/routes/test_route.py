from flask import Blueprint, jsonify

test_blueprint = Blueprint('test_blueprint', __name__)

@test_blueprint.route('/api/test', methods=['GET'])
def test_route():
    return jsonify(message="Hello from Flask!")
