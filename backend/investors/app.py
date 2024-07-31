import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from apifairy import APIFairy
from werkzeug.middleware.proxy_fix import ProxyFix

# Initialize db
db = SQLAlchemy()

# for db migrations using Flask-migrate/Alembic
migrate = Migrate()

#For API schemas
ma = Marshmallow()

# For API documentation
apifairy = APIFairy()

def create_app():
    app = Flask(__name__)

	#Configure the environemnt
    app.logger.info(f'Application Environment: {os.environ.get("APP_ENV")}')
    if os.environ.get("APP_ENV") == "production":
        from config import ProdConfig
        app.config.from_object(ProdConfig())
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
    elif os.environ.get("APP_ENV") == "development":
        from config import DevConfig
        app.config.from_object(DevConfig())
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
    elif os.environ.get("APP_ENV") == "local":
        from config import LocalConfig
        app.config.from_object(LocalConfig())
    else:
        from config import Config
        app.config.from_object(Config())

    initialise_extensions(app)
    register_blueprints(app)

    from investors.seed import load_csv
    app.cli.add_command(load_csv)

    return app

def register_blueprints(app:Flask):
    from investors.api import homepage_blueprint

    app.register_blueprint(homepage_blueprint, url_prefix='/api/v1/homepage')

def initialise_extensions(app:Flask):
    apifairy.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)