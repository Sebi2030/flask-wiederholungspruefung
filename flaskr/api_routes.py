from flask.views import MethodView
from flask_smorest import Blueprint, abort
from .models import Post, db, User
from .schemas import PostSchema, PostUpdateSchema

blp = Blueprint("posts", "posts", url_prefix="/posts", description="Operations on blog posts")

@blp.route("/")
class Posts(MethodView):
    @blp.response(200, PostSchema(many=True))
    def get(self):
        """List all posts

        Retrieve a list of all blog posts available in the database.
        This endpoint provides a way to see what articles are available to read, including their titles, authors, publication dates, and content snippets.
        """
        return Post.query.all()
    
    @blp.arguments(PostSchema)
    @blp.response(201, PostSchema)
    def post(self, new_data):
        """Add a new post

        Add a new blog post to the database.
        This endpoint allows users to create and publish new articles on the blog.
        """
        if 'author_id' in new_data and not User.query.filter_by(id=new_data['author_id']).first():
            abort(400, message="author_id doesn't exists")       
        new_post = Post(**new_data)
        db.session.add(new_post)
        db.session.commit()
        return new_post
    
    @blp.route("/<post_id>")
    class PostsById(MethodView):
        @blp.response(200, PostSchema)
        def get(self, post_id):
            """Get post by ID"""
            post = Post.query.filter_by(id=post_id).first()
            if post:
                return post
            abort(404, message="Post not found")
       
        @blp.arguments(PostUpdateSchema)
        @blp.response(200, PostSchema)
        def patch(self, update_data, post_id):
            """
            Update existing post

            Update an existing blog post in the database.
            This endpoint allows users to modify the content of an existing article.
            """
            post = Post.query.filter_by(id=post_id).first()
            if 'author_id' in update_data and not User.query.filter_by(id=update_data['author_id']).first():
                abort(400, message="author_id doesn't exists")
            if post:
                for key, value in update_data.items():
                    setattr(post, key, value)
                # Commit the changes to the database
                db.session.commit()
                return post
            abort(404, message="Post not found")
       
        @blp.response(204)
        def delete(self, post_id):
            """Delete post"""
            post = Post.query.filter_by(id=post_id).first()
            if post:
                Post.query.filter_by(id=post_id).delete()
                db.session.commit()
                return {"message": "Post deleted."}
            abort(404, message="Post not found.")
