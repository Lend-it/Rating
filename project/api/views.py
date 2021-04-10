from flask import Blueprint, jsonify, request
from sqlalchemy import exc
from project.api.models import Rate
from project.api.models import db

test_blueprint = Blueprint("tasks", __name__)


@test_blueprint.route("/api/rates", methods=["GET"])
def get_all_rates():
    response = {
        "status": "success",
        "data": {"tasks": [rate.to_json() for rate in Rate.query.all()]},
    }
    return jsonify(response), 200
