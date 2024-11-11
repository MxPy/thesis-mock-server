from fastapi import APIRouter, Depends, status, HTTPException, UploadFile
from fastapi.background import BackgroundTasks
from fastapi.responses import FileResponse
from typing import Dict
from pydantic import BaseModel
import logging
from datetime import datetime

# Pydantic Models
class User(BaseModel):
    userId: str
    nickName: str

class UserResponse(BaseModel):
    nickName: str
    avatar: str
    created_at: str

router = APIRouter(prefix="/forum", tags=["forum"])
logger = logging.getLogger()

# Mock data storage
mock_users = {
    "user123": {
        "userId": "user123",
        "nickName": "TestUser",
        "avatar": "http://localhost:9001/avatars/default.png",
        "created_at": datetime.utcnow().isoformat()
    }
}

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(request: User) -> Dict[str, str]:
    if request.userId in mock_users:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    
    mock_users[request.userId] = {
        "userId": request.userId,
        "nickName": request.nickName,
        "avatar": "http://localhost:9001/avatars/default.png",
        "created_at": datetime.utcnow().isoformat()
    }
    
    return {"details": "User created successfully"}

@router.get('/whoami', status_code=status.HTTP_200_OK)
async def get_user(userId: str) -> UserResponse:
    if userId not in mock_users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {userId} not found"
        )
    
    user_data = mock_users[userId]
    return UserResponse(**user_data)
