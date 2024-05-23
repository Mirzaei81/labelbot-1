import requests
from flask import Flask
from flask_restful import Api, Resource

app=Flask(__name__)
api=Api(app)

class testing(Resource):
    def get(self):
        return {"data":"testing!!!"}

api.add_resource(testing,"/test")
if __name__=="__main__":
    app.run(debug=True)
