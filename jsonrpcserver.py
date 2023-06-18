from jsonrpcserver import method, Result, serve


@method
def say_hello(name):
    return Result("Hello, {}!".format(name))


if __name__ == "__main__":
    serve(host='localhost', port=8000)