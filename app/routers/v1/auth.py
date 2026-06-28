from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.user import LoginRequest, UserCreate
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login")
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):
    return AuthService(db).login(credentials)


@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return AuthService(db).register(user)


@router.get("/me")
def me():
    return {"message": "Current user endpoint"}
