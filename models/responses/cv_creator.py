from typing import List, Optional
from pydantic import BaseModel, RootModel


class CreateResumeResponse(BaseModel):
    resume_id: int
    name: str
    email: str
    message: Optional[str] = None


class ListCreateResumeResponse(RootModel[List[CreateResumeResponse]]):
    pass
