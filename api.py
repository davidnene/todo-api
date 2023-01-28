from flask import Flask, current_app
from flask_restful import Resource, Api, reqparse, abort
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
api = Api(app)

with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aqlite.db'
    db = SQLAlchemy(app)

    class ToDoModel(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        task = db.Column(db.String(200))
        summary = db.Column(db.String(500))
    db.create_all()
    print(current_app.name)




todos = {
    1 : {"task": "Write a hello world program","summary": "write code with python."},
    2 : {"task": "Write a hello world program","summary": "write code with Java."},
    3 : {"task": "Write a hello world program","summary": "write code with C."}
}

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, help="task is required", required=True)
task_post_args.add_argument("summary", type=str, help="Summary is required", required=True)

task_put_args = reqparse.RequestParser()
task_put_args.add_argument("task", type=str)
task_put_args.add_argument("summary", type=str)

class ToDo(Resource):
    def get(self, todo_id):
        return todos[todo_id]
    
    def post(self, todo_id):
        args = task_post_args.parse_args()
        if todo_id in todos:
            abort(409, "Task Id already taken")
        todos[todo_id] = {"task":args["task"], "summary":args["summary"]}
        return todos[todo_id]
    
    def put(self, todo_id):
        args = task_put_args.parse_args()
        if todo_id not in todos:
            abort(404, message="Task does not exist, cannot update")
        if args['task']:
            todos[todo_id]['task'] = args['task']
        if args['summary']:
            todos[todo_id]['summary'] = args['summary']
        return todos[todo_id]

    def delete(self, todo_id):
        del todos[todo_id]
        return todos

class ToDoList(Resource):
    def get(self):
        return todos

api.add_resource(ToDo, '/todos/<int:todo_id>')
api.add_resource(ToDoList, "/todos")


if __name__ == "__main__":
    app.run(debug=True)