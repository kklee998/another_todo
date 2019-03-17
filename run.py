from flask import Flask
from flask_cors import CORS
from app import api_bp
from Model import db


app = Flask(__name__)
CORS(app)
app.config.from_object("config")
app.register_blueprint(api_bp, url_prefix='/api')
db.init_app(app)


@app.route('/')
def its_alive():
    return "Well, it's working..."


if __name__ == "__main__":
    app.run(debug=True)
