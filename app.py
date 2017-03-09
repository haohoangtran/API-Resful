from flask import Flask
import mlab
from models.task import Task
from flask_restful import Api
from resources.tast_resource import *

mlab.connect()

app = Flask(__name__)

api = Api(app)

api.add_resource(TaskListRes, "/tasks")
api.add_resource(TaskRes, "/tasks/<task_id>")
api.add_resource(TaskDeleteRes,"/tasks/<task_id>")
api.add_resource(TaskUpdateRes,"/tasks/<task_id>")

if __name__ == '__main__':
    app.run()
