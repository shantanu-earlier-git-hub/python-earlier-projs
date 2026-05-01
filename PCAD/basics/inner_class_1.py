class Response:

    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code

    class User:
        def __init__(self, name):
            self.name = name


if __name__ == '__main__':
    response = Response('inserted record ', 200)
    user1 = response.User('user1')

    print(f"message: {response.message} status: {response.status_code} , name : {user1.name}")
