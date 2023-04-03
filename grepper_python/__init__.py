"""
Python Grepper API
~~~~~~~~~~~~~~~~~~~
An API wrapper for the Grepper API.
"""

__title__ = "grepper-python"
__author__ = "CodeGrepper"
__license__ = "MIT"
__copyright__ = "Copyright 2010-2023 Grepper, Inc."
__version__ = "0.0.1a"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import NamedTuple, Literal

from .answer import GrepperAnswer


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(
    major=0, minor=0, micro=1, releaselevel="alpha", serial=0
)

logging.getLogger(__name__).addHandler(logging.NullHandler())

del (
    logging,
    NamedTuple,
    Literal,
)
