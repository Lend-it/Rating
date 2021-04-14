import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from project.api.views import rate_blueprint

migrate = Migrate()

# instantiate the app
def create_app(script_info=None):
    # Instantiate the app
    app = Flask(__name__)

    # Set Configuration
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    from project.api.models import db

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(rate_blueprint)

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
