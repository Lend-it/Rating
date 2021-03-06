from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid

db = SQLAlchemy()


class Rate(db.Model):
    __tablename__ = "rate"

    rateid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    stars = db.Column(db.Float, nullable=False)
    review = db.Column(db.Text, nullable=True, default="")
    report = db.Column(db.Boolean, nullable=False)
    reviewed = db.Column(db.Text, nullable=False)
    reviewer = db.Column(db.Text, nullable=False)
    requestid = db.Column(UUID(as_uuid=True), nullable=False)

    def __init__(self, stars, review, report, reviewed, reviewer, requestid):
        self.stars = stars
        self.review = review
        self.report = report
        self.reviewed = reviewed
        self.reviewer = reviewer
        self.requestid = requestid

    def to_json(self):
        return {
            "rateid": self.rateid,
            "stars": self.stars,
            "review": self.review,
            "report": self.report,
            "reviewed": self.reviewed,
            "reviewer": self.reviewer,
            "requestid": self.requestid,
        }
