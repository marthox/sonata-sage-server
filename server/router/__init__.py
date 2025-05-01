from .user import UserRouter
from .note import NoteRouter

class Router:
    def __init__(self, app):
        UserRouter(app)
        NoteRouter(app)

