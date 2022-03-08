from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

if __name__ == "__main__":
    app.run(debug=True)


class Transfer(Resource):
    def get(self):
        return {"data": "Transfer"}


api.add_resource(Transfer, "/transfer")


# def run_main():
#     repo = {
#         "123": Account('123', 'Bartek', 444, ),
#         "456": Account('456', 'Łukasz', 0),
#         "789": Account('789', 'Michał', 300, open_transaction="123")
