from flask import Blueprint
from app.controllers.user_controllers import change_users, get_user, delete_users, create_user, login_user 


bp_users = Blueprint('bp_users', __name__)

bp_users.post("/register")(create_user)
bp_users.post("/login")(login_user)
bp_users.get("/users")(get_user)
bp_users.patch("/users/<id>")(change_users)
bp_users.delete("/users/<id>")(delete_users)

