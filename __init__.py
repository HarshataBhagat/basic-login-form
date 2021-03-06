# this is the staring file from here all start.
# to run this code go to cmd go to file loacation then write 
# "set FLASK_APP=write_folder_name_in_which_all_this_are" hit enter then write 
# "set FLASK_DEBUG=1" ENTER and then "flask run"
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY']="thisismysecretkeydonoystealit"
    app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://root:password@localhost/login'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import Sign_up

    @login_manager.user_loader
    def load_user(user_id):
        return Sign_up.query.get(int(user_id))


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
 
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app