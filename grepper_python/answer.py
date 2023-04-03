from dataclasses import dataclass


@dataclass
class GrepperAnswer:
    id: int
    content: str
    author_name: str
    author_profile_url: str
    title: str
    upvotes: int
    downvotes: int
