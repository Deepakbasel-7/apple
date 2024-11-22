from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.sqlite3'


def create_database():
    db.create_all()
    print('Database Created')


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'willofD'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    # Initialize Flask-Migrate with app and db
    migrate = Migrate(app, db)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html')

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(id):
        return Customer.query.get(int(id))

    from .views import views
    from .auth import auth
    from .admin import admin
    from .models import Customer, Cart, Product, Order

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')

    return app