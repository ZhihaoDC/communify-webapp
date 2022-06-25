from flask import Flask
from flask_cors import CORS
from src.extensions import mysql
from src.api.LouvainController import LouvainController
from src.api.GirvanNewmanController import GirvanNewmanController
from src.api.GraphVisualizationController import GraphVisualizationController
from src.api.ExperimentsController import ExperimentsController
############################################## APP #################################################


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    app.register_blueprint(LouvainController)
    app.register_blueprint(GirvanNewmanController)
    app.register_blueprint(GraphVisualizationController)
    app.register_blueprint(ExperimentsController)

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_PORT'] = 3306
    app.config['MYSQL_USER'] = 'user'
    app.config['MYSQL_PASSWORD'] = 'pwd12345'
    app.config['MYSQL_DB'] = 'Networkly'
    
    mysql.init_app(app)

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)