import os
import psycopg2
from typing import List
from fastapi import HTTPException

from models.responses.cv_creator import CreateResumeResponse, ListCreateResumeResponse
from .connection import DbConnectionHandler


class ResumeConnectionHandler(DbConnectionHandler):
    def __init__(self):
        super().__init__()
        self.cursor = None
        self.connection = None

    async def __call__(self):
        await self.get_connection()

    async def get_connection(self) -> None:
        try:
            self.connection = psycopg2.connect(
                host=os.environ.get("DB_HOST"),
                database=os.environ.get("DB_NAME"),
                user=os.environ.get("DB_USER"),
                password=os.environ.get("DB_PASSWORD"),
                port=os.environ.get("DB_PORT")
            )
        except Exception:
            return

        self.cursor = self.connection.cursor()

    async def close_connection(self) -> None:
        if self.connection:
            self.connection.close()
            self.connection = None

        if self.cursor:
            self.cursor.close()
            self.cursor = None

    async def save_resume(self, name: str, email: str, pdf_content: str) -> int:
        if not self.connection or not self.cursor:
           return
        
        insert_query = """
            INSERT INTO resumes (name, resume_text, email)
            VALUES (%s, %s, %s)
            RETURNING resume_id
        """
        self.cursor.execute(insert_query, (name, pdf_content, email))
        self.connection.commit()
        resume_id = self.cursor.fetchone()[0]
        self.close_connection()
        return resume_id

    async def get_resumes(self, page: int = 1) -> List[CreateResumeResponse]:
        if not self.connection or not self.cursor:
            return
        offset = (page - 1) * 5
        select_query = f"""
            SELECT resume_id, name, email
            FROM resumes
            LIMIT 5 OFFSET {offset}
        """
        self.cursor.execute(select_query)
        resumes = self.cursor.fetchall()
        await self.close_connection()
        return ListCreateResumeResponse(
            root=[CreateResumeResponse(
                **dict(zip(["resume_id", "name", "email"], resume))) for resume in resumes]
        )
    
    async def get_resume(self, id_resume: int) -> bytes:
        if not self.connection or not self.cursor:
            return
        select_query = f"""
            SELECT resume_text
            FROM resumes
            WHERE resume_id = {id_resume}
        """
        self.cursor.execute(select_query)
        resume_text = self.cursor.fetchone()[0]
        await self.close_connection()
        return resume_text.encode()
