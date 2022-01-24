from email import message
from inspect import ArgInfo
from flask import Flask
from flask_restful import Api, Resource, reqparse,abort,fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    views = db.Column(db.Integer, nullable = False)
    likes = db.Column(db.Integer, nullable = False )

    def __repr__(self):
        return f"name = {name}, views = {views}, likes = {likes}"

#db.create_all()




video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type = str, help = "Name of video", required= True )
video_put_args.add_argument("likes", type = int, help = "Input value for Likes of video", required=True)
video_put_args.add_argument("views", type = int, help = "Views of video", required = True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type = str, help = "Name of video")
video_update_args.add_argument("likes", type = int, help = "Input value for Likes of video")
video_update_args.add_argument("views", type = int, help = "Views of video")

resource_field = {
    'id' : fields.Integer,
    'name' : fields.String,
    'views' : fields.Integer,
    'likes' : fields.Integer
}


class video(Resource):
    @marshal_with(resource_field)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404, message= 'Video not find ')
        return result
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id = video_id)
        if result:
            abort(409, message= 'Video i.d Taken')

        video = VideoModel(id = video_id, name = args['name'], views = args['views'], likes = args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201
    @marshal_with(resource_field)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id = video_id)
        if  not result:
            abort(404, 'Video doesn\'t exist')
        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        db.session.commit()
        return result 

        
    def delete(self, video_id):
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404, message= 'Video not found')
        del result
        return '', 204
api.add_resource(video, '/video/<int:video_id>')

if __name__ == "__main__":
    app.run(debug=True)