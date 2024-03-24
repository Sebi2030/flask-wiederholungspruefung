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