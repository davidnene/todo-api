from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {
    1 : {"task": "Write a hello world program","summary": "write code with python."},
    2 : {"task": "Write a hello world program","summary": "write code with Java."},
    3 : {"task": "Write a hello world program","summary": "write code with C."}
}

class ToDo(Resource):
    def get(self, todo_id):
        return todos[todo_id]

class ToDoList(Resource):
    def get(self):
        return todos

api.add_resource(ToDo, '/todos/<int:todo_id>')
api.add_resource(ToDoList, "/todos")
if __name__ == "__main__":
    app.run(debug=True)