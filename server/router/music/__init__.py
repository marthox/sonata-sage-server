from .note import router as note_router

class NoteRouter:
    def __init__(self, app):
        app.include_router(note_router)
