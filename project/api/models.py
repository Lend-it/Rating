from database_singleton import Singleton
from sqlalchemy.dialects.postgresql import UUID
import uuid

db = Singleton().database_connection()


class Rate(db.Model):
    __tablename__ = "rate"

    rateid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    stars = db.Column(db.Float, nullable=False)
    review = db.Column(db.Text, nullable=False)
    report = db.Column(db.Boolean, nullable=False)
    reviewed = db.Column(db.Text, nullable=False)
    reviewer = db.Column(db.Text, nullable=False)

    def __init__(self, stars, review, report, reviewed, reviewer):
        self.stars = stars
        self.review = review
        self.report = report
        self.reviewed = reviewed
        self.reviewer = reviewer
