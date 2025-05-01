from .user import router as user_router

class UserRouter:
    def __init__(self, app):
        app.include_router(user_router)
