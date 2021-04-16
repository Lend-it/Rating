from project.api.models import Rate, db

def add_rate(
    stars,
    review,
    report,
    reviewed,
    reviewer,
    requestid
):
    rate = Rate(stars, review, report, reviewed, reviewer, requestid)
    db.session.add(rate)
    db.session.commit()
    return rate
