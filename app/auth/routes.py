from app.auth import auth
@auth.route('/login') 
def login():
   return "LootAlert Login"