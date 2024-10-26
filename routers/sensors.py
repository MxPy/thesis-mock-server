from fastapi import Depends, status, HTTPException, APIRouter, Body, Request
from fastapi.responses import Response
import schemas
from datetime import datetime
from pydantic import BaseModel

class CreateSensorDataRequestModel(BaseModel):
    userId: int
    trainingId: int
    ir: list[int]
    red: list[int]
    ax: list[int]
    ay: list[int]
    az: list[int]
    recordedAt: str




router = APIRouter(
    prefix='/sensors',
    tags=['sensors'])

@router.post("/create_sensor_data")
async def create_sensor_data(request: CreateSensorDataRequestModel):
    if request.recordedAt:
        request.recordedAt = str(request.recordedAt)
    else:
        request.recordedAt = str(datetime.now())
        
    return request
    