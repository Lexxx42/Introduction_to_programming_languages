class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return "Hello, %s" % name
    else:
        raise BadName("Inappropriate name, %s" % name)
print("&*()")
