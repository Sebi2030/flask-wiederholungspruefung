from flask.views import MethodView
from flask_smorest import Blueprint, abort
from .models import Post,db, User
from .schemas import PostSchema,PostUpdateSchema

