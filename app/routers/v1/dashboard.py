from fastapi import APIRouter, Request
from app.core.templates import templates

router = APIRouter(tags=["Dashboard"])


@router.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse(
        request,
        "dashboard.html"
    )
