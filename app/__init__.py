from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app)

    from .routes.auth import auth_bp
    from .routes.emi import emi_bp
    from .routes.stocks import stocks_bp
    from .routes.metals import metals_bp
    from .routes.news import news_bp
    from .routes.bank_rates import bank_rates_bp
    from .routes.admin import admin_bp

    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(emi_bp)
    app.register_blueprint(stocks_bp)
    app.register_blueprint(metals_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(bank_rates_bp)

    return app



