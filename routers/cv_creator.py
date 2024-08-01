import logging
from typing import List

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from models.payloads.cv_creator import CreateResumePayload
from models.responses.cv_creator import CreateResumeResponse
from services.cv_creator import ResumeCreatorService

router = APIRouter(tags=["CV Creator"])

@router.post("/create-resume")
async def create_resume(
    payload: CreateResumePayload
) -> CreateResumeResponse:
    payload.validate(payload)
    logging.info("Creating resume")
    return await ResumeCreatorService().create_resume(payload, "json")


@router.post("/create-resume/pdf")
async def create_resume_pdf(
    payload: CreateResumePayload
) -> HTMLResponse:
    payload.validate(payload)
    logging.info("Creating resume")
    return await ResumeCreatorService().create_resume(payload)


@router.get("/resumes/page/{page}")
async def get_resumes(page: int) -> List[CreateResumeResponse] | None:
    logging.info("Getting resumes")
    resumes = await ResumeCreatorService().get_resumes(page)
    return resumes.root if resumes else None


@router.get("/resume/id/{id_resume}")
async def get_resume(id_resume: int) -> HTMLResponse:
    logging.info("Getting resume")
    return await ResumeCreatorService().get_resume(id_resume)