# Self Referencing Model / Recursive Model Example with Pydantic
# Seems bit weird but sometimes we need to create models which reference themselves.

from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None  # Replies are optional; but if present, it's a list of Comment instances. By default it's None.

# Always, whenever we are using the self-referencing model, do use this:
Comment.model_rebuild()

# More about line 13:
# Known as forward references in Pydantic.
# Always required when a model references itself.

comment = Comment(
    id=1,
    content="This is the main comment.",
    replies=[
        Comment(id=2, content="This is a reply to the main comment."),
        Comment(id=3, content="This is yet another reply.", replies=[
            Comment(id=4, content="This is a nested reply.")
        ]),
    ]
)