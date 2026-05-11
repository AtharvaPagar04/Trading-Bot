class RuntimeController:

    def __init__(
        self,
    ):

        self.is_running = False

        self.is_paused = False

        self.safe_mode = False

    def start_runtime(
        self,
    ):

        self.is_running = True

    def stop_runtime(
        self,
    ):

        self.is_running = False

    def pause_runtime(
        self,
    ):

        self.is_paused = True

    def resume_runtime(
        self,
    ):

        self.is_paused = False

    def enable_safe_mode(
        self,
    ):

        self.safe_mode = True

    def disable_safe_mode(
        self,
    ):

        self.safe_mode = False