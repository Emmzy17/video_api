from cgi import test
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type = str, help = "Name of vide0")
video_put_args.add_argument("likes", type = int, help = "Likes of vide0")
video_put_args.add_argument("views", type = int, help = "Views of vide0")

videos = {}

class video(Resource):
    def get(self, video_id):
        return video[video_id]
    def put(self, video_id):
        args = video_put_args.parse_args()
        return {video_id:args}

api.add_resource(video, '/video/<int:video_id>')

if __name__ == "__main__":
    app.run(debug=True)