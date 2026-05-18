from app.watchlist import watchlist
from flask import render_template
@watchlist.route('/watchlist') 
def watchlist():
   games = [
        {
            "name": "Elden Ring",
            "current_price": 39.99,
            "desired_price": 25.00
        }
    ]
   return render_template("watchlist/watchlist.html", games=games) 