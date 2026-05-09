from src.runtime.runtime_enums import RuntimeStatus


ALLOWED_TRANSITIONS = {
    RuntimeStatus.STARTING: {
        RuntimeStatus.RUNNING,
        RuntimeStatus.SHUTDOWN,
    },

    RuntimeStatus.RUNNING: {
        RuntimeStatus.PAUSED,
        RuntimeStatus.COOLDOWN,
        RuntimeStatus.EMERGENCY_STOP,
        RuntimeStatus.SHUTDOWN,
    },

    RuntimeStatus.PAUSED: {
        RuntimeStatus.RUNNING,
        RuntimeStatus.SHUTDOWN,
    },

    RuntimeStatus.COOLDOWN: {
        RuntimeStatus.RUNNING,
        RuntimeStatus.EMERGENCY_STOP,
        RuntimeStatus.SHUTDOWN,
    },

    RuntimeStatus.EMERGENCY_STOP: {
        RuntimeStatus.SHUTDOWN,
    },

    RuntimeStatus.SHUTDOWN: set(),
}