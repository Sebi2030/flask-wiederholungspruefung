from flask.views import MethodView
from flask_smorest import Blueprint, abort
from .models import Post, db, User
from .schemas import PostSchema, PostUpdateSchema

blp = Blueprint("posts", "posts", url_prefix="/posts", description="Operations on blog posts")

@blp.route("/")
class Posts(MethodView):
    @blp.response(200, postSchema(many=True))
    def get(self):
        """List posts"""
        return Post.query.all()
    
    @blp.arguments(PostSchema)
    @blp.response(201, PostSchema)

    def post(self, new_data):
        """Add a new post"""
         if 'author_id' in new_data and not User.query.filter_by(id=new_data['author_id']).first():
            abort(400, message="author_id doesn't exists")       
        new_post = Post(**new_data)
        db.session.add(new_post)
        db.session.commit()
        return new
    