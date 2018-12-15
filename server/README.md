### Setting up server-side with Python/Flask (Flask-RESTful)

Create the following file structure:

```sh
└── server/
    ├── env/
    ├── static/
    ├── templates/
    ├── README.md
    └── server.py
```

Create a `virtualenv`:

```sh
$ virtualenv env
```

Install `flask-restful` and `flask-cors`:

```sh
$ pip install flask-restful flask-cors
```

Create `server.py`, Flask-CORS enable handling of Cross Origin Resource Sharing when client-side app tries to make a HTTP request. Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs.

```sh
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api

SERVER_URL = ''

app = Flask(__name__)
CORS(app)

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return "hello"

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host=SERVER_URL, debug=True)
```

[//]: References (http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
[flask-restful docs]: <https://flask-restful.readthedocs.io/en/0.3.5/quickstart.html>
[flask-CORS]: <https://flask-cors.readthedocs.io/en/latest/>
[Buuntu/TicTacToe-Flask, This code has great structure, it was a great refresher for Flask]: <https://github.com/Buuntu/TicTacToe-Flask>
[Cledersonbc/tic-tac-toe-minimax, This developer's original code uses a 2D Array, I refactored his code to use a list]: <https://github.com/Cledersonbc/tic-tac-toe-minimax>