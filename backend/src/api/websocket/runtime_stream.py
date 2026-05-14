from fastapi import APIRouter
from fastapi import WebSocket
from src.api.websocket.websocket_manager import WebSocketManager

router = APIRouter()

manager = WebSocketManager()

@router.websocket(
    "/ws/runtime"
)
async def runtime_websocket(
    websocket: WebSocket,
):

    await manager.connect(
        websocket
    )

    try:

        while True:
            await websocket.receive_text()

    except Exception:

        manager.disconnect(
            websocket
        )
