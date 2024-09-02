from fastapi import Depends, status, HTTPException, APIRouter, Body, Request
from fastapi.responses import Response
import schemas



router = APIRouter(
    prefix='/comment_feed',
    tags=['comment_feed'])

@router.get("/popular")
def Feed():
    return {"exist":True}