from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

todos = {
    1 : {"task": "Write a hello world program","summary": "write code with python."},
    2 : {"task": "Write a hello world program","summary": "write code with Java."},
    3 : {"task": "Write a hello world program","summary": "write code with C."}
}

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, help="task is required", required=True)
task_post_args.add_argument("summary", type=str, help="Summary is required", required=True)

class ToDo(Resource):
    def get(self, todo_id):
        return todos[todo_id]
    
    def post(self, todo_id):
        args = task_post_args.parse_args()
        if todo_id in todos:
            abort(409, "Task Id already taken")
        todos[todo_id] = {"task":args["task"], "summary":args["summary"]}
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