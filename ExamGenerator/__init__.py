from flask import Flask


def create_app():
    # initialize Flask App
    app = Flask(__name__)
    
    # import and register Blueprint
    from .views import views
    app.register_blueprint(views)

    return app