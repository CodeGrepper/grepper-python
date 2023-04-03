"""
grepper-python.exceptions
~~~~~~~~~~~~~~~~~~~
This module contains the set of grepper-python's exceptions.
"""


# 400
class BadRequest:
    """Your request is invalid."""


# 401
class Unauthorized:
    """Your API key is wrong."""


# 403
class Forbidden:
    """You do not have access to the requested resource."""


# 404
class NotFound:
    """The specified enpoint could not be found."""


# 405
class MethodNotAllowed:
    """You tried to access an enpoint with an invalid method."""


# 429
class TooManyRequests:
    """You're making too many requests! Slow down!"""


# 500
class InternalServerError:
    """We had a problem with our server. Try again later."""


# 503
class ServiceUnavailable:
    """We're temporarily offline for maintenance. Please try again later."""
