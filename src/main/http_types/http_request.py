class HttpRequest:
    def __init__(
        self,
        body: dict = None,
        header: dict = None,
        params: dict = None
    ) -> None:

        self.body = body
        self.headers = header
        self.params = params
