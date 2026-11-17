from flask import Blueprint, jsonify
from __init__ import app

health_bp = Blueprint("health", __name__)
app.register_blueprint(health_bp)

@health_bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "healthy"
    }), 200