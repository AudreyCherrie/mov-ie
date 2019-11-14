from flask import Flask
# from .config import DevConfig
# from flask_bootstrap import Bootstrap
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    #creating the app configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extensions
    bootstrap.init_app(app)

    #will add the views and forms

    # registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .requests import configure_request
    configure_request(app)
    

    return app






















# Initializing application
# app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile("config.py")

# Initializing Flask Extensions
# bootstrap = Bootstrap(app)

# from app import views
# from app import error