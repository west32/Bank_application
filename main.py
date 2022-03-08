from flask import Flask
from flask_restful import Api, Resource,reqparse
from Domain.Account import Account
from Domain.Transaction import Transaction
app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video")
video_put_args.add_argument("views", type=int, help="Views of the video")
video_put_args.add_argument("likes", type=int, help="Likes on  the video")


names = {"Bart": {"age":19, "gender": "male"},
         "bill": {"age":23, "gender": "male"}}
repo = {
        "123": Account('123', 'Bartek', 444, ),
        "456": Account('456', 'Łukasz', 0),
        "789": Account('789', 'Michał', 300, open_transaction="123")}


videos = {}

class Transfer(Resource):
    def get(self, name):
        # return {"Transfer"}
        # return {"name": name, "test": test}
        return names[name]


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        return{video_id: args}

api.add_resource(Video, "/video/<int:video_id>")
api.add_resource(Transfer, "/transfer/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)

# def run_main():
#     repo = {
#         "123": Account('123', 'Bartek', 444, ),
#         "456": Account('456', 'Łukasz', 0),
#         "789": Account('789', 'Michał', 300, open_transaction="123")
