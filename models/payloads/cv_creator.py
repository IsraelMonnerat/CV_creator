from pydantic import BaseModel
from typing import Optional


class Experience(BaseModel):
    company_name: str
    role_name: str
    start_date: str
    end_date: str
    description: str

class Education(BaseModel):
    university_name: str
    univerity_address: str
    course_name: str
    end_date: str
    description: str

class CreateResumePayload(BaseModel):
    language: Optional[str] = "en"
    name: str
    telephone_number: str
    email: str
    address: str
    skills: list[str]
    experience: list[Experience]
    education: list[Education]
