from weasyprint import HTML, CSS

from fastapi import HTTPException
from fastapi.responses import HTMLResponse

from jinja2 import Environment, FileSystemLoader
from cv_creator_enums import Languages

from models.payloads.cv_creator import CreateResumePayload


class ResumeCreatorService:
    async def create_resume(
            self, resume_data: CreateResumePayload
    ) -> HTMLResponse:
        """
            Asynchronously creates a resume based on the provided `resume_data` and returns it as an HTMLResponse object.
            Args:
                resume_data (CreateResumePayload): The data used to create the resume.
            Returns:
                HTMLResponse: The resume as an HTMLResponse object with the content type set to "application/pdf".
            Raises:
                HTTPException: If the language specified in `resume_data` is not found.
        """
        match resume_data.language:
            case Languages.English.value:
                template = Environment(loader=FileSystemLoader(".")).get_template("cv_template_english.html")
            case Languages.Portuguese.value:
                template = Environment(loader=FileSystemLoader(".")).get_template("cv_template_portuguese.html")
            case _:
                raise HTTPException(status_code=404, detail="Language not found")
        html_content = template.render(resume_data)
        pdf_content = HTML(string=html_content).write_pdf(stylesheets=[await self.get_style()])
        return HTMLResponse(content=pdf_content, media_type="application/pdf")


    @staticmethod
    async def get_style() -> CSS:
        """
            Asynchronously reads the contents of the "style.css" file and returns a CSS object.
            Returns:
                CSS: The CSS object containing the contents of the "style.css" file.
        """
        with open("style.css", "r") as file:
            return CSS(string=file.read())
