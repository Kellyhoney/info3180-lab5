from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from .config import Config

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    from app.models import Movie
    from app.views import main  # <-- import blueprint

    app.register_blueprint(main)  # <-- register blueprint

    return app

app = create_app()  # Needed so 'flask --app app' works
