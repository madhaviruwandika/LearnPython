class HttpException(Exception):
    statusCode = None
    message = None

    def __init__(self):
        super().__init__(f'Http Status Code : {self.statusCode}, message: {self.message}')

class NotFound(HttpException):
    statusCode = 404
    message = "Not Found"

class InternalServerError(HttpException):
    statusCode = 500
    message = "Internal Server Error"

def raiseErrorExample():
    raise NotFound()

raiseErrorExample()

#    raise NotFound()
#__main__.NotFound: Http Status Code : 404, message: Not Found

# Custome Decorator
## @<methodName> is used as decorator
## value should be returned