from flask import Flask
from flaskr.router import student

app = Flask(__name__)

app.register_blueprint(student.blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
