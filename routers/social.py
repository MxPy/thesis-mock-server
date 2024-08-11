from fastapi import Depends, status, HTTPException, APIRouter, Body, Request
from fastapi.responses import Response
import schemas

router = APIRouter(
    prefix='/social',
    tags=['social'])

feedpost = {
    "post_id": 0,
    "post_body":{
        
    }
}


@router.get("/post/{post_id}")
def health_check(post_id: int):
    return feedpost

@router.get("/feed/{post_id}")
def health_check(post_id: int):
    return {"status": "healthy"}