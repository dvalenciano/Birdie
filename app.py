from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
from models import user, bird, comment, location
from resources import user, bird, comment, location


app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/birdie_db"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(user.Users, '/users')
api.add_resource(user.UserDetail, '/users/<int:user_id>')
api.add_resource(bird.Birds, '/birds')
api.add_resource(bird.BirdDetail, '/birds/<int:bird_id>')
api.add_resource(comment.Comments, '/comments')
api.add_resource(comment.CommentDetail, '/comments/<int:comment_id>')
api.add_resource(location.Locations, '/locations')
api.add_resource(location.LocationDetail, '/locations/<int:location_id>')

if __name__ == '__main__':
    app.run(debug=True)
