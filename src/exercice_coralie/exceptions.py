class TooMuchWorksError(Exception):
    """Exception when an elf is asked to work, when he already finished his job."""
    def __init__(self, message: str):
        self.message = message
