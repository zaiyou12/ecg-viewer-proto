

class Fetching_Error(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self) -> str:
        return self.msg
