from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
def read_user():
    return {"message": "read_user"}

@router.get("/user/{user_id}")
def read_user(user_id: int):
    return {"message": "read_user", "user_id": user_id}

@router.post("/user")
async def create_user():
    return {"message": "create_user"}

@router.put("/user/{user_id}")
async def replace_user(user_id: int):
    return {"message": "replace_user", "user_id": user_id}

@router.patch("/user/{user_id}")
async def update_user(user_id: int):
    return {"message": "update_user", "user_id": user_id}

@router.delete("/user/{user_id}")
async def delete_user(user_id: int):
    return {"message": "delete_user", "user_id": user_id}

@router.delete("/user/deactivate/{user_id}")
async def deactivate_user(user_id: int):
    return {"message": "deactivate_user", "user_id": user_id}
