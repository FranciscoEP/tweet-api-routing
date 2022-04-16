
# from Ptyhon
from uuid import UUID
from datetime import datetime
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import Field
from models.User import User

# from User import User

class Tweet(BaseModel):
    tweet_id: UUID = Field(..., alias="id")
    content: str = Field(
        ...,
        min_length=1,
        max_length=140,
        )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)