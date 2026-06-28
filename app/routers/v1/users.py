from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
def users(
    db: Session = Depends(get_db)
):
    return AuthService(db).get_users()
