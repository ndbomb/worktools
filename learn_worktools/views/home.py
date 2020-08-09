from flask import Blueprint, render_template, jsonify, request

home = Blueprint('home', '/')
task = Blueprint('task', '/task')

@home.route('/', methods=['GET'])
def index():
    return render_template('home.html')

@task.route('/task', methods=['GET', 'POST'])
def task_management():
    # print(request)
    # print(request.environ)
    response = jsonify({"hello": "world", "name": "中国"})
    print(response)
    print(response.data)
    return response
