from flask import Flask
from app.main import main
from app.auth import auth
from app.watchlist import watchlist

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(watchlist)
    
    return app