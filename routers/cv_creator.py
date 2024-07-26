import logging

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from models.payloads.cv_creator import CreateResumePayload
from services.cv_creator import ResumeCreatorService

router = APIRouter(tags=["CV Creator"])

@router.post("/create-resume")
async def create_resume(
    payload: CreateResumePayload
) -> HTMLResponse:
    logging.info("Creating resume")
    resume = await ResumeCreatorService().create_resume(payload)
    return resume