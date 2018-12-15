from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

SERVER_URL = ''

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['get'])
@cross_origin(origin='*')
def hello():
    return jsonify({"hello":"world"})

if __name__ == '__main__':
    app.run(host=SERVER_URL,debug=True)
