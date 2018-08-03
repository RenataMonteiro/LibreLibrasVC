#!flask/bin/python
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload():
    print(request.files)
    return jsonify({'resposta': 'Ok'})


if __name__ == '__main__':
    app.run(debug=True)
