from fastapi import APIRouter

from schemas.notes import Note as NoteSchema

router = APIRouter()

@router.post("/")
async def create_note(note: NoteSchema):
    return {"message": "Note created successfully"}
