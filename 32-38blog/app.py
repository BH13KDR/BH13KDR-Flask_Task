from flask import Flask
from flask_mysqldb import MySQL
import yaml # pip install pyyaml
from flask_smorest import Api
from posts_routes import create_posts_blueprint

app = Flask(__name__)

db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
app.config["MYSQL_HOST"] = db_info["MYSQL_HOST"]
app.config["MYSQL_USER"] = db_info["MYSQL_USER"]
app.config["MYSQL_PASSWORD"] = db_info["MYSQL_PASSWORD"]
app.config["MYSQL_DB"] = db_info["MYSQL_DB"]
app.config["MYSQL_UNIX_SOCKET"] = db_info["MYSQL_UNIX_SOCKET"]

mysql = MySQL(app)

# blueprint
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
posts_blp = create_posts_blueprint(mysql)
api.register_blueprint(posts_blp)


if __name__ == "__main__":
    app.run(debug=True)