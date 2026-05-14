from fastapi import APIRouter, HTTPException
from src.monitoring.runtime_metrics import build_runtime_metrics
from src.monitoring.metrics_history import metrics_history

router = APIRouter(prefix="/api/v1/monitoring", tags=["monitoring"])

@router.get("/metrics")
def get_metrics():
    """Returns the authoritative monitoring snapshot."""
    from src.api.main import runtime_controller
    try:
        metrics = build_runtime_metrics(
            runtime_state=runtime_controller.runtime_state,
            exchange=runtime_controller.exchange,
        )
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/metrics/history")
def get_metrics_history():
    """Returns the rolling metrics history buffer."""
    return metrics_history.get_history()

