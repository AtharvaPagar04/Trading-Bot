from fastapi import FastAPI

from src.runtime.runtime_registry import (
    runtime_snapshot,
)
from fastapi.middleware.cors import (
    CORSMiddleware,
)
from src.runtime.runtime_controller import (
    RuntimeController,
)

app = FastAPI()

runtime_controller = (
    RuntimeController()
)
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


@app.post(
    "/runtime/start"
)
def start_runtime():

    runtime_controller.start_runtime()

    return {
        "success": True,

        "runtime_running":
        runtime_controller
        .is_running,
    }

@app.post(
    "/runtime/stop"
)
def stop_runtime():

    runtime_controller.stop_runtime()

    return {
        "success": True,

        "runtime_running":
        runtime_controller
        .is_running,
    }

@app.post(
    "/runtime/pause"
)
def pause_runtime():

    runtime_controller.pause_runtime()

    return {
        "success": True,

        "runtime_paused":
        runtime_controller
        .is_paused,
    }

@app.post(
    "/runtime/resume"
)
def resume_runtime():

    runtime_controller.resume_runtime()

    return {
        "success": True,

        "runtime_paused":
        runtime_controller
        .is_paused,
    }

@app.post(
    "/runtime/safe-mode"
)
def toggle_safe_mode():

    if runtime_controller.safe_mode:

        runtime_controller.disable_safe_mode()

    else:

        runtime_controller.enable_safe_mode()

    return {
        "success": True,

        "safe_mode":
        runtime_controller
        .safe_mode,
    }