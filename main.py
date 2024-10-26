from fastapi import FastAPI
from routers import feed, comment_feed, sensors
import uvicorn


app = FastAPI(
    title="A&A Prototype",
    summary="Prototype Authentication and Authorization Server for mobile app development",
)

origins = [
    "http://localhost:3000",
]


@app.get("/")
async def read_root():
	return {"Hello":"World"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(feed.router)
app.include_router(comment_feed.router)
app.include_router(sensors.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)