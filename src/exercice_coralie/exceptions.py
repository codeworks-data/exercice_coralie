class TooMuchWorksError(Exception):
    """Exception lorsque le nain a beaucoup travaillé."""
    def __init__(self, message: str):
        self.message = message
