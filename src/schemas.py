from typing import Optional

from pydantic import BaseModel

from settings import BODY


class EchoDto(BaseModel):
    message: Optional[str] = BODY
