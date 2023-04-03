"""
The MIT License

Copyright (c) 2010-2023 Grepper, Inc. (https://www.grepper.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from __future__ import annotations

from typing import Optional

from .answer import GrepperAnswer
from .exceptions import *

import requests


def exception_handler(status_code: str):
    if status_code == "400":
        return BadRequest
    elif status_code == "401":
        return Unauthorized
    elif status_code == "403":
        return Forbidden
    elif status_code == "404":
        return NotFound
    elif status_code == "405":
        return MethodNotAllowed
    elif status_code == "429":
        return TooManyRequests
    elif status_code == "500":
        return InternalServerError
    elif status_code == "503":
        return ServiceUnavailable


class Grepper:
    """
    Python Grepper API Wrapper
    """

    def __init__(self, api_key: str):
        self.api_key = api_key

    def search(
        self, query: str = False, similarity: Optional[int] = 60
    ):
        """This function searches all answers based on a query.

        Args:
            query (str, optional): Query to search through answer titles. ex: "Javascript loop array backwords". Defaults to False.
            similarity (Optional[int], optional): How similar the query has to be to the answer title. 1-100 where 1 is really loose matching and 100 is really strict/tight match. Defaults to 60.

        Returns:
            GrepperAnswer
        """
        response = requests.get(
            "https://api.grepper.com/v1/answers/search",
            params={"query": query, "similarity": similarity},
            auth=(self.api_key, ""),
        )
        if str(response.status_code) != "200":
            exception = exception_handler(str(response.status_code))
            raise exception(exception.__doc__)
        json_response = response.json()
        print(json_response)
        data = []
        for i in json_response["data"]:
            new_answer = GrepperAnswer(
                id=i["id"],
                content=i["content"],
                author_name=i["author_name"],
                author_profile_url=i["author_profile_url"],
                title=i["title"],
                upvotes=i["upvotes"],
                downvotes=i["downvotes"],
            )
            data.append(new_answer)
        return data
