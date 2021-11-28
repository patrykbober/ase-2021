from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api')
def my_microservice():
    print(request)
    response = jsonify({'Hello': 'World'})
    print(response)
    print(response.data)
    return response


if __name__ == '__main__':
    app.run()
