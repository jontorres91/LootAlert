from flask import Blueprint
watchlist = Blueprint( 'watchlist' , __name__)
from app.watchlist import routes