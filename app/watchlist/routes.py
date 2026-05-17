from app.watchlist import watchlist
from flask import render_template
@watchlist.route('/watchlist') 
def watchlist():
   return render_template('watchlist/watchlist.html') 