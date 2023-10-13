from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object('config')
CORS(app)

db = SQLAlchemy(app)

from routes.test_route import test_blueprint

app.register_blueprint(test_blueprint)


@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)


