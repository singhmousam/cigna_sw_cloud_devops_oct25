from pydantic import BaseModel

class Status(BaseModel):
    app_name: str = ''
    owner: str