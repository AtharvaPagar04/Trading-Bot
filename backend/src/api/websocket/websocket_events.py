import asyncio
from src.api.websocket.runtime_stream import manager
from src.events.event_serializer import serialize_event

def register_websocket_events(event_bus):
    if event_bus is None:
        return

    def handle_event(event):
        # We need to broadcast. 
        # Create an asyncio task so we don't block the sync event_bus
        payload = serialize_event(event)
        
        # Schedule the coroutine
        try:
            loop = asyncio.get_running_loop()
            loop.create_task(manager.broadcast(payload))
        except RuntimeError:
            pass # No running loop

    event_bus.subscribe_all(handle_event)

