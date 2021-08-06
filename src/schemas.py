from pydantic import BaseModel
from settings import BODY

class EchoDto(BaseModel):
    message: str = BODY