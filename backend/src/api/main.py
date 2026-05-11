from fastapi import FastAPI

from src.runtime.runtime_registry import (
    runtime_snapshot,
)
from fastapi.middleware.cors import (
    CORSMiddleware,
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

@app.get("/health")
async def health():

    return {
        "status": "ok"
    }


@app.get("/runtime")
async def get_runtime():

    return runtime_snapshot