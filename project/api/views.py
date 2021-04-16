from flask import Blueprint, jsonify, request
from sqlalchemy import exc
from project.api.models import Rate
from project.api.models import db

rate_blueprint = Blueprint("tasks", __name__)


@rate_blueprint.route("/rating", methods=["POST"])
def add_rating():
    post_data = request.get_json()
    reviewer = request.headers.get("reviewer")
    reviewed = request.headers.get("reviewed")
    requestid = request.headers.get("requestid")

    error_response = {"status": "fail", "message": "Invalid payload."}

    if not post_data:
        return jsonify(error_response), 400

    if not reviewer or not reviewed or not requestid:
        return jsonify(error_response), 400

    stars = post_data.get("stars")
    review = post_data.get("review")
    report = post_data.get("report")

    rating_request = Rate(
        stars,
        review,
        report,
        reviewer,
        reviewed,
        requestid,
    )

    try:
        db.session.add(rating_request)
        db.session.commit()

        response = {"status": "success", "data": {"rate": rating_request.to_json()}}

        return jsonify(response), 201
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify(error_response), 400


@rate_blueprint.route("/rating", methods=["GET"])
def get_all_rates():
    response = {
        "status": "sucess",
        "data": {"rates": [rate.to_json() for rate in Rate.query.all()]},
    }
    return jsonify(response), 200
