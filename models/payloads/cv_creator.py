from pydantic import BaseModel
from typing import Optional
from fastapi import HTTPException

from services.utils import validate_field



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

    @classmethod
    def validate_payload(cls, field: str) -> None:
        if not validate_field(field=field, pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'):
            raise HTTPException(status_code=400, detail=f"Invalid field format: {field}")

    @classmethod
    def validate(cls, payload: dict) -> None:
        cls.validate_payload(payload.email)
