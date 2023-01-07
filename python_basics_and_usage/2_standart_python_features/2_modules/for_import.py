GREETING = "Hello, "
_SECOND_GREETING = "Hello, "


class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return _SECOND_GREETING + name
    else:
        raise BadName("Inappropriate name, %s" % name)


print("&*()")

#__all__ = ["BadName", "greet"]
