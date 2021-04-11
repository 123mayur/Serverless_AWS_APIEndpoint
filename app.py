import json
from flask import request,json
from flask_lambda import FlaskLambda
import schedule_lambda

app = FlaskLambda(__name__)

@app.route('/')
def index():
    return json_response({"message":"Hello Word"})

@app.route('/myapp',methods=['GET'])
def fetch_all():
    if request.method == 'GET':
        data = json.loads(schedule_lambda.fetch_all())
        return json_response(data)

@app.route('/myapp',methods=['POST'])
def create_schedule():
    if request.method == 'POST':
        payload = request.get_json()
        event=schedule_lambda.create_schedule(payload)
    return json_response(event)

@app.route('/myapp/<id>',methods=['DELETE'])
def removes_schedule(id):
    if request.method == 'DELETE':
        payload = request.get_json(id)
        event = schedule_lambda.delete_schedule(payload)
        return json_response(event)


@app.route('/myapp/<id>', methods=['GET'])
def fetching_schedule(id):
    if request.method == 'GET':
        payload = request.get_json(id)
        event = schedule_lambda.get_schedule(payload)
        return json_response(event)


@app.route('/myapp/<id>',methods=['PATCH'])
def update_schedule(id):
    if request.method == 'PATCH':
        payload = request.json(id)
        items = schedule_lambda.update_schedule(payload)
        return json_response(items)


def json_response(data, response_code=200):
    return json.dumps(data), response_code,{'Content-Type': 'application/json'}

def api_response():
    from flask import jsonify
    if request.method == 'POST':
        return jsonify(**request.json)

if __name__ == '__main__':
    app.run(debug=True)